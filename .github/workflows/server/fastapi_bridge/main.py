from fastapi import FastAPI
import os, requests

app = FastAPI()
ORION = os.getenv("ORION_URL", "http://orion:1026")

@app.post("/detection")
def post_detection(payload: dict):
    # payload example: {"id":"cam1-001","timestamp":"2025-11-11T10:00:00","detections":[...]}
    entity = {
        "id": f"Detection:{payload.get('id','0')}",
        "type": "EPI_Detection",
        "timestamp": {"type":"Property", "value": payload.get("timestamp")},
        "detections": {"type":"Property", "value": payload.get("detections")}
    }
    headers = {"Content-Type": "application/ld+json"}
    try:
        res = requests.post(f"{ORION}/ngsi-ld/v1/entities/", json=entity, headers=headers, timeout=5)
        return {"status": res.status_code, "text": res.text}
    except Exception as e:
        return {"error": str(e)}
