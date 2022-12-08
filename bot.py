import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Your Bot Is Ready"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()
from datetime import datetime
import discord
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is active")

@client.event
async def on_message(message):
    # print(message)
    if message.author == client.user:
        return
    if message.author.bot:
        return
    if "Hello" in message.content:
        hellos = ["Sup Asshole", "I am Groot", ]
        await message.channel.send("Hello")
    elif "Time" in message.content:
        await message.channel.send(datetime.today().strftime("%I:%M:%S %p"))
    # await message.add_reaction('\N{THUMBS UP SIGN}')
    print(message)
key = os.environ['client']
client.run(key)