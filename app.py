import telebot
import requests
import random

# 1. अपना असली टोकन यहाँ डालें
TOKEN = "8789588958:AAFmBXyEgd4zlAjDrjhD8zLS7qqhFzyYAGA" 
bot = telebot.TeleBot(TOKEN)

# विज्ञापनों का पूल
ADS = [
    {"b": "Khan Sir / PW", "img": "https://img.freepik.com/free-vector/online-education-concept_23-2148496154.jpg", "l": "https://pw.live", "t": "📖 खान सर और PW के नए बैच पर 50% छूट!"},
    {"b": "Ankit Awasthi Sir", "img": "https://img.freepik.com/free-vector/world-news-concept-illustration_114360-1011.jpg", "l": "https://www.youtube.com/@AnkitInspiresIndia", "t": "🌍 दुनिया की बड़ी खबरें अंकित सर के साथ समझें!"}
]

@bot.message_handler(commands=['start', 'gk', 'news', 'market'])
def handle_commands(message):
    try:
        # रैंडम विज्ञापन दिखाना
        ad = random.choice(ADS)
        bot.send_photo(message.chat.id, ad['img'], 
                       caption=f"🌟 *Featured by {ad['b']}*\n{ad['t']}\n👉 [अभी देखें]({ad['l']})", 
                       parse_mode="Markdown")
        
        if 'start' in message.text:
            bot.send_message(message.chat.id, "नमस्ते! आपका 24/7 बॉट लाइव है। सर्च करें: /gk, /news, /market")
        elif 'gk' in message.text:
            bot.send_message(message.chat.id, "📚 *राजस्थान GK*: आज का अपडेट यहाँ है।")
    except Exception as e:
        print(f"Error: {e}")

# Render पर 24/7 चलाने के लिए यह लाइन सबसे जरूरी है
if __name__ == "__main__":
    print("Bot is starting 24/7...")
    bot.infinity_polling()
