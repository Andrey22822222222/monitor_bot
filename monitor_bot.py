from telethon import TelegramClient, events
import asyncio
import os
import requests
from aiohttp import web

api_id = 26620563
api_hash = "6be823fef2b233d828259c332d09c9679"
channel_username = "hy_i_dnepr"
keywords = ["ракета на Дніпро", "Червоний", "негайно в укриття", "вибух"]

BOT_TOKEN = "8361339789:AAFAGs8zQ6OOa0LLW1pYJhBunvTvo_xAo"
CHAT_ID = 384327027

# === создаём клиента без авторизации ===
client = TelegramClient("bot", api_id, api_hash)

async def main():
    print("✅ Запуск бота...")
    await client.start(bot_token=BOT_TOKEN)
    print("✅ Авторизация прошла успешно!")

    @client.on(events.NewMessage(chats=channel_username))
    async def handler(event):
        text = event.message.message.lower()
        if any(keyword.lower() in text for keyword in keywords):
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            data = {"chat_id": CHAT_ID, "text": f"⚠️ Найдено сообщение:\n\n{event.message.message}"}
            requests.post(url, data=data)

    async def web_server():
    async def handle(request):
        return web.Response(text="✅ Бот работает 24/7 на Render.")
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.environ.get("PORT", 10000)))
    await site.start()

async def main():
    # здесь объединяем задачи
    await asyncio.gather(
        client.run_until_disconnected(),
        web_server()
    )

if __name__ == "__main__":
    asyncio.run(main())


