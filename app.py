from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model('saved_model.h5')
image_size = (180, 180)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    image = load_img(file, target_size=image_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    return jsonify({'prediction': 'Dog' if prediction > 0.5 else 'Cat'})

if __name__ == '__main__':
    app.run(debug=True)
