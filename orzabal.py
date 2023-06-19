import os
import discord
import datetime
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

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
    
    await morning_message()

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hello {member.name}, welcome to the lab!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        await message.channel.send("Hello! I'm a Discord bot.")

    await bot.process_commands(message)

async def send_morning_message():
    channel_id = 748224867085582425
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send("Good morning, everyone! Let's rule the fucking world")

async def morning_message():
    while True:
        now = datetime.datetime.now()
        target_time = datetime.time(hour=9, minute=00)
        target_datetime = datetime.datetime.combine(now.date(), target_time)

        if now.time() > target_time:
            target_datetime += datetime.timedelta(days=1)

        delta = target_datetime - now
        seconds_until_target = delta.total_seconds()

        await asyncio.sleep(seconds_until_target)

        await send_morning_message()

bot.run(TOKEN)
