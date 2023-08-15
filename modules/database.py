import sqlite3
import datetime as dt
import discord
from discord.ext import commands


async def setup(client):
    await client.add_cog(database(client))


class database(commands.Cog):

    connection = sqlite3.connect('database.db')
    do = connection.cursor()

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

        infoEmbed = discord.Embed(

            title="PSB bot | status info",
            description='Following information represents PSBs status:',
            colour=discord.Colour.from_rgb(0, 255, 255)

        )

        infoEmbed.add_field(name='Up time:', value=(
            'Online Since (' + database.uptime + ')'), inline=False)
        infoEmbed.add_field(
            name='Birth day:', value='PSB was born on (11th November 2021)', inline=False)

        infoEmbed.add_field(name='Number of servers:', value='🔴 in (' +
                            number_of_servers + ') servers', inline=True)

        infoEmbed.add_field(name='Bots ping:', value=(
            '🔴 (' + str(ping) + ') ms'), inline=True)
        infoEmbed.add_field(name='Bots prefix:',
                            value='Using "&"', inline=True)

        infoEmbed.add_field(name='Location:', value=':flag_se: Sweden')
        infoEmbed.add_field(name='Version:', value='📱 Version 3.1')

        infoEmbed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/678610661986664459/931933901092438086/Tumbnail.png')
        infoEmbed.set_footer(text='Contact owner : Ψ |¦ PSI ¦| Ψ  # 2653')

        await ctx.send(embed=infoEmbed)
