FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .

# 1. Instalação das dependências do sistema
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential

# 2. Instalação das dependências do Python
# SE ESTA LINHA FALHAR, o problema está no requirements.txt ou em uma biblioteca de sistema faltante.
RUN pip install --no-cache-dir -r requirements.txt

# 3. Limpeza (Otimização do tamanho da imagem)
RUN apt-get purge -y build-essential \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY app.py .
CMD ["python", "app.py"]