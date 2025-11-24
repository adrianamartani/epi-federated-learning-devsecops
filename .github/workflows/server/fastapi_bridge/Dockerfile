# FastAPI Bridge Dockerfile
FROM python:3.10-slim
WORKDIR /app

# 1. Instala dependências e limpa o cache
COPY requirements.txt .

RUN apt-get update \
    && pip install --no-cache-dir -r requirements.txt \
    # Limpa o cache do apt imediatamente para reduzir o tamanho
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2. Copia o código da aplicação (main.py e quaisquer outros arquivos)
COPY main.py .

# 3. Define o comando de execução
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]