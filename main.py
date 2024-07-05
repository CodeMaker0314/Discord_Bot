import discord, os, asyncio
from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

bot_status = cycle(['Status One', 'Hello from FATE/CASTER', 'Status Code 123', 'Subscribe to FATE/CASTER'])

@tasks.loop(seconds=5)
async def change_bot_status():
    await bot.change_presence(activity=discord.Game(next(bot_status)))

@bot.event
async def on_ready():
    print('Bot ready!')
    change_bot_status.start()

# get token from token.txt
with open('token.txt') as file:
    TOKEN = file.read()

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)

asyncio.run(main())