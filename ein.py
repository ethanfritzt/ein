import discord
from discord.ext import commands
import settings

intents = discord.Intents().all()
client = discord.Client(intents=intents)
ein = commands.Bot(command_prefix='ein: ', intents=intents)

### Commands ###

# Give basic server info
@ein.command()
async def info(ctx):
    infoEmbed = discord.Embed(
        title='**Info**',
        color=5592575,
        description="*ein: info*"
                    "\n`Gives a list of commands`"
                    "\n*ein: create <game> <private/public>*"
                    "\n`Creates a new channel`"
    )
    await ctx.send(embed=infoEmbed)

# Creates a channel for the specified game
# takes in the name
@ein.command()
async def create(ctx, game):
    await ctx.send("Creating channel for " + game + "...")
    cat = await ctx.guild.create_category(game)
    await ctx.guild.create_text_channel("Game Chat", category=cat)
    await ctx.guild.create_voice_channel("Voice Chat", category=cat)



# Fun command that lets ein talk
@ein.command()
async def talk(ctx):
    await ctx.send("Borf!")


### Functions ###
def get_channel(ctx, channelName):
    channel = discord.utils.get(ctx.guild.category, name=channelName) 
    return channel

ein.run(settings.TOKEN)