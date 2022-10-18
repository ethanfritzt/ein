import discord
from discord.ext import commands
import settings

intents = discord.Intents().all()
client = discord.Client(intents=intents)
ein = commands.Bot(command_prefix='ein: ', intents=intents)

# Give basic server info
@ein.command()
async def info(ctx):
    await ctx.send(ctx.message.guild.name)

ein.run(settings.TOKEN)