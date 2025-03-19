from fastapi import FastAPI, File, UploadFile, HTTPException
from ultralytics import YOLO
import cv2
import numpy as np
import uvicorn

app = FastAPI()

# Load the YOLOv8 model from the model folder
model = YOLO("model/best.pt")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file provided")

    # Read image from the file stream
    file_bytes = np.frombuffer(await file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Run model prediction
    results = model(img)
    detections = []
    for result in results:
        boxes = result.boxes
        for box in boxes:
            xyxy = box.xyxy[0].tolist()  # Bounding box coordinates
            conf = box.conf[0].item()
            cls = int(box.cls[0].item())
            detections.append({'bbox': xyxy, 'confidence': conf, 'class': cls})
    
    return {"detections": detections}

if __name__ == "__main__":
    !python -m uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
