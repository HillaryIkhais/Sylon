FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install dashscope openai

COPY . .

CMD ["uvicorn", "openserv.server:app", "--host", "0.0.0.0", "--port", "8080"]
