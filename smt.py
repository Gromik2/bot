import tensorflow as tf

def predict_custom_image(img_path):
    from tensorflow.keras.preprocessing import image
    import numpy as np

    model = tf.keras.models.load_model('cat_dog_model.h5')

    img = image.load_img(img_path, targer_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    prediction = model.predict(img_array)

    if prediction[0] > 0.5:
        print("Это собака")
    else:
        print("Это кот")

predict_custom_image("PetImages 2/Cat/27.jpg")
