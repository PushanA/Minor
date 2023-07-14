import numpy as np
import cv2
from tensorflow.keras.preprocessing import image 
from tensorflow.keras.models import Model
from tensorflow.keras.models import load_model
from flask import Flask, render_template, request


model=Model
model= load_model('Xception(4).h5')

app = Flask(__name__)


@app.route('/', methods=['GET'])
def man():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def predict():
    print("MOdel running")
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)
    
    img = cv2.imread(image_path)
    img= cv2.resize(img,(224,224))
    img = image.img_to_array(img)
    img= np.array(img)
    img= np.expand_dims(img, axis=0)
   # image = load_img(image_path, target_size=(224,224,3))
    #image = image.reshape((1,image.shape[0], image.shape[1], image.shape[2]))
    # image = ImageDataGenerator(
    #     rescale=1./255,
    #     shear_range=0.2,
    #     zoom_range=0.2,
    #     horizontal_flip=True)
    
    yhat = model.predict(img)
    print("/n")
    print("/n")
    print("/n")
    print (yhat)
    print("/n")
    print("/n")
    print("/n")

    if (yhat==1):
        classification = 'Autistic'
    elif(yhat==0):
        classification = 'Not Autistic'
    return render_template('home.html',prediction=classification)

if __name__ == '__main__':
    app.run(port=3000, debug=True)

    #onchange="readURL(this)"
#active="{{url_for('home')}}

