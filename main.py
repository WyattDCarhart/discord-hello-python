import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

command_prefix = "!"

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=command_prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# HELLO
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

# REMIND
@bot.command()
async def remind(ctx):
    ...

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
