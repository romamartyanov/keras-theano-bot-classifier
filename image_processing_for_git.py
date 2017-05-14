# -*- coding: utf-8 -*-
"""
Created on Sun May 14 00:55:04 2017

@author: iromi
"""

import uuid
import urllib.request
import predicting
import os

from PIL import Image

TOKEN = '...'

# Resizing of the received picture
def resize(image_name):
     img = Image.open(image_name)
     
     # Changing the size of the image according to the specified parameters 'width' and 'height'
     width = 28
     height = 28
     resized_img = img.resize((width, height), Image.ANTIALIAS)
     
     resized_img.save(image_name)
     
# Deleting the image
def delete_image(image_name):
     os.remove(image_name)

# Downloading the received image from Telegram's servers 
def download_image(path, unique_filename):
     urllib.request.urlretrieve("https://api.telegram.org/file/bot{0}/{1}".format(
              TOKEN,
              path), "images/{0}.{1}".format(
                        unique_filename,
                        "png"))
     
     image_name = "images/{0}.{1}".format(
                        unique_filename,
                        "png")
     
     return image_name
     
     

def process_PhotoMessage(bot, message):    
     # Getting the file ID    
     fileID = message.photo[-1].file_id
                           
     # Getting the file by file ID
     file = bot.get_file(fileID)
     
     # Getting the path of the received image 
     path = file.file_path

     # Making the unique filename for this image     
     unique_filename = uuid.uuid4()
     
     # Downloading the received image by path 
     image_name = download_image(path, unique_filename)
     
     resize(image_name)
     
     # Predicting what the figure is it
     number = predicting.predicting(image_name)
     
     bot.send_message(message.chat.id, "The estimated number: {0}".format(
               number))
     
     # Deleting the received image 
     delete_image(image_name)    