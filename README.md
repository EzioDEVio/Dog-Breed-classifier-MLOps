
# Dog Breed Classifier Using Teachable Machine and Flask

This project demonstrates how to build a dog breed classifier using Google's Teachable Machine and deploy it using a Flask web application. The application allows users to upload an image of a dog and returns the predicted breed along with a confidence level.

## Project Setup

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8+
- pip (Python package installer)
- Virtual environment (optional but recommended)

### Setting Up the Project

1. **Clone the Repository**

   Start by cloning this repository to your local machine:

   ```bash
   git clone https://github.com/EzioDEVio/Dog-Breed-classifier-MLOps.git
   cd Dog-Breed-classifier-MLOps
   ```

2. **Create and Activate a Virtual Environment (Optional)**

   For Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   For macOS and Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Required Packages**

   Install all the required packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

### Train Your Model with Teachable Machine

1. **Go to [Teachable Machine](https://teachablemachine.withgoogle.com/) and create a new project.**
2. **Select "Image Project" and upload images of various dog breeds.**
3. **Train the model and export it as a TensorFlow model.**
4. **Download the model files (`model.json` and weights) and place them in the `model/` directory of your project.**

### Setting Up Flask Application

1. **Application Structure**

   Ensure your project structure looks like this:

   ```
   Dog-Breed-classifier-MLOps/
   ├── model/
   │   ├── model.json
   │   ├── group1-shard1of1.bin
   ├── static/
   │   ├── css/
   │   │   └── style.css
   │   ├── js/
   │   │   └── script.js
   │   ├── images/  # for uploaded images
   ├── templates/
   │   └── index.html
   ├── app.py
   ├── predict.py
   ├── requirements.txt
   ├── README.md
   ```

2. **Implementing Flask Routes**

   In `app.py`, set up routes for loading the home page and handling the image prediction:

   ```python
   from flask import Flask, render_template, request, jsonify
   import predict

   app = Flask(__name__)

   @app.route('/')
   def index():
       return render_template('index.html')

   @app.route('/predict', methods=['POST'])
   def predict_route():
       # implementation for handling prediction
   ```

3. **Implementing the Prediction Logic**

   In `predict.py`, implement the function to handle the image processing and model prediction:

   ```python
   import tensorflow as tf

   def predict_image(image_path):
       # Load and preprocess the image
       # Predict the breed using the loaded model
   ```

### Running the Flask Application

1. **Start the Flask Server**

   Run the following command to start the Flask server:

   ```bash
   flask run
   ```

   The application should now be running on `http://127.0.0.1:5000/`.

### Interacting with the Application

1. **Open your web browser and go to `http://127.0.0.1:5000/`.**
2. **Upload an image of a dog and click the "Predict" button.**
3. **View the predicted breed and confidence level displayed on the page.**

## Deployment

1. **Dockerize the Flask Application**

   Create a `Dockerfile` in the root of the project and build the Docker image:

   ```dockerfile
   # Use an official Python runtime as a base image
   FROM python:3.9-slim

   # Set the working directory to /app
   WORKDIR /app

   # Copy the current directory contents into the container at /app
   COPY . /app

   # Install any needed packages specified in requirements.txt
   RUN pip install --no-cache-dir -r requirements.txt

   # Make port 5000 available to the world outside this container
   EXPOSE 5000

   # Define environment variable
   ENV NAME World

   # Run app.py when the container launches
   CMD ["flask", "run
