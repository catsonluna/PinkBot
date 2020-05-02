import asyncio
import datetime

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

BotToken2 = private.get("BotToken2")

PinkBotPS = private.get("PinkBotPartnerServers")

PinkBotPSC = private.get("PinkBotPartnerChats")

PinkBotPSO = private.get("PinkBotPartnerServerOwners")


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
    'cogs.info',
    'cogs.photo',
    'cogs.helpcommand',
    'cogs.pinkbotserver',
    'cogs.games',
    'cogs.partnerThings',
    'cogs.countries'
]

bot = commands.Bot(command_prefix=get_prefix, description='yes')
bot.remove_command("help")
for extension in initial_extensions:
    bot.load_extension(extension)

bot.load_extension("jishaku")


async def status_task():
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game('>help to get started'))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("watching over " + str(len(bot.guilds)) + " guilds"))
        await asyncio.sleep(10)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("watching over " + str(len(bot.users)) + " users"))
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

@bot.event
async def on_member_join(member):
    g = member.guild.id
    channel = bot.get_channel(681911212740575297)
    if g == 681561708052873358:
        await channel.send(f"Welcome {member.mention} to PinkBots support server, check out the info channel")


@bot.command()
async def pStaff(ctx, arg1: str = None, member: discord.User = None):
    if ctx.author.id in PinkBotStaff:
        if arg1 is None:
            await ctx.send(
                "please choose an action \nBan (puts a PinkBot blacklist on the person) \nunban (removes a PinkBot blacklist on the person)")
        elif arg1 == "ban":
            with open('./private.json', 'w') as file:
                BlacklistedUsers.append(member.id)
                json.dump(private, file, indent=4)
                await ctx.send(f"{ctx.author} has banned {member}")
                channel = bot.get_channel(698923439729279016)
                embed = discord.Embed(colour=0xfb0006, timestamp=datetime.datetime.utcnow())
                embed.add_field(name=f"Banned by:", value=ctx.author, inline=False)
                embed.add_field(name="User banned:", value=f"{member}", inline=False)
                embed.add_field(name="User id:", value=member.id, inline=False)
                await channel.send(embed=embed)
        elif arg1 == "unban":
            with open('./private.json', 'w') as file:
                BlacklistedUsers.remove(member.id)
                json.dump(private, file, indent=4)
                await ctx.send(f"{ctx.author} has unbanned {member}")
                channel = bot.get_channel(698923439729279016)
                embed = discord.Embed(colour=0x00fb52, timestamp=datetime.datetime.utcnow())
                embed.add_field(name=f"Unbanned by:", value=ctx.author, inline=False)
                embed.add_field(name="User unbanned:", value=f"{member}", inline=False)
                embed.add_field(name="User id:", value=member.id, inline=False)
                await channel.send(embed=embed)


@bot.command()
async def pAdmin(ctx, arg1: str = None, member: discord.User = None):
    if ctx.author.id in PinkBotStaff:
        if arg1 is None:
            await ctx.send(
                "Available PinkBot admin commands \nstaff (add the person as a PinkBot staff) \nunstaff (removes somones PinkBot staff) \npso (adds a server partner) \npsor (removes a server partner)")
        elif arg1 == "staff":
            with open('./private.json', 'w') as file:
                PinkBotStaff.append(member.id)
                json.dump(private, file, indent=4)
                await ctx.send(f"{ctx.author} has made {member} staff")
                channel = bot.get_channel(698923439729279016)
                embed = discord.Embed(colour=0x56fed8, timestamp=datetime.datetime.utcnow())
                embed.add_field(name=f"Admin:", value=ctx.author, inline=False)
                embed.add_field(name="User made staff:", value=f"{member}", inline=False)
                embed.add_field(name="User id:", value=member.id, inline=False)
                await channel.send(embed=embed)
        elif arg1 == "unstaff":
            with open('./private.json', 'w') as file:
                PinkBotStaff.remove(member.id)
                json.dump(private, file, indent=4)
                await ctx.send(f"{ctx.author} has removed {member} staff")
                channel = bot.get_channel(698923439729279016)
                embed = discord.Embed(colour=0xaa0004, timestamp=datetime.datetime.utcnow())
                embed.add_field(name=f"Admin:", value=ctx.author, inline=False)
                embed.add_field(name="User removed staff:", value=f"{member}", inline=False)
                embed.add_field(name="User id:", value=member.id, inline=False)
                await channel.send(embed=embed)
        if arg1 == "pso":
            with open('./private.json', 'w') as file:
                PinkBotPSO.append(member.id)
                json.dump(private, file, indent=4)
                await ctx.send(f"{ctx.author} has made {member} a PinkBot partner")
                channel = bot.get_channel(698923439729279016)
                embed = discord.Embed(colour=0xff8b77, timestamp=datetime.datetime.utcnow())
                embed.add_field(name=f"Admin:", value=ctx.author, inline=False)
                embed.add_field(name="User made partner:", value=f"{member}", inline=False)
                embed.add_field(name="User id:", value=member.id, inline=False)
                await channel.send(embed=embed)
        elif arg1 == "psor":
            with open('./private.json', 'w') as file:
                PinkBotPSO.remove(member.id)
                json.dump(private, file, indent=4)
                await ctx.send(f"{ctx.author} has removed {member} from being a PinkBot partner")
                channel = bot.get_channel(698923439729279016)
                embed = discord.Embed(colour=0x3f4678, timestamp=datetime.datetime.utcnow())
                embed.add_field(name=f"Admin:", value=ctx.author, inline=False)
                embed.add_field(name="Users partner removed:", value=f"{member}", inline=False)
                embed.add_field(name="User id:", value=member.id, inline=False)
                await channel.send(embed=embed)


bot.run(BotToken2, bot=True, reconnect=True)
