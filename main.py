from gevent import monkey
monkey.patch_all()

import os
from coursesniper import getclass
import discord
from alive import keep_alive
import random
from datetime import datetime
from pytz import timezone
from anagrams import anagrams

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
  # print("Bot is active")
  await client.get_channel(1049478814301945887).send("Bot is active")


@client.event
async def on_message(message):
  # print(message)
  if message.author == client.user:
    return
  if message.author.bot:
    return
  if "Hello" in message.content:
    await message.channel.send("Hello")
  if "Joke" in message.content:
    jokes = open('jokes.txt').read().splitlines()
    await message.channel.send(random.choice(jokes).replace("<>", "\n"))
  if "Word" in message.content:
    await message.channel.send(
      anagrams(message.content[message.content.find(" ") + 1:]))
  if "Time" in message.content:
    tz = timezone('EST')
    await message.channel.send(datetime.now(tz).strftime("%I:%M:%S %p"))
  elif message.content.isnumeric() and len(message.content) != 5:
    await message.channel.send("Invalid course ID")
  elif message.content.isnumeric() and len(message.content) == 5:
    print("MESSAGE")
    send = getclass(message.content)
    await message.channel.send(send)
    # if send == "Got class":
    #   await message.add_reaction('🎉')




#     # print(message.content.isnumeric())

keep_alive()
key = os.environ['client']
client.run(key)
