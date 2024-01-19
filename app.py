from flask import Flask, render_template, request
import tensorflow as tf
from keras.preprocessing import image
import numpy as np

app = Flask(__name__, static_url_path='/static')

# Load the pre-trained CNN model
cnn = tf.keras.models.load_model("Pneumonia_Model.h5")

# Define a route for the home page
@app.route('/')
def index():
    return render_template('index.html')
# Define a route for the second page with the image upload form
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return render_template('page2.html', error='No file part')

    file = request.files['image']

    if file.filename == '':
        return render_template('page2.html', error='No selected file')

    # Save the uploaded file to a temporary location
    file_path = 'temp_image.jpg'
    file.save(file_path)

    # Load and preprocess the uploaded image
    img = image.load_img(file_path, target_size=(64, 64))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # Make prediction using the loaded model
    result = cnn.predict(img_array)

    # Remove the temporary file
    import os
    os.remove(file_path)

    # Determine the prediction result
    if result[0][0] == 1:
        prediction = 'Pneumonia'
        
        hospital_link = "https://www.medifee.com/list/best-pulmonology-hospitals#odg" 
        
        doctors_link = "https://www.clinicspots.com/pulmonologist/india"
        
        return render_template('resultforPneumonia.html', prediction=prediction, hospital_link =hospital_link , doctors_link=doctors_link)

    else:
        prediction = 'Normal'
        
    return render_template('resultforNormal.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
    
# Run the app on a specific host and port
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5001)