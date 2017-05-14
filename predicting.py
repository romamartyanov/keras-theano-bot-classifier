# -*- coding: utf-8 -*-
"""
Created on Sun May 14 01:12:55 2017

@author: iromi
"""
import numpy

from PIL import Image
from keras.models import model_from_json

def predicting(image_name):
     im = Image.open(image_name)
     im_grey = im.convert('L')
     
     im_array = numpy.array(im_grey)
     im_array = numpy.reshape(im_array, (1, 784)).astype('float32')
     
     # Invert the image
     # Инвертируем изображение
     x = 255 - im_array
     
     # Normalize the image
     # Нормализуем изображение
     x /= 255
     
     # Loading the network architecture data from the json file 
     # Загружаем данные об архитектуре сети из файла json
     json_file = open("neural_network_json/mnist_model.json", "r")
     loaded_model_json = json_file.read()
     json_file.close()
     
     # Create a model based on the uploaded data
     # Создаем модель на основе загруженных данных
     loaded_model = model_from_json(loaded_model_json)
     
     # Load the weights in the model
     # Загружаем веса в модель
     loaded_model.load_weights("neural_network_json/mnist_model.h5")
     
     # Compiling the model
     # Компилируем модель
     loaded_model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])

     # The neural network predicts an image class
     # Нейронная сеть предсказывает класс изображения
     prediction = loaded_model.predict(x)
     
     # Convert a response from a categorical representation to a class label
     # Преобразуем ответ из категориального представления в метку класса
     prediction = numpy.argmax(prediction, axis=1)
     
     # Send the result further
     # Отправляем результат дальше
     return prediction