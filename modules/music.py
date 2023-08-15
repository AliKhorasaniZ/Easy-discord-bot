import discord
import discord.embeds
from discord.ext import commands
import yt_dlp as youtube_dl
import urllib.request
import re
import asyncio

from modules.logger import log


async def setup(client):
    await client.add_cog(music(client))


class Track:
    def __init__(self, url, title):
        self.url = url
        self.age = title


class music(commands.Cog):

    loopMode = False
    queueList = []
    currentTrack = Track(None, None)

    def __init__(self, client):
        self.client = client

    # play------------------------------------------

    @commands.command()
    async def play(self, ctx, *trackName):

        # error_check--------------------------------

        if ctx.author.voice is None:
            return

        if ctx.voice_client is None and ctx.author.voice is not None:
            channel = ctx.author.voice.channel
            await channel.connect()
            try:
                log(f"Connection established at {ctx.guild.name} by {ctx.author.name}")
            except:
                pass
       # youtube_search_function----------------------

        query = "https://www.youtube.com/results?search_query="

        for word in trackName:
            query = (query + word + "+")

        html = urllib.request.urlopen(query)

        if query.startswith("https://soundcloud.com/"):
            url = (query)
        else:
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            url = ("https://www.youtube.com/watch?v=" + video_ids[0])

        # queue_check--------------------------------

        if ctx.voice_client.is_playing():
            music.queueList.append(url)
            header = "Song added to queue!"

        # youtube_play_function----------------------

        if ctx.voice_client.is_playing() is False:
            await music.playFunction(ctx, url)
            header = "Now playing the requested song!"

        await ctx.send(embed=music.trackEmbed(header, url, ctx.author.name))

    # join------------------------------------------

    @commands.command()
    async def join(self, ctx):

        try:
            authorChannel = ctx.author.voice.channel
            if ctx.voice_client.channel != authorChannel:
                await ctx.voice_client.move_to(authorChannel)
            else:
                await authorChannel.connect()
        except:
            return

    # leave-----------------------------------------

    @commands.command()
    async def leave(self, ctx):

        try:
            await ctx.voice_client.disconnect()
            log(f"Connection terminated at {ctx.guild.name} by {ctx.author.name}")
        except:
            return

    # pause-----------------------------------------

    @commands.command()
    async def pause(self, ctx):

        try:
            await ctx.send("Song paused!")
            ctx.voice_client.pause()
        except:
            return

    # resume----------------------------------------

    @commands.command()
    async def resume(self, ctx):

        try:
            await ctx.send("Song resumed!")
            ctx.voice_client.resume()
        except:
            return

    # skip------------------------------------------

    @commands.command()
    async def skip(self, ctx):

        try:
            music.loopMode = False
            ctx.voice_client.stop()
            try:
                message = ("Skipping **" + music.currentTrack.title + "**...")
            except:
                message = "Skipping the current song..."
            await ctx.send(message)
        except:
            await ctx.send("Something went wrong!")

    # loop------------------------------------------

    @commands.command()
    async def loop(self, ctx):

        try:
            music.loopMode = not music.loopMode
            if music.loopMode == True:
                try:
                    message = ("Looping **" +
                               music.currentTrack.title + "**...")
                except:
                    message = "Looping the curront song..."
            else:
                message = "Loop mode **Turned Off**..."
            await ctx.send(message)
        except:
            await ctx.send("Something went wrong!")

    # queue--------------------------------------------------------------------------

    async def queueFunction(ctx):

        if music.loopMode == True:

            url = music.currentTrack.url
            await music.playFunction(ctx, url)

        else:
            if music.queueList != []:

                url = music.queueList.pop(0)
                await music.playFunction(ctx, url)

            else:
                return

    @commands.command()
    async def queuelist(self, ctx):

        queueEmbedList = []

        try:

            for i in range(len(music.queueList)):
                queueEmbedList.append(music.queueList[i])

            queueShow = discord.Embed(

                title="Your queue list :",
                description='Following information:',
                colour=discord.Colour.from_rgb(0, 255, 255)
            )

            for i in range(len(queueEmbedList)):

                var1 = urllib.request.urlopen('https://www.youtube.com')
                var1 = urllib.request.urlopen(queueEmbedList[i])
                var2 = re.findall(
                    'title":{"simpleText":"(.+?(?="},))', var1.read().decode())
                var2 = str(var2.pop(0))

                queueShow.add_field(
                    name=f'{i+1}' + ' : ' + var2, value=queueEmbedList[i] + '\n-------------------------------------------------------', inline=False)

            queueShow.set_footer(
                text='Use &queuerem [queue index] to remove a queue item !')

            await ctx.send(embed=queueShow)

        except:
            await ctx.send("Something went wrong!")

    @commands.command()
    async def queuerem(self, ctx, queueIndex):

        try:
            queueIndex = int(queueIndex)
            del music.queueList[queueIndex-1]
            queueIndex = str(queueIndex)
            await ctx.send("Removed song number **" + queueIndex + "** from queue !")
        except:
            await ctx.send("Something went wrong!")

    # embed----------------------------------------

    def trackEmbed(header, url, author):

        YDL_OPTIONS = {'format': "bestaudio", "quiet": True}

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)

        minutes = int(info.get('duration', None)) // 60
        remaining_seconds = int(info.get('duration', None)) % 60
        duration = f"{minutes} Mins {remaining_seconds} Secs"

        title = info.get('title', None)
        thumbnail = info.get('thumbnail', None)

        platform = 'unrecognized'
        if url.startswith("https://www.youtube.com"):
            platform = 'Youtube'
        if url.startswith("https://soundcloud.com/"):
            platform = 'Sound Cloud'

        trackEmbed = discord.Embed(

            title=header,
            description='Following infromation:',
            colour=discord.Colour.from_rgb(0, 255, 255)
        )

        trackEmbed.add_field(name="Music name: ", value=title, inline=False)
        trackEmbed.add_field(name="Song duration: ",
                             value=duration, inline=False)
        trackEmbed.add_field(name="Requested by: ",
                             value=author, inline=True)
        trackEmbed.add_field(name='Used Platform :',
                             value=platform, inline=True)
        trackEmbed.add_field(name='Video link :', value=url, inline=False)
        trackEmbed.set_image(url=thumbnail)

        return trackEmbed

    # main_functions-------------------------------

    async def playFunction(ctx, url):

        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format': "bestaudio", "quiet": True}

        try:
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                ##############################################
                formats = info.get('formats', [info])
                audio_formats = [
                    f for f in formats if f.get('acodec') != 'none']
                audio_url = audio_formats[0]['url'] if audio_formats else None
                ##############################################
                source = await discord.FFmpegOpusAudio.from_probe(audio_url, **FFMPEG_OPTIONS)
                ctx.voice_client.play(
                    source, after=lambda _: asyncio.run(music.queueFunction(ctx)))
        except:
            return

        title = info.get('title', None)
        music.setInfo(title, url)

    def setInfo(title, url):

        music.currentTrack.title = title
        music.currentTrack.url = url
