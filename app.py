from flask import Flask, request
import requests

app = Flask(__name__)

# 👉 यहाँ अपना token डालना है
TOKEN = "8789588958:AAFmBXyEgd4zlAjDrjhD8zLS7qqhFzyYAGA"


@app.route("/")
def home():
    return "Bot is running!"


@app.route("/telegram", methods=["POST"])
def telegram():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]

        reply = f"""🔥 Welcome!

आपका मैसेज: {text}

💰 आज का ऑफर:
₹999 का product सिर्फ ₹299

👉 Buy Now:
https://amzn.to/yourlink
"""

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        requests.post(url, json={
            "chat_id": chat_id,
            "text": reply
        })

    return "ok"
