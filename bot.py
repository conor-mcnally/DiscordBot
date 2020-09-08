import os
import random
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv

#Bot prefix
BOT_PREFIX = ("%")

#DONT FORGET TO ADD YOUR OWN DISCORD TOKEN AND SERVER NAME IN the .env FILE
#Tokens to be used for bot within .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

Client = discord.Client()
client = Bot(command_prefix=BOT_PREFIX)

#Some information to display in terminal to show bot working
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

#Command for quotes - WORKS PERFECTLY
@client.command(name='quotes', description="Gives a quote")
async def quotes(ctx):
    possible_responses = [
        'If you want a happy ending, that depends, of course, on where you stop your story.',
        'The enemy of art is the absence of limitations.',
        'Ask not what you can do for your country. Ask whats for lunch.',
        'I passionately hate the idea of being with it, I think an artist has always to be out of step with his time.',
        'A good artist should be isolated. If he isnt isolated, something is wrong.',
    ]
    await ctx.send(random.choice(possible_responses))

#Command for sending gif/image - NEEDS WORK
@client.command(name='gif', description='Sends GIF')
async def gif(ctx):
    possible_gifs = [
    "https://giphy.com/gifs/fandor-cigar-orson-welles-f-for-fake-26BoCO6rR1gezc9Gw",
    "https://giphy.com/gifs/orson-welles-citizen-kane-xnWSYSELI9tF6",
    "https://giphy.com/gifs/classic-applause-clapping-2mxA3QHH4aHFm",
    ]
    await ctx.send(random.choice(possible_gifs))

client.run(TOKEN)

# @client.command(pass_context=True)
# async def test(ctx):
#     currentDT = DT.datetime.now()
#     print(' ')
#     await bot.say("Working!")
#     await client.say("https://imgur.com/gallery/ryvBY92")
#     print("-------------------------")
#     print(currentDT)
#     print("test has been run")
#     print("-------------------------")
