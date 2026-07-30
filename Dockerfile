FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir \--index-url https://download.pytorch.org/whl/cpu torch==2.7.1


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "app.py"]