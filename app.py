
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
import tensorflow as tf  # Make sure TensorFlow is imported if used directly
import numpy as np  # NumPy is used for numerical operations
from PIL import Image, ImageOps  # Pillow is required for image manipulation

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'static/images'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Load the model and labels globally if they don't change
model = tf.saved_model.load('model/model.savedmodel')

# Make sure to handle errors/exceptions in your production code
with open('labels.txt', 'r') as file:
    labels = [line.strip() for line in file.readlines() if line.strip()]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict_route():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file'}), 400

    file = request.files['image']
    filename = secure_filename(file.filename)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(image_path)

    predicted_class, confidence = predict_image(image_path)
    return jsonify({'class': predicted_class, 'confidence': confidence})


def predict_image(image_path):
    # Your existing image processing code
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    img = Image.open(image_path).convert('RGB')
    img = ImageOps.fit(img, (224, 224), Image.Resampling.LANCZOS)
    img_array = np.array(img)
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    # Run prediction
    prediction = model(data, training=False)
    index = np.argmax(prediction)
    class_name = labels[index] if index < len(labels) else "Index out of range"
    confidence = float(prediction[0][index])

    return class_name, confidence


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)