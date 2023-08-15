import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.all()
intents.members = True
PREFIX = os.getenv("PREFIX")
client = commands.Bot(command_prefix=PREFIX or "&", intents=intents)


@client.event
async def on_ready():

    await client.change_presence(status=discord.Status.online, activity=discord.Game("Music"))

    await client.load_extension('modules.database')
    await client.load_extension('modules.music')

    os.system('cls' if os.name == 'nt' else 'clear')
    print('Successfully logged in \n----------------------\n')

TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
