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
    print('--------------------')

@client.event
async def on_message(message):
    if message.content.startswith('The race has ended!'):
        wait()
        again = await client.send_message(message.channel, '!snail start')
    if message.content.startswith('Fiddle sticks! The bot won the race.'):
        wait()
        again = await client.send_message(message.channel, '!snail start')
    if message.content.startswith("The race has ended! The winner: the_nightman#3860! Here's your prize:"):
        prize = await client.send_message(message.channel, '!snail open')

def wait():
    sleeper = randint(1, 5)
    time.sleep(sleeper)

email = input("Email: ")
password = input("Password: ")

print("Authenticating...")

client.run(email, password)
