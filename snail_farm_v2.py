import discord
import asyncio
import time
from random import randint

client = discord.Client()
enter = True

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------------------------')

@client.event
async def on_message(message):
    if message.content.startswith(':race_car: A snail race has begun!'):
        sleeper = randint(1, 5)
        time.sleep(sleeper)
        again = await client.send_message(message.channel, '!snail enter')
    if message.content.startswith("The race has ended! The winner: nobody#9250! Here's your prize: :love_letter:"):
        prize = await client.send_message(message.channel, '!snail open')

email = input("Email: ")
password = input("Password: ")

print("Authenticating...")

client.run(email, password)
