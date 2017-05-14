# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

# Generate a description of the model in json format
# Генерируем описание модели в формате json
def creating_json(model):
     model_json = model.to_json()
     
     #Write model to the file
     # Записываем модель в файл
     json_file = open("mnist_model.json", "w")
     json_file.write(model_json)

     json_file.close()
     
     # Save weight to the file
     # Сохраняем веса в файл
     model.save_weights("mnist_model.h5")

''''''

''''''
# Set the seed to repeat the results
# Устанавливаем seed для повторяемости результатов
numpy.random.seed(42)

# Uploading data
# Загружаем данные
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Image size conversion
# Преобразование размерности изображений
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)

# Normalization of the data
# Нормализация данных
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# Convert labels to categories
# Преобразуем метки в категории
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)


# 0 -> [1, 0, 0, 0, 0, 0, 0, 0, 0 ,0]
# 1 -> [0, 1, 0, 0, 0, 0, 0, 0, 0 ,0]
# 2 -> [0, 0, 1, 0, 0, 0, 0, 0, 0 ,0]
# 3 -> [0, 0, 0, 1, 0, 0, 0, 0, 0 ,0]
# 4 -> [0, 1, 0, 0, 1, 0, 0, 0, 0 ,0]
# 5 -> [0, 0, 0, 0, 0, 1, 0, 0, 0 ,0]
# 6 -> [0, 0, 0, 0, 0, 0, 1, 0, 0 ,0]
# 7 -> [0, 0, 0, 0, 0, 0, 0, 1, 0 ,0]
# 8 -> [0, 0, 0, 0, 0, 0, 0, 0, 1 ,0]
# 8 -> [0, 0, 0, 0, 0, 0, 0, 0, 0 ,1]

# Create a consistent model
# Создаем последовательную модель
model = Sequential()

# Add network levels
# Добавляем уровни сети
model.add( Dense(800, input_dim = 784, activation = "relu", kernel_initializer = "normal") )
model.add( Dense(10, activation="softmax", kernel_initializer = "normal") )

# Compile the model
# Компилируем модель
model.compile(loss="categorical_crossentropy", optimizer = "SGD", metrics = ["accuracy"])

print(model.summary())

# Training the network
# Обучаем сеть
model.fit(X_train, Y_train, batch_size = 25, epochs = 150, validation_split = 0.2, verbose = 2)

# Evaluating the quality of online learning on test data
# Оцениваем качество обучения сети на тестовых данных
scores = model.evaluate(X_test, Y_test, verbose = 0)
print("Точность работы на тестовых данных: %.2f%%" % (scores[1] * 100))

# 
creating_json(model)