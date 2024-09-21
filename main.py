from dotenv import load_dotenv
from os import environ
from discord.ext import commands
from discord import Intents

load_dotenv()
bot = commands.Bot(command_prefix="!", intents=Intents.all())


@bot.command()
async def ping(ctx: commands.Context):
    await ctx.reply("Pong!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print("Slash commands synced!")


bot.run(environ.get("DISCORD_TOKEN"))
