from flask import Flask, jsonify, request
import tensorflow as tf
import numpy as np
from PIL import Image
import base64
from io import BytesIO

print("Loading Crop Models ....")
# Corn_model = tf.keras.models.load_model('./Crops_Models/Corn_Saved_Model')
print("Loaded Crop Models!")

app = Flask(__name__)

def preprocess_base64_image(base64_string):
    # Convert base64 string to bytes
    img_data = base64.b64decode(base64_string)
    
    # Read image from bytes
    img = Image.open(BytesIO(img_data))
    
    img = img.resize((32, 32))
    img = img.convert('RGB')
    
    img_array = np.array(img)
    img_array = img_array.astype('float32') / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array


@app.route("/")
def home():
    return "Hello World", 200

@app.route('/image',methods=['POST'])
def process_image():
    try:
        data = request.json
        crop = data["type"]
        name = data["name"]

        input_image = preprocess_base64_image(data["filebase64"])
      
        return {"status":"true", "name":name}
    except error:
        return {"status:":"false","error":error}

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"status": 404, "message": "Not Found"}), 404