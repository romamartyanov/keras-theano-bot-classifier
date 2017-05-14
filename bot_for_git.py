# -*- coding: utf-8 -*-
"""
Created on Fri May 12 19:06:10 2017

@author: iromi
"""

import image_processing
import telebot


TOKEN = '...'

# Creating the bot
bot = telebot.TeleBot(TOKEN)

# Description of the command /start
@bot.message_handler(commands=["start"])
def welcome_Message(message):
     try:
          bot.send_message(message.chat.id, "Please, send the image with a number")
     except:
          bot.send_message(message.chat.id, "Something is going wrong. Please clear the conversation history with the bot.")

# Description of the command /help       
@bot.message_handler(commands=["help"])
def help_Message(message):
     try:
          bot.send_message(message.chat.id, """
The main function of the bot is the recognition of handwritten figures.
This bot uses the Theano library (v. 0.9.0) and Keras (v. 2.0.4) - the high-level library for Theano or TensorFlow, as a back-end of the bot.
For faster learning of the neural network were used such technologies and libraries to work with the GPU as:
- CUDA Toolkit
- NVIDIA CNMeM Library
- NVIDIA cuDNN

<code>Developed by Roman Martyanov</code> (@romamartyanov)
""", parse_mode="HTML")
     except:
          bot.send_message(message.chat.id, "Something is going wrong. Please clear the conversation history with the bot.")
    
# Response function to the input text    
@bot.message_handler(content_types=["text"])
def text_anwser(message):
     try:
          bot.send_message(message.chat.id, "Please, send the image with a number")
     except:
          bot.send_message(message.chat.id, "Something is going wrong. Please clear the conversation history with the bot.")
 


# Response function to the received image  
@bot.message_handler(func=lambda message: True, content_types=["photo"])
def photo_anwser(message):
     try:
          bot.send_message(message.chat.id, "Please, wait a second...")
          
          # Sending the received image to processing and prediction
          image_processing.process_PhotoMessage(bot, message)
          
          bot.send_message(message.chat.id, "Please, send the image with a number")
     except:
          bot.send_message(message.chat.id, "Something is going wrong. Please clear the conversation history with the bot.")


bot.polling(none_stop=True, interval=0)