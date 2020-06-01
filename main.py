import asyncio

import asyncpg
import discord
import discord.utils
import json
from discord.ext import commands


def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)


private = getJSON('./cogs/private.json')

keys = getJSON('./keys.json')

AdminList = private.get("AdminList")

BlacklistedUsers = private.get("BlacklistedUsers")

PinkBotStaff = private.get("PinkBotStaff")

PinkBotContributors = private.get("PinkBotContributors")

PinkBotPS = private.get("PinkBotPartnerServers")

PinkBotPSC = private.get("PinkBotPartnerChats")

PinkBotPSO = private.get("PinkBotPartnerServerOwners")

KSoft_api = keys.get("KSoft_api")

BotToken = keys.get("BotToken")

BotToken2 = keys.get("BotToken2")

dbpass = keys.get("dbpass")

initial_extensions = [
    'cogs.botcommands',
    'cogs.guildcommands',
    'cogs.hypixelstats',
    'cogs.privatecommands',
    'cogs.mod',
    'cogs.info',
    'cogs.photo',
    'cogs.helpcommand',
    'cogs.games',
    'cogs.level',
    'cogs.countries'
]


async def get_prefix(bot, message):
    prefixes = ["pink", '>', "."]
    return commands.when_mentioned_or(*prefixes)(bot, message)


bot = commands.Bot(command_prefix=get_prefix, description='yes', case_insensitive=True)
bot.remove_command("help")
for extension in initial_extensions:
    bot.load_extension(extension)

bot.load_extension("jishaku")


async def create_db_pool():
    bot.pg_con = await asyncpg.create_pool(database="pinkbot", user="pinkulu",
                                           password=dbpass)


async def status_task():
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game('>help to get started'))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.online,
                                  activity=discord.Game("watching over " + str(len(bot.guilds)) + " guilds"))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.online,
                                  activity=discord.Game("watching over " + str(len(bot.users)) + " users"))
        await asyncio.sleep(10)


@bot.event
async def on_ready():
    print(f'Y-you tu-urned mwe on successfully daddy uwu, im looking at')
    print(bot.cogs)
    print("Guilds im in:")
    print(len(bot.guilds))
    print("People im watching over:")
    print(len(bot.users))
    bot.loop.create_task(status_task())


bot.loop.run_until_complete(create_db_pool())
bot.run(BotToken2, bot=True, reconnect=True)
