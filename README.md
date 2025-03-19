# fastner-vision-application
Detection & Classification Demo

This repository contains a full-stack demo application for object detection and classification using YOLOv8. It includes:

- **Backend API** built with FastAPI.
- **Frontend Application** built with React.
- **Documentation** outlining system architecture and model training details.

## Folder Structure

The project is structured as follows:

- **`README.md`**: Provides project overview and documentation.
- **`requirements.txt`**: List of Python dependencies needed to run the project.
- **`.gitignore`**: Specifies files and directories to be ignored by Git.

### Backend:
- **`model/`**: Contains the trained model (`best.pt`).
- **`inference/`**: Holds scripts responsible for running inference.
- **`utils/`**: Contains any utility functions (optional).

### Frontend:
- **`public/`**: Contains static files like HTML, images, etc., for the frontend.
- **`src/`**: The source code of the React app, including components and entry point files (`App.js`, `index.js`).
- **`package.json`**: Manages React app dependencies and scripts.

### Scripts:
- **`test.py`**: Script for testing the model, running inference on input images, and saving results.

### Data:
- **`input_images/`**: Folder to store input images for inference.
- **`output_images/`**: Folder to store the images with detection results.

### Documentation:
- **`setup.md`**: Setup instructions for the project.
