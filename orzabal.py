import os
import discord
import datetime
import pytz
import random
from dotenv import load_dotenv
from discord.ext import commands,tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f'{bot.user} has entered {guild.name}. You may now commence the mayhem.')
    send_daily_messages.start()

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'hello {member.name}, welcome to the lab!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        await message.channel.send("i am but a mere child and i need some time to grow. yet, the vibes i will provide.")

    await bot.process_commands(message)

@tasks.loop(minutes=15)
async def send_daily_messages():
    est = pytz.timezone('US/Eastern') 
    now = datetime.datetime.now(est)
    
    morning_time = datetime.time(7, 45, 0)
    night_time = datetime.time(22, 45, 0)

    if now.hour == morning_time.hour and now.minute == morning_time.minute:
        channel = bot.get_channel(748224867085582425)
        morning_message = get_random_message_from_file('messages/morning_message.txt')
        await channel.send(morning_message)


    if now.hour == night_time.hour and now.minute == night_time.minute:
        channel = bot.get_channel(748224867085582425)
        night_message = get_random_message_from_file('messages/night_message.txt')
        await channel.send(night_message)

def get_random_message_from_file(file_path):
    with open(file_path, 'r') as file:
        messages = file.readlines()
    return random.choice(messages).strip()

bot.run(TOKEN)
