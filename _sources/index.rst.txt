.. Payment bot documentation master file, created by
   sphinx-quickstart on Sun Nov 17 13:51:12 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bot Overview and Functionality
==============================

This bot based on Flask and Telegram APIs to provide a range of functionalities including:
   - Handling user payments through Telegram and Stripe
   - Recording user information in a PostgreSQL database
   - Managing different interactive elements and responses for users

.. container:: image-right

   .. image:: payment-method.png
      :alt: pay
      :scale: 40%

Components and Workflow
-----------------------

1. **Importing Required Libraries**
   The bot script begins by importing necessary libraries:

   .. code-block:: python

      from flask import Flask, request
      import threading
      import requests
      import time as t
      import logging
      from telebot.types import LabeledPrice, InlineKeyboardButton, InlineKeyboardMarkup
      import telebot
      from telebot import types
      from telegram.error import BadRequest
      from flask_sqlalchemy import SQLAlchemy
      import os
      import ngrok

   Additionally, custom modules are imported for handling specific tasks, such as interacting with the database and loading configuration.

2. **Setting Up Database and Flask**
   The bot uses Flask as a web server and connects to a PostgreSQL database via SQLAlchemy:

   .. code-block:: python

      db = SQLAlchemy()
      app = Flask(__name__)
      app.config['SQLALCHEMY_DATABASE_URI'] = get_from_env('DATABASE_URL')
      db.init_app(app)

3. **Configuring ngrok for Local Testing**
   To expose the local server, ngrok is configured, with an authtoken fetched from environment variables:

   .. code-block:: python

      authtoken = get_from_env('ENV_NGROK_AUTHTOKEN')
      listener = ngrok.forward("localhost:5000", authtoken=authtoken)
      bot.set_webhook(url=f"{listener.url()}/{bot.token}")

4. **Creating the Bot and Webhook**
   Using `telebot`, a Telegram bot instance is created and connected to a webhook to receive updates:

   .. code-block:: python

      bot = telebot.TeleBot(get_from_env("TELEGRAM_BOT_TOKEN"))
      bot.set_webhook(url=f"{listener.url()}/{bot.token}")

5. **Setting Up Inline Keyboards**
   Several buttons are configured to be displayed as inline options:

   .. code-block:: python

      inline_keyboard = InlineKeyboardMarkup()
      pay_button = InlineKeyboardButton("Pay", pay=True, callback_data="pay")
      terms_button = InlineKeyboardButton("Terms", callback_data="terms")
      help_button = InlineKeyboardButton("Help", callback_data="help")
      inst_button = InlineKeyboardButton("Instructions", callback_data="instructions")
      keyboard_2 = InlineKeyboardMarkup([[pay_button], [terms_button], [help_button], [inst_button]])

6. **Defining Bot Commands and Handlers**
   Different bot commands handle user interactions, including:

   - **/start**: Greets the user and requests contact information.
   - **/contact**: Handles contact-sharing events and saves user data.
   - **/location**: Manages location-sharing events.
   - **callback_query_handler**: Responds to inline button actions, such as initiating payments or displaying terms.

   Sample command handler for `/start`:

   .. code-block:: python

      @bot.message_handler(commands=['start'])
      def command_start(message):
         keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
         button_phone = types.KeyboardButton(text="Share Number", request_contact=True)
         keyboard.add(button_phone)
         bot.send_message(message.chat.id, "Hello!", reply_markup=keyboard)

7. **Payment Processing and Invoice Generation**
   To handle payments, the bot uses `LabeledPrice` for the amount and generates invoices using the Telegram API:

   .. code-block:: python

      def send_invoice(chat_id, amount):
         title = "Product Title"
         description = "Product Description"
         payload = "invoice_payload"
         provider_token = get_from_env("PAYMENT_TOKEN")
         currency = 'USD'
         prices = [LabeledPrice("Product", amount)]
         bot.send_invoice(chat_id, title, description, payload, provider_token, currency, prices)

8. **Managing Pending Payments**
   A dictionary `pending_payments` tracks payments in process. A separate thread periodically checks for timeouts:

   .. code-block:: python

      def check_pending_payments():
         while True:
            for chat_id, timestamp in list(pending_payments.items()):
               if (timestamp + PAYMENT_TIMEOUT) < t.time():
                  del pending_payments[chat_id]
                  bot.send_message(chat_id, "Payment timed out. Please try again.")
            t.sleep(60)

9. **Running the Application**
   The Flask app and the `check_pending_payments` thread start together:

   .. code-block:: python

      if __name__ == '__main__':
         if listener:
            thread = threading.Thread(target=check_pending_payments)
            thread.start()
            app.run(host='localhost', port=5000)
         else:
            print("ngrok URL not found. Webhook not set.")




.. toctree::
   :maxdepth: 2

   readme

