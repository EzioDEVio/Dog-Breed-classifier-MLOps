
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps

def load_and_prepare_image(image_path):
    img = Image.open(image_path).convert('RGB')
    img = ImageOps.fit(img, (224, 224), Image.Resampling.LANCZOS)
    img_array = np.array(img)
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    return normalized_image_array

def predict_image(model, image_path, class_labels):
    print(f"Predicting image: {image_path}")
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = load_and_prepare_image(image_path)

    prediction = model(data, training=False)
    index = np.argmax(prediction)
    class_name = class_labels[index] if index < len(class_labels) else "Index out of range"
    confidence = prediction[0][index]

    return class_name, confidence

# Load the model
model = tf.saved_model.load('model/model.savedmodel')

# Load the labels and extract class names
with open('labels.txt', 'r') as file:
    labels = [line.strip().split(' ', 1)[1] for line in file if ' ' in line.strip()]

# Debugging: Print the loaded labels
print("Loaded labels:", labels)

# Predict an image
image_path = 'images/image1.jpg'
predicted_class, confidence = predict_image(model, image_path, labels)
print(f"Predicted Class: {predicted_class}, Confidence: {confidence:.4f}")