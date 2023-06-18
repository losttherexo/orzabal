import discord
import datetime
import asyncio
from secret import bot_secret

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await morning_message()

async def send_morning_message():
    channel_id = '748224867085582425'
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send("Good morning, everyone! Let's rule the fucking world")

async def morning_message():
    while True:
        now = datetime.datetime.now()
        target_time = datetime.time(hour=7, minute=45)  # Set the target time for the message
        target_datetime = datetime.datetime.combine(now.date(), target_time)

        if now.time() > target_time:
            target_datetime += datetime.timedelta(days=1)  # Add 1 day if the target time has already passed today

        delta = target_datetime - now
        seconds_until_target = delta.total_seconds()

        await asyncio.sleep(seconds_until_target)

        await send_morning_message()

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore messages sent by the bot itself

    if message.content == 'hello':
        await message.author.send('hello my friend!')


client.run(bot_secret)