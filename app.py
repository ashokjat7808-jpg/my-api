from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Game API running 🎮"

@app.route("/start/<user_id>")
def start(user_id):
    if user_id not in users:
        users[user_id] = {"coins": 100}
    return jsonify(users[user_id])

@app.route("/daily/<user_id>")
def daily(user_id):
    if user_id in users:
        users[user_id]["coins"] += 50
        return jsonify({"message": "Daily bonus added", "coins": users[user_id]["coins"]})
    return "User not found"

@app.route("/balance/<user_id>")
def balance(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    return "User not found"
