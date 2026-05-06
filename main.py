import asyncio
import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from remind import Remind

async def main():
    # Load environment variables
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')

    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s:%(levelname)s:%(name)s: %(message)s",
        handlers=[logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")]
    )

    # Set up bot intents and command prefix
    command_prefix = "!"
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix=command_prefix, intents=intents)

    # Register events and commands
    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')

    # TEST
    @bot.command()
    async def test(ctx, *args):
        print('gonna do it')
        print('did it')

    # HELLO
    @bot.command()
    async def hello(ctx):
        await ctx.send(f'Hello {ctx.author.mention}!')

    # Add the cog asynchronously
    await bot.add_cog(Remind(bot))

    # Start the bot
    await bot.start(token)

# Run the asynchronous main function
asyncio.run(main())
