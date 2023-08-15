import datetime as dt
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

env_file_path = "../.env"
load_dotenv(dotenv_path=env_file_path)
OWNERS_DISCORD_USERNAME = os.getenv("OWNERS_DISCORD_USERNAME")
PREFIX = os.getenv("PREFIX")


async def setup(client):
    await client.add_cog(database(client))


class database(commands.Cog):

    uptime = str(dt.datetime.now().strftime("%H:%M, %B %d, %Y"))

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def status(self, ctx):

        client = self.client

        # number_of_servers------------------------------------------------

        for i in range(len(client.guilds)):
            number_of_servers = i + 1

        number_of_servers = str(number_of_servers)

        # ------------------------------------------------------------------

        ping = int(client.latency*1000)

        # ------------------------------------------------------------------

        CLIENT_NAME = client.user.name

        # ------------------------------------------------------------------

        infoEmbed = discord.Embed(

            title=f"{CLIENT_NAME} | status info",
            description=f"Following information represents {CLIENT_NAME} status:",
            colour=discord.Colour.from_rgb(0, 255, 255)

        )

        infoEmbed.add_field(name='Ping:', value=(
            '(' + str(ping) + ') ms'), inline=False)
        infoEmbed.add_field(name='Up time:', value=(
            'Online Since (' + database.uptime + ')'), inline=False)

        infoEmbed.add_field(name='Number of servers:', value='In (' +
                            number_of_servers + ') servers', inline=False)

        infoEmbed.add_field(name='Command prefix:',
                            value=f"{PREFIX}", inline=False)

        infoEmbed.set_footer(text=f'Contact owner : {OWNERS_DISCORD_USERNAME}')

        await ctx.send(embed=infoEmbed)

    @commands.command()
    async def commandslist(self, ctx):

        infoEmbed = discord.Embed(

            title=f"List of commands",
            description=f"List of default commands:",
            colour=discord.Colour.from_rgb(0, 255, 255)

        )

        infoEmbed.add_field(name=f'{PREFIX}play [track name]', value=(
            "Plays the requested track"), inline=False)

        infoEmbed.add_field(name=f'{PREFIX}join', value=(
            "Causes the bot to connect to your channel"), inline=False)

        infoEmbed.add_field(name=f'{PREFIX}leave', value=(
            "Causes the bot to leave your channel"), inline=False)

        infoEmbed.add_field(name=f'{PREFIX}pause', value=(
            "Pauses the current track"), inline=False)

        infoEmbed.add_field(name=f'{PREFIX}resume', value=(
            "Resumes the current track"), inline=False)

        infoEmbed.add_field(name=f'{PREFIX}skip', value=(
            "Skips the current track"), inline=False)

        infoEmbed.add_field(name=f'{PREFIX}loop', value=(
            "Loops the current track"), inline=False)

        infoEmbed.add_field(name=f'{PREFIX}queuelist', value=(
            "Displays a list of the queued tracks"), inline=False)

        infoEmbed.add_field(name=f'{PREFIX}queuerem [track index]', value=(
            "Removes the corresponding track from queue"), inline=False)

        infoEmbed.set_footer(text=f'Contact owner : {OWNERS_DISCORD_USERNAME}')

        await ctx.send(embed=infoEmbed)
