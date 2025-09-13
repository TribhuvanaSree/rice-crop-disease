from flask import Flask, request, render_template, jsonify,send_from_directory
import subprocess
import pandas as pd
import time
import tensorflow as tf
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
import numpy as np

with open('model1.json', 'r') as json_file:
    loaded_model_json = json_file.read()

fm = model_from_json(loaded_model_json)
fm.load_weights('model1.h5')

with open('model2.json', 'r') as json_file:
    loaded_model_json2 = json_file.read()

sm = model_from_json(loaded_model_json2)
sm.load_weights('model2.h5') 

def pdanl(image_path):
    ni = image.load_img(image_path, target_size=(224, 224))
    ni_array = image.img_to_array(ni)
    ni_array = np.expand_dims(ni_array, axis=0)
    ni_array /= 255.0  
    ni2 = image.load_img(image_path, target_size=(256, 256))
    ni_array2 = image.img_to_array(ni2)
    ni_array2 = np.expand_dims(ni_array2, axis=0)
    ni_array2 /= 255.0  

    prediction_first = fm.predict(ni_array2)
    predicted_class_first = np.argmax(prediction_first)
    class_labels_first = {0: 'BrownSpot', 1: 'Healthy', 2: 'Hispa', 3: 'LeafBlast'}

    if predicted_class_first == 1:
        return "Your crop is healthy, no lack of any nutrients."
    else:
        #return f"You have this disease: {class_labels_first[predicted_class_first]}"
        predictions = sm.predict(ni_array)

        #second_class_labels = ['nitrogen', 'phosphorus', 'potassium']

        # Get the predicted class index
        predicted_class_index = np.argmax(predictions[0])

        # Get the predicted class label
        predicted_class_label = second_class_labels[predicted_class_index]
        return f"You have this disease: {class_labels_first[predicted_class_first]}, Lack of {predicted_class_label}."
second_class_labels = ['nitrogen', 'phosphorus', 'potassium']
app = Flask(__name__)
data = pd.read_excel(r"D:\epics work\Book1.xlsx")
current_row = 0

# Serve static CSS files
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_data', methods=['POST'])
def get_data():
    try:
        print("here")
        result = subprocess.check_output(['python', 'link2.py'], universal_newlines=True, stderr=subprocess.STDOUT)
        print("here1")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return result
@app.route('/get_data_mois', methods=['POST'])
def get_data_mois():
    try:
        print("here")
        result = subprocess.check_output(['python', 'linkmois.py'], universal_newlines=True, stderr=subprocess.STDOUT)
        print("here1")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return result
@app.route('/get_data_ph', methods=['POST'])
def get_data_ph():
    try:
        print("here")
        result =subprocess.check_output(['python', 'linkPh.py'], universal_newlines=True, stderr=subprocess.STDOUT)
        print("here1")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return result
@app.route('/get_data_ec', methods=['POST'])
def get_data_ec():
    try:
        print("here")
        result = subprocess.check_output(['python', 'linkEc.py'], universal_newlines=True, stderr=subprocess.STDOUT)
        print("here1")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return result
@app.route('/get_data_npk', methods=['POST'])
def get_data_npk():
    try:
        print("here")
        result = subprocess.check_output(['python', 'linkNPK.py'], universal_newlines=True, stderr=subprocess.STDOUT)
        print("here1")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return result

@app.route('/datta', methods=['POST'])
def datta():
    try:
        result = pdanl("phos.jpg")
    except subprocess.CalledProcessError as e:
        result = f"Error: {e.output}"
    
    return result

if __name__ == "__main__":
    app.run(debug=True)