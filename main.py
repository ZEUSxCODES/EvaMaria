from flask import Flask
from bot import Bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

if __name__ == "__main__":
    bot = Bot()
    bot.run()  # Assuming this doesn't block
    app.run(host='0.0.0.0', port=8080)  # Bind to port 5000
