FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && pip install --no-cache-dir -r requirements.txt
COPY main.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
