import discord
from discord.ext import commands
import music

cogs = [musica]

client = commands.Bot(command_prefix="!", 
intents = discord.Intents.all())


for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("OTEwNzIxNzkyOTA4MzQ5NDUw.YZW9ww.v0egzSzk1cknO_3IEZP3mp2eKic")