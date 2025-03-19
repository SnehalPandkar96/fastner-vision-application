import time
from ultralytics import YOLO
import cv2
import os
from pathlib import Path

# Define paths
model_path = '/content/drive/MyDrive/fastner-vision-application/backend/model/best.pt'  # Path to your trained model
test_images_path = '/content/drive/MyDrive/fastner-vision-application/test_images/'  # Folder with test images
output_folder = '/content/drive/MyDrive/fastner-vision-application/output_images/'  # Folder to save results

# Create output folder if it doesn't exist
Path(output_folder).mkdir(parents=True, exist_ok=True)

# Load the trained YOLOv8 model
model = YOLO(model_path)

# Function to run inference on a single image
def run_inference(image_path):
    # Read image
    image = cv2.imread(image_path)

    # Run inference
    results = model(image)

    # Measure inference time
    start_time = time.time()
    results = model(image)
    inference_time = time.time() - start_time

    # Show and save the detection results
    result_image = results[0].plot()  # The image with detections
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    cv2.imwrite(output_path, result_image)

    # Print the inference time and return the output image
    print(f"Inference time for {image_path}: {inference_time:.4f} seconds")

# Run inference on all test images
for image_name in os.listdir(test_images_path):
    image_path = os.path.join(test_images_path, image_name)
    if image_path.endswith(('.jpg', '.jpeg', '.png', '.tiff')):  # Check if the file is an image
        run_inference(image_path)
