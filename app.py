from flask import Flask, render_template, request, session
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
import uuid


app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "medical-chatbot-dev-secret")

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


embeddings = download_embeddings()

index_name = "medical-chatbot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

chat_model = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
    temperature=0
)

qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{question}"),
    ]
)

condense_question_prompt = PromptTemplate.from_template(
    contextualize_q_system_prompt
)

# Per-browser-session ConversationBufferMemory store
_conversation_memories = {}


def _get_session_id():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    return session["session_id"]


def _get_memory():
    """Return ConversationBufferMemory for the current browser session."""
    sid = _get_session_id()
    if sid not in _conversation_memories:
        _conversation_memories[sid] = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer",
        )
    return _conversation_memories[sid]


def _build_chain(memory):
    return ConversationalRetrievalChain.from_llm(
        llm=chat_model,
        retriever=retriever,
        memory=memory,
        condense_question_prompt=condense_question_prompt,
        combine_docs_chain_kwargs={"prompt": qa_prompt},
        return_source_documents=False,
        verbose=True,
    )


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print("User:", msg)

    memory = _get_memory()
    print("Chat history:", memory.buffer)

    chain = _build_chain(memory)
    response = chain.invoke({"question": msg})
    answer = response["answer"]
    print("Response:", answer)

    return str(answer)


@app.route("/clear", methods=["POST"])
def clear_history():
    sid = session.get("session_id")
    if sid and sid in _conversation_memories:
        _conversation_memories[sid].clear()
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
