from flask import Flask, request
import cv2
import numpy as np
import requests
import os
from detector import detect
app = Flask(__name__)

FASTAPI_BRIDGE = os.getenv("FASTAPI_BRIDGE", "http://SERVER_PUBLIC_IP:8000")  # ajuste

@app.route("/frame", methods=["POST"])
def frame():
    file = request.files.get("image")
    if not file:
        return {"status":"no image"}, 400
    data = file.read()
    arr = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    cv2.imwrite("last.jpg", img)
    detections = detect("last.jpg")
    payload = {"id":"edge-client-1", "timestamp": "2025-11-11T00:00:00Z", "detections": detections}
    try:
        res = requests.post(f"{FASTAPI_BRIDGE}/detection", json=payload, timeout=3)
        return {"status":"ok", "bridge":res.status_code}
    except Exception as e:
        return {"status":"ok", "bridge_error":str(e)}
