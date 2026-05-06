from apscheduler.schedulers.background import BackgroundScheduler
import discord
from discord.ext import commands

class Remind(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    ############################################################################
    # REMIND
    ############################################################################

    @commands.group()
    async def remind(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f'You said: {ctx.message.content}')

    # EVERY
    @remind.command()
    async def every(self, ctx, *args):
        reminder = ' '.join(args)
        await ctx.send(f'Okay, I\'ll remind you EVERY {reminder}')
