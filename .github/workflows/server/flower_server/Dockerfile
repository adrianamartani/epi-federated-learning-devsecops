# Usa uma imagem Python leve e estável
FROM python:3.10-slim

# Define o diretório de trabalho no container
WORKDIR /app

# 1. Copia apenas o requirements.txt (Melhora o cache)
# Se o requirements.txt não mudar, as próximas camadas não precisam ser reconstruídas.
COPY requirements.txt .

# 2. INSTALAÇÃO DAS DEPENDÊNCIAS DO SISTEMA (Build e Runtime)
# Resolve o problema do "apt-get exit code: 100" e o "pip install exit code: 1"
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        # Ferramentas de compilação (necessário para PyTorch/NumPy/flwr)
        build-essential \
        gfortran \
        # Bibliotecas de Runtime e Headers (essenciais para PyTorch/SSL/OpenBLAS)
        libstdc++6 \
        libssl-dev \
        libffi-dev \
        libopenblas-dev \
        libgomp1 \
    && rm -rf /var/lib/apt/lists/*
    
# 3. INSTALAÇÃO DAS DEPENDÊNCIAS PYTHON
# Esta etapa é isolada e garantida pelas ferramentas instaladas acima.
RUN pip install --no-cache-dir -r requirements.txt

# 4. LIMPEZA FINAL DA IMAGEM
# Remove as ferramentas de desenvolvimento (build-essential, gfortran) 
# para reduzir o tamanho da imagem, mas MANTÉM as bibliotecas de runtime necessárias.
RUN apt-get purge -y build-essential gfortran \
    && apt-get autoremove -y \
    && apt-get clean

# 5. Copia o código da aplicação
COPY app.py .
# Se houver outros arquivos/diretórios, use: COPY . .

# 6. Define o comando de execução
CMD ["python", "app.py"]