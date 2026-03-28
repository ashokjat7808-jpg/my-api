from flask import Flask, request, jsonify

app = Flask(__name__)

# --- अपनी RapidAPI Proxy Secret यहाँ डालें ---
MY_SECRET_KEY = "10458a00-2ac6-11f1-b7ee-5161c277cfaa"

users = {}

# सुरक्षा चेक करने वाला फंक्शन (ताकि बार-बार न लिखना पड़े)
def check_auth():
    user_secret = request.headers.get('X-RapidAPI-Proxy-Secret')
    return user_secret == MY_SECRET_KEY

@app.route("/")
def home():
    if not check_auth():
        return jsonify({"error": "Unauthorized Access! Please use RapidAPI."}), 401
    return "Game API running 🎮"

@app.route("/start/<user_id>")
def start(user_id):
    if not check_auth():
        return jsonify({"error": "Unauthorized Access"}), 401
    if user_id not in users:
        users[user_id] = {"coins": 100}
    return jsonify(users[user_id])

@app.route("/daily/<user_id>")
def daily(user_id):
    if not check_auth():
        return jsonify({"error": "Unauthorized Access"}), 401
    if user_id in users:
        users[user_id]["coins"] += 50
        return jsonify({
            "message": "Daily bonus added",
            "coins": users[user_id]["coins"]
        })
    return "User not found"

@app.route("/balance/<user_id>")
def balance(user_id):
    if not check_auth():
        return jsonify({"error": "Unauthorized Access"}), 401
    if user_id in users:
        return jsonify(users[user_id])
    return "User not found"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
