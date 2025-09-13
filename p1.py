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
        print("Your crop is healthy, no lack of any nutrients.")
    else:
        #print(f"You have this disease: {class_labels_first[predicted_class_first]}")
        predictions = sm.predict(ni_array)

        second_class_labels = ['nitrogen', 'phosphorus', 'potassium']

        # Get the predicted class index
        predicted_class_index = np.argmax(predictions[0])

        # Get the predicted class label
        predicted_class_label = second_class_labels[predicted_class_index]

        
  

image_path = "IMG_3826.jpg"
pdanl(image_path)