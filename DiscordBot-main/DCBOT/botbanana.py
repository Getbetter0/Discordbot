import discord
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot {bot.user}!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def seg(ctx, odp):
    odp = odp.lower()
    plastic = ["butelka", "opakowanie po chipsach", "opakowanie po jogurcie", "torebka foliowa"]
    paper = ["gazeta", "kartka papieru", "karton po mleku", "karton po soku"]
    glass = ["słoik", "butelka po napoju", "szklanka", "kieliszek"]
    zmieszane = ["zużyta chusteczka", "butelka po szamponie", "zużyta gąbka"]
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