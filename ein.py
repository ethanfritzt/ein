import discord
from discord.ext import commands

intents = discord.Intents().all()
client = discord.Client(intents=intents)
ein = commands.Bot(command_prefix='ein: ', intents=intents)

# Give basic server info
@ein.command()
async def info(ctx):
    await ctx.send(ctx.message.guild.name)

ein.run('MTAzMTc2MTU3OTkzNjU4MzY4MA.GMES3X.iqq5GjElzzhbB_NHwvHccg2MJKSQ8ap_vv96eo')