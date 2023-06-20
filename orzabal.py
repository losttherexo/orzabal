import os
import discord
import datetime
import pytz
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
        await message.channel.send("i am but a mere child and i need some time to grow yet the vibes i will provide.")

    await bot.process_commands(message)

@tasks.loop(minutes=15)
async def send_daily_messages():
    est = pytz.timezone('US/Eastern') 
    now = datetime.datetime.now(est)
    
    morning_time = datetime.time(7, 45, 0)
    night_time = datetime.time(22, 45, 0)

    print(now)

    if now.hour == morning_time.hour and now.minute == morning_time.minute:
        channel = bot.get_channel(748224867085582425)
        await channel.send("good morrow brethren")

    if now.hour == night_time.hour and now.minute == night_time.minute:
        channel = bot.get_channel(748224867085582425)
        await channel.send("don't forget to drink water before bed tonight <3")

bot.run(TOKEN)
