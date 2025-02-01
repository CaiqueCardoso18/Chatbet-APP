from flask import Flask, request
import os
import telegram

app = Flask(__name__)

# Pegando o token do Telegram das variáveis de ambiente
TOKEN = os.getenv("TOKEN")
bot = telegram.Bot(token=TOKEN)

@app.route("/webhook", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    # Responde à mensagem
    bot.send_message(chat_id=chat_id, text=f"Você disse: {text}")

    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
