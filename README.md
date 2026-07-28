# medical-chatbot

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)
![Framework](https://img.shields.io/badge/framework-Flask-red.svg?logo=flask&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-GPT--4o-412991.svg?logo=openai&logoColor=white)
![Vector DB](https://img.shields.io/badge/VectorDB-Pinecone-000000.svg?logoColor=white)
![Status](https://img.shields.io/badge/status-Active-brightgreen.svg)

**A production-ready AI-powered medical chatbot leveraging Retrieval-Augmented Generation (RAG) for accurate, context-aware medical information retrieval.**



</div>

---

## 🎯 Overview

The **End-to-End Medical Chatbot** is an intelligent conversational system designed to provide accurate, evidence-based medical information. It combines the power of **Retrieval-Augmented Generation (RAG)** with state-of-the-art language models to ensure responses are grounded in a verified medical knowledge base, minimizing hallucinations and maximizing reliability.

### Key Highlights

✅ **RAG-Powered**: Retrieves relevant medical context before generating responses  
✅ **Production-Ready**: Fully containerized with CI/CD pipeline  
✅ **Scalable**: Built with Pinecone for high-performance vector search  
✅ **Enterprise-Grade**: Uses Groq as free tool for superior response quality  
✅ **Easy Deployment**: Docker + GitHub Actions automation  

---

## ✨ Features

- 🤖 **Smart Q&A**: Context-aware medical question answering using RAG
- 📚 **PDF Knowledge Base**: Automatic ingestion and processing of medical documents
- ⚡ **Vector Search**: Efficient similarity search powered by Pinecone
- 🧠 **Advanced LLM**: GPT-4o for high-quality natural language generation
- 🎨 **User-Friendly Interface**: Intuitive web chat UI with real-time responses
- 🔒 **Environment-Based Config**: Secure credential management via `.env`
- 🐳 **Docker Support**: Containerized deployment for consistency
- 🚀 **CI/CD Pipeline**: Automated deployment to AWS via GitHub Actions
- 📝 **Comprehensive Docs**: Full documentation and architecture guides

---

## 🏗️ Architecture

### System Overview

The chatbot follows a classic RAG architecture pattern:

```
┌─────────────────────────────────────────────────────────────┐
│                   Medical Chatbot System                     │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │           User Interface (Flask Web App)              │   │
│  │  • HTML/CSS/JavaScript Chat Interface                │   │
│  │  • Real-time Response Display                        │   │
│  └──────────────┬───────────────────────────────────────┘   │
│                 │                                             │
│  ┌──────────────▼───────────────────────────────────────┐   │
│  │         Flask Backend (app.py)                        │   │
│  │  • Route Handlers (/get, /)                          │   │
│  │  • Request Validation                                │   │
│  └──────────────┬───────────────────────────────────────┘   │
│                 │                                             │
│  ┌──────────────▼───────────────────────────────────────┐   │
│  │      LangChain RAG Pipeline                          │   │
│  │  • Retrieval Chain                                   │   │
│  │  • Document Combination                             │   │
│  │  • Prompt Management                                │   │
│  └──────────────┬───────────────────────────────────────┘   │
│                 │                                             │
│    ┌────────────┴──────────────┬──────────────┐              │
│    │                           │              │              │
│  ┌─▼──────────┐          ┌────▼──┐    ┌─────▼────┐          │
│  │ Pinecone   │          │ Groq   │    │ HuggingFace│        │
│  │ Vector DB  │          │  LLM│    │ Embeddings│        │
│  └────────────┘          └───────┘    └───────────┘         │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```


---

## 📁 Project Structure

```
End-to-End-Medical-Chatbot/
├── 📄 app.py                          # Main Flask application
├── 📄 store_index.py                  # Data ingestion & Pinecone indexing
├── 📄 requirements.txt                # Python dependencies
├── 📄 setup.py                        # Package setup configuration
├── 📄 Dockerfile                      # Docker container configuration
├── 📄 .env.example                    # Example environment variables
├── 📄 README.md                       # This file
│
├── 📁 src/                            # Source code modules
│   ├── __init__.py
│   ├── helper.py                      # PDF loading, text splitting, embeddings
│   └── prompt.py                      # System prompts for the chatbot
│
├── 📁 templates/                      # HTML templates
│   └── chat.html                      # Chat interface template
│
├── 📁 static/                         # Static files (CSS, JS, images)
│   └── style.css                      # Chat UI styling
│
├── 📁 data/                           # Medical PDF documents (input data)
│   └── *.pdf                          # Your medical documents
│
├── 📁 docs/                           # Documentation files
│   ├── ARCHITECTURE.md                # Detailed architecture documentation
│   ├── INSTALLATION.md                # Detailed installation guide
│   ├── API.md                         # API endpoint documentation
│   └── DEVELOPMENT.md                 # Development guidelines
│
├── 📁 workflows/                      # Process workflows and diagrams
│   ├── data_flow.mmd                  # Data flow diagram
│   ├── rag_pipeline.mmd               # RAG pipeline workflow
│   ├── user_query_flow.mmd            # Query processing flow
│   └── deployment_pipeline.mmd        # CI/CD deployment flow
│
├── 📁 research/                       # Research notebooks
│   └── demo.ipynb                     # Demo and experimentation
│
├── 📁 all-utils/                      # Utility modules and examples
│   ├── main.py
│   ├── utilities/                     # Utility notebooks and scripts
│   └── db/                            # Local database cache
│
├── 📁 .github/                        # GitHub configuration
│   └── workflows/                     # CI/CD workflow files
│
└── 📁 medical_chatbot.egg-info/       # Package metadata

```

---

## 🚀 Installation

### Using UV (Faster)

UV is significantly faster for dependency resolution and installation (~10x faster than pip).

#### Step 1-2: Clone and Navigate


#### Step 3: Create Virtual Environment with UV

```bash
# Create and activate a UV-managed Python environment
uv venv --python 3.10 .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

#### Step 4: Install Dependencies with UV

```bash
uv pip install -r requirements.txt
```

#### Step 5-6: Configure and Run

**Why UV?**
- ⚡ **10x faster** dependency resolution
- 📦 **Simpler syntax** than pip
- 🔒 **Better lock files** for reproducibility
- 🎯 **Drop-in replacement** for pip

---

## 💬 Usage

### Web Interface

Once the application is running at `http://localhost:8080`:

1. **Open your browser** and navigate to `http://localhost:8080`
2. **Type your medical query** in the chat input box
3. **Press Enter** or click Send
4. **Receive AI-generated response** based on your knowledge base

## 🔌 API Endpoints

### GET `/`

Returns the chat interface HTML page.

**Response**: HTML chat UI

---

### POST `/get`

Processes user queries and returns AI-generated responses.

**Request Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `msg` | string | Yes | User's medical query |

**Example Request:**

```bash
curl -X POST http://localhost:8080/get \
  -d "msg=What are the symptoms of diabetes?"
```

**Example Response:**

```
Diabetes symptoms include increased thirst, frequent urination, fatigue, 
and blurred vision. More serious symptoms may include slow wound healing, 
tingling in the extremities, and recurring infections.
```

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Language** | Python 3.10+ | Core programming language |
| **Web Framework** | Flask 3.1+ | Web server and routing |
| **LLM Orchestration** | LangChain 0.3+ | RAG pipeline management |
| **Large Language Model** | GPT-4o (OpenAI) | Natural language generation |
| **Vector Database** | Pinecone | Semantic search and embedding storage |
| **Embeddings** | HuggingFace (all-MiniLM-L6-v2) | Text-to-vector conversion (384-dim) |
| **PDF Processing** | PyPDF2 | PDF document parsing |
| **Environment Config** | python-dotenv | Secure credential management |
| **Frontend** | HTML/CSS/JavaScript | User chat interface |
| **Containerization** | Docker | Application containerization |
| **CI/CD** | GitHub Actions | Automated deployment pipeline |
| **Deployment** | AWS (EC2, ECR) | Cloud infrastructure |



## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Amit Awasthi**
- Email: amitawasthi.dev@gmail.com

---

## ⭐ Acknowledgments

- Groq for Groq API
- Pinecone for vector database infrastructure
- LangChain for RAG orchestration framework
- HuggingFace for embedding models


### Techstack Used:

- Python
- LangChain
- Flask
- GPT
- Pinecone



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_DEFAULT_REGION
   - ECR_REPO
   - PINECONE_API_KEY
   - OPENAI_API_KEY
