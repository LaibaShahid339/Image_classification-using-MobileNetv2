from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import matplotlib.pyplot as plt
import numpy as np
from keras.models import load_model

def make_predictions(image_path):
    model = load_model('model.keras')
    load_img = load_preprocess(image_path)
    predictions = model.predict(load_img)
    decoded_predictions = decode_predictions(predictions, top=3)[0]
    result = []
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        result.append(f"{i + 1}: {label} ({score:.2f})")
    return result



def load_preprocess(image_path):
    img = image.load_img(image_path, target_size=(224,224))
    image_array = image.img_to_array(img)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = preprocess_input(image_array)
    return image_array

