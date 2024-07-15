import discord
from discord import Intents
from flask import Flask, request
import threading
import asyncio


intents = discord.Intents.default()
intents.dm_messages = True
bot = discord.Bot(intents=intents)
CHANNEL_ID = "123456" # Channel to send the notification when the part gets touched


app = Flask(__name__)

@app.route('/notify')
def notify():
    channel = bot.get_channel(int(CHANNEL_ID))
    if channel:
        asyncio.run_coroutine_threadsafe(channel.send("message"), bot.loop)
    return 'Notification sent', 200

def run_flask():
    app.run(port=5000)

flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


bot.run("TOKEN")
