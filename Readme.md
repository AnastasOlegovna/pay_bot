18.06.2024-run in dockerfile
How use:
1. Create bot and get telegram token from BotFather
2. Go to telegram bot, add payment and get Stripe token 
3. Go to telegram web, write your id user
4. Go to Ngrok, get AUTHTOKEN for Flask 
5. Create your database postgres
6. Clone repo
7. cd bot_flask_stripe
8. Create .env file
9. Write inside

```env
TELEGRAM_BOT_TOKEN=YOUR_TOKEN
PAYMENT_TOKEN=YOUR_TOKEN
ADMIN_ID=YOUR_ID
HOST=127.0.0.1
USER=postgres
PASSWORD=password
DB_NAME=name
DATABASE_URL=postgresql://postgres:password@localhost:5432/name
ENV_NGROK_AUTHTOKEN=YOUR_TOKEN
```

10. start build image

```
 sudo docker build -t flask_pay .
```

11. run bot

```
sudo docker-compose up -d
```