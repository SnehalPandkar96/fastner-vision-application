from flask import Flask, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np

app = Flask(__name__)

# Load the YOLOv8 model from the model folder
model = YOLO("model/yolov8s.pt")

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Read image from the file stream
    file_bytes = np.frombuffer(file.read(), np.uint8)
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
    
    return jsonify({'detections': detections})

if __name__ == '__main__':
    app.run(debug=True)
