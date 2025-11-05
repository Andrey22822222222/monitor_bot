import asyncio
import os
import requests
from telethon import TelegramClient, events
from aiohttp import web

# === ТВОИ ДАННЫЕ ===
api_id = 26620563  # твой API ID
api_hash = "6be823fef2b233d828259c332d09c9679"  # твой API hash
channel_username = "hy_i_dnepr"  # канал, который бот слушает
keywords = ["ракета на Дніпро", "прилёт", "Червоний", "негайно в укриття", "вибух"]  # ключевые слова

BOT_TOKEN = "8361339789:AAFAGs8zQ6OOa0LLW1pYJhBunvTvo_xAo"  # твой токен бота
CHAT_ID = 384327027  # твой Telegram ID

# === ИНИЦИАЛИЗАЦИЯ БОТА ===
client = TelegramClient('bot', api_id, api_hash).start(bot_token=BOT_TOKEN)

async def send_alert(message_text):
    """Отправка уведомления в Telegram"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": f"⚠️ Найдено сообщение с ключевым словом:\n\n{message_text}"}
    requests.post(url, data=data)

@client.on(events.NewMessage(chats=channel_username))
async def handler(event):
    """Обработка новых сообщений"""
    text = event.message.message.lower()
    if any(keyword.lower() in text for keyword in keywords):
        await send_alert(event.message.message)

# === ЗАПУСК TELETHON И ВЕБ-СЕРВЕРА ===
async def start_bot():
    print("✅ Бот запущен и слушает канал...")
    await client.start()
    await client.run_until_disconnected()

async def web_server():
    """Простой веб-сервер для Render (чтобы не завершал процесс)"""
    async def handle(request):
        return web.Response(text="✅ Бот работает 24/7 на Render.")
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.environ.get("PORT", 10000)))
    await site.start()

async def main():
    await asyncio.gather(start_bot(), web_server())

if __name__ == "__main__":
    asyncio.run(main())



