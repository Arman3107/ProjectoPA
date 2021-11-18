import discord
from discord.ext import commands
import Musica

cogs = [Musica]

client = commands.Bot(command_prefix="!", 
intents = discord.Intents.all())


for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("OTEwNzIxNzkyOTA4MzQ5NDUw.YZW9ww.N9WD1XU-hWBY0Gip-KdVmveyioM")