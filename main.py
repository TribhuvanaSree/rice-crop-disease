from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the model architecture from JSON
with open('model2.json', 'r') as json_file:
    model_json = json_file.read()

model = model_from_json(model_json)

# Load the model weights
model.load_weights('model2.h5')

# Rest of the code remains the same...
def preprocess_image(img_path, target_size=(224, 224)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Rescale to [0, 1]
    return img_array

# Function to make a prediction
def predict_logo(img_path):
    processed_image = preprocess_image(img_path)
    predictions = model.predict(processed_image)

    class_labels = ['nitrogen', 'phosphorus', 'potassium']

    # Get the predicted class index
    predicted_class_index = np.argmax(predictions[0])

    # Get the predicted class label
    predicted_class_label = class_labels[predicted_class_index]

    # Print the predictions
    print(f'Predicted class index: {predicted_class_index}')
    print(f'Predicted class label: {predicted_class_label}')
    print('Predictions for each class:')
    for i, label in enumerate(class_labels):
        print(f'{label}: {predictions[0][i]:.4f}')

# Get user input for image file path
image_path = "untitled-171.jpg"
# Perform prediction
predict_logo(image_path)
