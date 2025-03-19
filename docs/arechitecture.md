# System Architecture and Workflow

The system consists of two main components:

1. **Backend API**:
   - Built using Flask.
   - Loads a YOLOv8 model for object detection.
   - Provides a `/predict` endpoint to process images and return detections.

2. **Frontend Application**:
   - Built with React.
   - Allows users to upload images.
   - Displays detection results including bounding boxes, class labels, and confidence scores.

## Workflow:
1. The user uploads an image via the React UI.
2. The image is sent to the Flask backend.
3. The YOLOv8 model processes the image and returns detection results.
4. The frontend displays the results.
