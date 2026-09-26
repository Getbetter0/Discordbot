# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random
import os
import requests

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------gg------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def random_mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('dog')
async def dog(ctx):
    '''Po wywołaniu polecenia dog program wywołuje funkcję get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command()
async def seg(ctx, odp):
    plastic = ["butelka", "opakowanie po chipsach", "opakowanie po jogurcie", "torebka foliowa"]
    paper = ["gazeta", "kartka papieru", "karton po mleku", "karton po soku"]
    glass = ["słoik", "butelka po napoju", "szklanka", "kieliszek"]
    zmieszane = ["zużyta chusteczka", "zużyta szampon", "zużyta gąbka"]
    bio = ["skórka od banana", "resztki jedzenia", "liść", "gałązka"]
    if odp in plastic:
        await ctx.send("To jest plastik, wrzuć do żółtego pojemnika.")
    elif odp in paper:
        await ctx.send("To jest papier, wrzuć do niebieskiego pojemnika.")
    elif odp in glass:
        await ctx.send("To jest szkło, wrzuć do zielonego pojemnika.")
    elif odp in zmieszane:
        await ctx.send("To są odpady zmieszane, wrzuć do czerwonego pojemnika.")
    elif odp in bio:
        await ctx.send("To są odpady biodegradowalne, wrzuć do brązowego pojemnika.")


bot.run('TOKEN')