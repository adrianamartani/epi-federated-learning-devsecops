# Flower Server Dockerfile
FROM python:3.10-slim
WORKDIR /app

# 1. Copia o requirements.txt primeiro para otimizar o cache
COPY requirements.txt .

# 2. INSTALAÇÃO DAS DEPENDÊNCIAS DE BUILD (Ferramentas de Compilação e Bibliotecas Essenciais)
# MANTENHA ESTA ETAPA SEPARADA!
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libstdc++6 \
    gfortran \
    libssl-dev \
    libffi-dev \
    # Adicionar libhdf5-dev se o flwr/torch usar HDF5. Descomentar se necessário.
    # libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*
    
# 3. INSTALAÇÃO DAS DEPENDÊNCIAS PYTHON
# ESTA É A LINHA QUE ESTAVA FALHANDO. Agora ela é uma camada de build única.
RUN pip install --no-cache-dir -r requirements.txt

# 4. LIMPEZA FINAL (Remove as ferramentas de build que não são necessárias em runtime)
# MANTENHA ESTA ETAPA SEPARADA!
RUN apt-get purge -y build-essential gfortran libssl-dev libffi-dev \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 5. Copia o código da aplicação
COPY app.py .

# 6. Define o comando de execução
CMD ["python", "app.py"]