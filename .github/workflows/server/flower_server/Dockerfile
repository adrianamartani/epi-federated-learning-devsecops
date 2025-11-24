# Dockerfile do flower_server (FINAL)
FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt . # Deve conter flwr, numpy, boto3

# 2. INSTALAÇÃO DE DEPENDÊNCIAS DE SISTEMA (REFORÇADA)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gfortran \
    # Adicionado libc-dev para garantir todos os headers C/C++
    libc-dev \ 
    libstdc++6 \
    libssl-dev \
    libffi-dev \
    libopenblas-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*
    
# 3. INSTALAÇÃO DE DEPENDÊNCIAS PYTHON (flwr, numpy, boto3)
# O build só passará se todas as dependências acima estiverem corretas.
RUN pip install --no-cache-dir -r requirements.txt

# 4. INSTALAÇÃO DO PYTORCH VIA WHEEL (SEPARADA)
# Garantir que torch seja instalado de forma binária e não tente compilar
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# 5. LIMPEZA FINAL DA IMAGEM
# Removemos os pacotes de desenvolvimento para otimizar o tamanho
RUN apt-get purge -y build-essential gfortran libc-dev libssl-dev libffi-dev \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY app.py .
CMD ["python", "app.py"]