import os
import discord
import datetime
from dotenv import load_dotenv
from discord.ext import commands,tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

utc = datetime.timezone.utc
times = [
    datetime.time(hour=11, minute=45, tzinfo=utc),
    datetime.time(hour=3, minute=15, tzinfo=utc)
]

morning_time = datetime.time(11, 45, 0)
night_time = datetime.time(3, 15, 0)

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f'{bot.user} has entered {guild.name}. You may now commence the mayhem.')
    send_daily_messages.start()

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hello {member.name}, welcome to the lab!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        await message.channel.send("I am but a mere child and I need some time to grow yet the vibes I will provide.")

    await bot.process_commands(message)

@tasks.loop(time=times)
async def send_daily_messages():
    now = datetime.datetime.now().time()
    print(f"Current time: {now}")

    if now == morning_time:
        channel = bot.get_channel(748224867085582425)
        await channel.send("Good morning yall!")

    if now == night_time:
        channel = bot.get_channel(748224867085582425)
        await channel.send("Don't forget to drink water before bed tonight <3")


bot.run(TOKEN)
