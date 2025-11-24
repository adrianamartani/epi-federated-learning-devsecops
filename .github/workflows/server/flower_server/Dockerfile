# Flower Server Dockerfile
FROM python:3.10-slim
WORKDIR /app

# 1. Copia o requirements.txt
COPY requirements.txt .

# 2. INSTALAÇÃO DAS DEPENDÊNCIAS DE BUILD E RUNTIME NECESSÁRIAS
# Substituímos o problemático 'libatlas-base-dev' por 'libopenblas-dev'.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libstdc++6 \
    gfortran \
    libssl-dev \
    libffi-dev \
    # Substituição para OpenBLAS:
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*
    
# 3. INSTALAÇÃO DAS DEPENDÊNCIAS PYTHON
RUN pip install --no-cache-dir -r requirements.txt

# 4. LIMPEZA FINAL
# Garante que as ferramentas de build sejam removidas, mas mantém as bibliotecas de runtime necessárias.
RUN apt-get purge -y build-essential gfortran libssl-dev libffi-dev libopenblas-dev \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 5. Copia o código da aplicação
COPY app.py .

# 6. Define o comando de execução
CMD ["python", "app.py"]