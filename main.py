from dotenv import load_dotenv
from os import environ
from discord.ext import commands
from discord import Interaction

load_dotenv()
bot = commands.Bot(command_prefix="!")


@bot.tree.command()
async def ping(ctx: Interaction):
    await ctx.response.send_message("pong!")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    await bot.tree.sync()
    print("Slash commands synced!")


bot.run(environ.get("DISCORD_TOKEN"))
