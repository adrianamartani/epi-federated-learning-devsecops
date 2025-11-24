# Dockerfile do flower_server (Versão FINAL)
FROM python:3.10-slim
WORKDIR /app

# 1. Copia o requirements.txt (AGORA SEM O PACOTE 'torch')
COPY requirements.txt .

# 2. INSTALAÇÃO DE DEPENDÊNCIAS DE SISTEMA
# Removemos a maioria das ferramentas de build (build-essential, gfortran, etc.)
# e mantemos APENAS as bibliotecas de runtime essenciais.
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Mantemos bibliotecas essenciais para SSL, OpenBLAS e Runtime
    libssl-dev \
    libffi-dev \
    libopenblas-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*
    
# 3. INSTALAÇÃO DE DEPENDÊNCIAS PYTHON (flwr, numpy, boto3)
# O flwr e o numpy agora instalam sem problemas.
RUN pip install --no-cache-dir -r requirements.txt

# 4. INSTALAÇÃO DO PYTORCH VIA WHEEL PRÉ-COMPILADO
# Forçamos o uso do índice de wheels do PyTorch, que garante a instalação de um binário compatível com CPU.
# Use a URL de índice para a versão mais recente do PyTorch que suporte Python 3.10
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# 5. LIMPEZA FINAL DA IMAGEM
# Mantemos apenas a limpeza de cache.
RUN apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 6. Copia o código da aplicação
COPY app.py .

# 7. Define o comando de execução
CMD ["python", "app.py"]