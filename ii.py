import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

data = np.load('mnist_data (1).npz')

x_train = data['x_train']
y_train = data['y_train']
x_test = data['x_test']
y_test = data['y_test']

x_train, x_test = x_train / 255.0, x_test / 255.0

model = models.Sequential([
    layers.Reshape((28, 28, 1), input_shape=(28, 28)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10)
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Тестовая точность: {test_acc}")

def predict_custom_image(img_path):
    from PIL import Image, ImageOps

    img = Image.open(img_path).convert("L")
    img = ImageOps.invert(img)
    img = ImageOps.fit(img, (28, 28), method=Image.Resampling.LANCZOS)
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    confidence = np.max(predictions)
    print(f"Предсказанная цифра: {predicted_class} (уверенность: {confidence: .2f})")

predict_custom_image("pixel art/pixil-frame-0-24.png")
predict_custom_image("pixel art/pixil-frame-0-25.png")
predict_custom_image("pixel art/pixil-frame-0-26.png")
predict_custom_image("pixel art/pixil-frame-0-27.png")
predict_custom_image("pixel art/pixil-frame-0-28.png")
predict_custom_image("pixel art/pixil-frame-0-29.png")
predict_custom_image("pixel art/pixil-frame-0-30.png")
predict_custom_image("pixel art/pixil-frame-0-31.png")
predict_custom_image("pixel art/pixil-frame-0-32.png")
predict_custom_image("pixel art/pixil-frame-0-33.png")
predict_custom_image("pixel art/pixil-frame-0-34.png")
predict_custom_image("pixel art/pixil-frame-0-35.png")
predict_custom_image("pixel art/pixil-frame-0-36.png")
predict_custom_image("pixel art/pixil-frame-0-37.png")
predict_custom_image("pixel art/pixil-frame-0-38.png")
predict_custom_image("pixel art/pixil-frame-0-39.png")
predict_custom_image("pixel art/pixil-frame-0-40.png")
predict_custom_image("pixel art/pixil-frame-0-41.png")
predict_custom_image("pixel art/pixil-frame-0-42.png")
predict_custom_image("pixel art/pixil-frame-0-43.png")


if input("Сохранить? 1 - Да, 2 - Нет") == "1":
    model.save("mnist_model.h5")