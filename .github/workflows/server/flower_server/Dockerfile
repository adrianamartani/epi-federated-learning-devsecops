# Flower Server Dockerfile
FROM python:3.10-slim
WORKDIR /app

# Colocamos o requirements.txt antes de qualquer RUN que o utilize
COPY requirements.txt .

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        # Ferramentas de compilação C/C++ (para flwr/numpy/outras)
        build-essential \
        # OBRIGATÓRIO para PyTorch (torch) em imagens slim
        libstdc++6 \
        # Adição útil para otimizações matemáticas
        gfortran \
    \
    && pip install --no-cache-dir -r requirements.txt \
    \
    # Limpeza para reduzir o tamanho final da imagem:
    # Remove as ferramentas de build que não são necessárias em runtime
    && apt-get purge -y build-essential gfortran \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2. Copia o código da aplicação
COPY app.py .

# 3. Define o comando de execução
CMD ["python", "app.py"]