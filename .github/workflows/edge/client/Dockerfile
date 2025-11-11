FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 && pip install --no-cache-dir -r requirements.txt
COPY fl_client.py detector.py frame_receiver.py .
CMD ["python", "frame_receiver.py"]
# note: para rodar o cliente FL, em dev você executa fl_client.py separadamente.
