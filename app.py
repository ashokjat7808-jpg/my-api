import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread

# --- बॉट को जगाए रखने के लिए छोटा सा वेब सर्वर ---
app = Flask('')
@app.route('/')
def home(): return "Bot is Online!"
def run(): app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
def keep_alive():
    t = Thread(target=run)
    t.start()

# --- मुख्य जानकारी (यहीं पेस्ट करें) ---
API_TOKEN = '8789588958:AAFmBXyEgd4zlAjDrjhD8zLS7qqhFzyYAGA' # <--- BotFather वाला टोकन
CARD_LINK = 'यहाँ_अपना_क्रेडिट_कार्ड_लिंक_डालें' # <--- अर्निंग लिंक

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("💳 क्रेडिट कार्ड (कमाई)", url=CARD_LINK),
        InlineKeyboardButton("🏛️ सरकारी योजनाएं", callback_data="yojana"),
        InlineKeyboardButton("📚 NCERT समाधान", callback_data="edu"),
        InlineKeyboardButton("🏰 राजस्थान GK", callback_data="gk")
    )
    await message.answer("🔥 स्वागत है! क्या सहायता करूँ?", reply_markup=kb)

@dp.callback_query_handler(lambda c: True)
async def process(call: types.CallbackQuery):
    if call.data == "yojana":
        await bot.send_message(call.from_user.id, "🚩 राजस्थान योजनाएं: चिरंजीवी, अन्नपूर्णा, फ्री स्मार्टफोन।")
    elif call.data == "edu":
        await bot.send_message(call.from_user.id, "📖 क्लास 6-12 के सभी नोट्स यहाँ मिलेंगे।")
    elif call.data == "gk":
        await bot.send_message(call.from_user.id, "🏰 राजस्थान का इतिहास और मंडी भाव अपडेट।")
    await call.answer()

if __name__ == '__main__':
    keep_alive()
    executor.start_polling(dp, skip_updates=True)
