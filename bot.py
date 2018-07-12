import discord
from discord.ext import commands
import youtube_dl

TOKEN = 'NDYzOTIwMTM2OTAzMTk2Njcy.DiP5yA.jaE5naPcMPD1QXZZjM5vlTfiUeg'
client = commands.Bot(command_prefix='.')

extensions = {'music'}

@client.event
async def on_ready():
    print('Bot online.')

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

client.run(TOKEN)
