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

# On Message
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith(command_prefix):
        contents = message.content[len(command_prefix):].split()
        command = contents[0]
        args = contents[1:]

        # !hello
        if command == 'hello':
            await message.channel.send('Hello!')

        # default
        else:
            await message.channel.send(f'The command \'{command}\' is not recognized.')

    await bot.process_commands(message)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
