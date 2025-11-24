# Flower Server Dockerfile
FROM python:3.10-slim
WORKDIR /app

# 1. Instala dependências do sistema necessárias para compilação (ex: NumPy)
COPY requirements.txt .

RUN apt-get update \
    # Instala o build-essential (que inclui o gcc) e evita pacotes recomendados desnecessários
    && apt-get install -y --no-install-recommends \
        build-essential \
    && pip install --no-cache-dir -r requirements.txt \
    # Limpa o cache do apt e remove pacotes de build para reduzir o tamanho da imagem final
    && apt-get purge -y build-essential \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2. Copia o código da aplicação
COPY app.py .

# 3. Define o comando de execução (assumindo que 'app.py' é o ponto de entrada)
CMD ["python", "app.py"]