How to Install Bot
===================

Follow these steps to set up and run the bot:

1. **Create Bot and Obtain Telegram Token**
   Go to BotFather on Telegram, create a new bot, and get the bot token.

2. **Set Up Payment and Get Stripe Token**
   Go to your Telegram bot, enable payment processing, and obtain the Stripe token.

3. **Get Your Telegram User ID**
   Go to Telegram Web, find your user ID, and note it down.

4. **Obtain Ngrok AUTHTOKEN for Flask**
   Go to Ngrok, sign up (if necessary), and get your AUTHTOKEN to use with Flask.

5. **Create PostgreSQL Database**
   Set up a PostgreSQL database for the bot's data storage.

6. **Clone the Repository**
   .. code-block:: bash

      git clone <your-repo-url>

7. **Navigate to Project Directory**
   .. code-block:: bash

      cd bot_flask_stripe

8. **Create a `.env` File**
   In the project root directory, create a `.env` file with the following content:

   .. code-block::

      TELEGRAM_BOT_TOKEN=YOUR_TOKEN
      PAYMENT_TOKEN=YOUR_TOKEN
      ADMIN_ID=YOUR_ID
      HOST=127.0.0.1
      USER=postgres
      PASSWORD=password
      DB_NAME=name
      DATABASE_URL=postgresql://postgres:password@localhost:5432/name
      ENV_NGROK_AUTHTOKEN=YOUR_TOKEN

   Replace `YOUR_TOKEN`, `YOUR_ID`, `password`, and `name` with your actual values.

9. **Build the Docker Image**
   Run the following command to build the Docker image:

   .. code-block:: bash

      sudo docker build -t flask_pay .

10. **Run the Bot**
    Start the bot using Docker Compose:

    .. code-block:: bash

       sudo docker-compose up -d

Your bot should now be running! Check the logs or bot responses for confirmation.
