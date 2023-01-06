import discord
from discord.ext import commands
from discord.utils import get
import settings
import webcolors

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
        description="``ein: info``"
                    "\n*Gives a list of commands*"
                    "\n``ein: create <game> <private/public>``"
                    "\n*Creates a new category*"
    )
    await ctx.send(embed=infoEmbed)

# Creates a channel for the specified game
# takes in the name
@ein.command()
async def create(ctx, game):
    await ctx.send("Creating channel for " + game + "...")
    cat = await ctx.guild.create_category(game)
    await ctx.guild.create_text_channel("General Chat", category=cat)
    await ctx.guild.create_voice_channel("Voice Chat", category=cat)

# Creates a new role
# takes in name, and color name as a string
# converts string color name to its corresponding hex value
@ein.command()
async def createRole(ctx, roleName, colour="grey"):
    hexValue = nameToHex(colour)
    await ctx.guild.create_role(name=roleName, colour=hexValue)

# Assigns a role to a user
# takes in role name and user name
# create role if it doesn't exist
@ein.command()
async def assignRole(ctx, roleName, user: discord.Member, colour="grey"):
    role = get(user.guild.roles, name=roleName)
    if (role):
        await user.add_roles(role)
    else:
        await createRole(ctx, roleName, colour)
        role = get(user.guild.roles, name=roleName)
        await user.add_roles(role)
    

@ein.command()
async def purge(ctx, limit):
    await ctx.channel.purge(limit=int(limit))

# Fun command that lets ein talk
@ein.command()
async def talk(ctx):
    await ctx.send("Borf!")


### Functions ###

# takes in a color name and converts it to its corresponding hex value
# returns a base 16 integer
def nameToHex(colour):
    hexValue = "0x" + webcolors.name_to_hex(colour)[1:]
    return int(hexValue, 16)

ein.run(settings.TOKEN)
