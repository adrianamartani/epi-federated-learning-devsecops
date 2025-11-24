# Dockerfile do flower_server 
FROM python:3.10-slim-buster 
WORKDIR /app

# Copia o requirements.txt (flwr, numpy, boto3)
COPY requirements.txt .

# 2. INSTALAÇÃO DE DEPENDÊNCIAS DE SISTEMA 
RUN apt-get update && apt-get install -y --no-install-recommends \
    libstdc++6 \
    libgomp1 \
    # CORREÇÃO: Usamos o nome de pacote genérico para a biblioteca Fortran
    libgfortran-dev \
    && rm -rf /var/lib/apt/lists/*
    
# 3. INSTALAÇÃO DE DEPENDÊNCIAS PYTHON 
RUN pip install --no-cache-dir -r requirements.txt

# 4. INSTALAÇÃO DO PYTORCH VIA WHEEL (SEPARADA)
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu

# 5. Copia o código da aplicação e comandos finais...
COPY app.py .
CMD ["python", "app.py"]