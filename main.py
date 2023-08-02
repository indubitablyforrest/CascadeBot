from dotenv import load_dotenv
import os

load_dotenv() # take environment variables from .env

import discord
from discord.ext import commands
import cascadefun


def run():
    print('starting to Cycle')
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
        print("______________")

    @bot.command(
        aliases=['test', 't'],
        help="shows help",
        description="describing that this is a test command",
        brief="describe this a test cmd w/ fewer word",
        enabled=True,  # does it work
        Hidden=False,  # if set to true, doesn't show in help list
    )
    async def trial1(ctx):
        await ctx.send("test1")

    @bot.command(
        help="you should know how to cascade",
        description=" ",
        brief="what will you reveal?",
        enabled=True,
        Hidden=False,
    )
    async def cascade(ctx):
        await ctx.send(cascadefun.cascade_resolved())

    @bot.command(
        description="only available if your a mod",
        breif="mods only"
    )
    @commands.has_role("Moderators")
    async def m(ctx):
        await ctx.send("you are a mod!")

    bot.run(os.getenv("API_Key"))  # add token here

if __name__ == '__main__':
    # run the bot

    run()