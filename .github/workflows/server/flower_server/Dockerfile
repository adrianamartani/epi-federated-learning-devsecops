# Dockerfile do flower_server (VERSÃO FINAL E ESTÁVEL)

# 1. Use uma imagem base mais robusta, mas ainda leve.
# O 'slim-buster' é a base Debian 10, que é mais estável.
FROM python:3.10-slim-buster 
WORKDIR /app

# Copia o requirements.txt (Deve conter flwr, numpy, boto3)
COPY requirements.txt .

# 2. INSTALAÇÃO DE DEPENDÊNCIAS DE SISTEMA
# Instalamos apenas as bibliotecas de RUNTIME que o NumPy/PyTorch precisam
# e que podem não estar na imagem base.
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Bibliotecas de runtime C/C++ essenciais
    libstdc++6 \
    libgomp1 \
    # Biblioteca de Fortran para NumPy/SciPy (versão mais moderna que gfortran)
    libgfortran5 \
    && rm -rf /var/lib/apt/lists/*
    
# 3. INSTALAÇÃO DE DEPENDÊNCIAS PYTHON (flwr, numpy, boto3)
# Esta etapa agora usa as bibliotecas de runtime acima e não precisa compilar PyTorch
RUN pip install --no-cache-dir -r requirements.txt

# 4. INSTALAÇÃO DO PYTORCH VIA WHEEL (SEPARADA)
# Garantimos que torch seja instalado de forma binária.
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# 5. Copia o código da aplicação e define o comando
COPY app.py .
CMD ["python", "app.py"]