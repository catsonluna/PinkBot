import discord
import discord.utils
import json
from discord.ext import commands


def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)


private = getJSON('./private.json')

AdminList = private.get("AdminList")

BlacklistedUsers = private.get("BlacklistedUsers")

PinkBotStaff = private.get("PinkBotStaff")

PinkBotContributors = private.get("PinkBotContributors")

KSoft_api = private.get("KSoft_api")

BotToken = private.get("BotToken")

PinkBotPS = private.get("PinkBotPartnerServers")

PinkBotPSC = private.get("PinkBotPartnerChats")


def get_prefix(bot, message):
    if message.author.id in AdminList:
        prefixes = ['pinkdev ']
    else:
        prefixes = []

    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = [
    'cogs.botcommands',
    'cogs.guildcommands',
    'cogs.hypixelstats',
    'cogs.privatecommands',
    'cogs.mod',
    'cogs.photo',
    'cogs.info',
    'cogs.helpcommand',
    'cogs.pinkbotserver',
    'cogs.games',
    'cogs.partnerThings'
]

bot = commands.Bot(command_prefix=get_prefix, description='yes')
bot.remove_command("help")
for extension in initial_extensions:
    bot.load_extension(extension)

bot.load_extension("jishaku")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('>help to get started'))
    print(f'Y-you tu-urned mwe on successfully daddy uwu, im looking at')
    print(bot.cogs)
    print(len(bot.guilds))



@bot.event
async def on_member_join(member):
    g = member.guild.id
    channel = bot.get_channel(681911212740575297)
    if g == 681561708052873358:
        await channel.send(f"Welcome {member.mention} to PinkBots support server, check out the info channel")


bot.run(BotToken, bot=True, reconnect=True)
