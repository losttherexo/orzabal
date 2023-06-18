import discord
from discord.ext import commands
import asyncio
from secret import bot_secret

orzabal = commands.Bot(command_prefix='!')

@orzabal.event
async def on_ready():
    print(f'Orzabal is ready! Logged in as {orzabal.user.name}')

orzabal.run(bot_secret)

