from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8789588958:AAFmBXyEgd4zlAjDrjhD8zLS7qqhFzyYAGA"

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        reply = "आपने भेजा: " + text

        send_url = "https://api.telegram.org/bot" + TOKEN + "/sendMessage"

        requests.post(send_url, json={
            "chat_id": chat_id,
            "text": reply
        })

    return "ok"
