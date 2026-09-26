import discord
from bot_logic import gen_pass
from bot_logic import coin_flip
# Zmienna intents przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej client i przekazanie mu uprawnień
client = discord.Client(intents=intents)

gen_pass(10)

@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Cześć!")
    elif message.content.startswith('$flip'):
        await message.channel.send(coin_flip())
    elif message.content.startswith('$genpass'):
        await message.channel.send("Twoje hasło: " + gen_pass(15))
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("TOKEN")