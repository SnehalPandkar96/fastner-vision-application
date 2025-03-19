
# fastner-vision-application
Detection & Classification Demo

This repository contains a full-stack demo application for object detection and classification using YOLOv8. It includes:

- **Backend API** built with FastAPI.
- **Frontend Application** built with React.
- **Documentation** outlining system architecture and model training details.

## Folder Structure

fastner-vision-application/ │ ├── README.md # Project description and documentation ├── requirements.txt # List of required Python packages ├── .gitignore # Files/folders to be ignored by Git │ ├── backend/ # Backend logic (model, inference, etc.) │ ├── model/ # Folder for model files │ │ └── best.pt # Trained model file │ ├── inference/ # Inference-related scripts │ │ └── inference.py # Inference script for model (e.g., main.py or inference.py) │ └── utils/ # Utility functions (optional) │ └── helper.py # Helper functions for inference │ ├── scripts/ # Testing and execution scripts │ └── test.py # Test script for running inference and saving results │ ├── data/ # Folder for storing input data and outputs │ ├── input_images/ # Input images for inference │ └── output_images/ # Folder to store inference results (detection images) │ ├── docs/ # Documentation for the project └── setup.md # Setup instructions and details for contributors
