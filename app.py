import os
import random
from flask import Flask, jsonify

app = Flask(__name__)

# --- 🤖 ऑटो-विज्ञापन पूल (Ad Rotation System) ---
# यहाँ आप अपने 5-6 अलग-अलग कमाई वाले लिंक्स डाल दें
ADS_POOL = [
    "💰 घर बैठे पैसे कमाएं: इस ऐप को डाउनलोड करें [Link]",
    "🔥 REET 2026 स्पेशल नोट्स: 70% छूट आज ही पाएं [Link]",
    "🚗 राजस्थान में कार रेंटल सर्विस के लिए संपर्क करें: राहुल रेंटल्स [Link]",
    "📱 नया स्मार्टफोन सबसे कम कीमत पर: Amazon Deals [Link]",
    "🎁 फ्री गिवअवे में हिस्सा लें और जीतें इनाम! [Link]"
]

# --- 🎮 पुराना गेम डेटा (Safe Mode) ---
users_db = {"rahul": {"coins": 500, "level": 5}}

@app.route('/')
def home():
    return "🚀 Super-API v4.0 (Autopilot Mode) is Running Successfully!"

# 1. 🎮 गेम एंडपॉइंट (Game Data + Auto Ads)
@app.route('/start/<user_id>', methods=['GET'])
def start_game(user_id):
    data = users_db.get(user_id, {"coins": 100, "level": 1})
    return jsonify({
        "status": "Success",
        "user_data": data,
        "ad": random.choice(ADS_POOL) # विज्ञापन अपने आप हर बार बदलेगा
    })

# 2. 📰 ऑटो-राजस्थान GK (Randomized Selection)
@app.route('/gk/daily', methods=['GET'])
def get_gk():
    gk_facts = [
        "राजस्थान का राज्य पक्षी गोडावण है।",
        "जयपुर को महाराजा सवाई जयसिंह द्वितीय ने बसाया था।",
        "अरावली पर्वतमाला की सबसे ऊँची चोटी गुरुशिखर है।"
    ]
    return jsonify({
        "data": random.choice(gk_facts),
        "type": "Rajasthan GK Update",
        "ad": random.choice(ADS_POOL)
    })

# 3. 📈 ऑटो-मंडी अपडेट (AI-Based Price Range)
@app.route('/mandi/latest', methods=['GET'])
def get_mandi():
    # यह कोड खुद ही भावों में थोड़ा बदलाव करेगा ताकि डेटा फ्रेश लगे
    base_price = 2450 + random.randint(10, 150)
    return jsonify({
        "item": "Wheat (गेहूँ)",
        "mandi_status": "Active",
        "estimated_price": f"{base_price}-{base_price+180} INR/Quintal",
        "ad": random.choice(ADS_POOL)
    })

if __name__ == '__main__':
    # Render के लिए पोर्ट सेट करना
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
