import asyncio
from telethon import TelegramClient, events
import requests

# === ТВОИ ДАННЫЕ ===
api_id = 26625063          # без кавычек, например 1234567
api_hash = "6be823ff7fb233d828259c3320b9c679"       # в кавычках
channel_username = "ny_i_dnipro" # канал, за которым следим
keywords = ["Балістика", "Балістика на Дніпро", "ППО", "вибух", "ракета", "тривога"]

BOT_TOKEN = "8361339789:AAF4GS8zQ60OOaDlW1PyJnHBunvIwfo_xAo"  # вставь токен, как в тесте
CHAT_ID = 384327027               # твой Telegram ID

# === КОД ===
client = TelegramClient("monitor_session", api_id, api_hash)

async def send_alert(message_text):
    """Отправляет уведомление в Telegram"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": f"⚠️ Найдено ключевое слово!\n\n{message_text}"}
    requests.post(url, data=data)

@client.on(events.NewMessage(chats=channel_username))
async def handler(event):
    text = event.message.message
    if any(word.lower() in text.lower() for word in keywords):
        print(f"🚨 Обнаружено ключевое слово в сообщении: {text}")
        await send_alert(text)

async def main():
    print("✅ Бот запущен и слушает канал...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
