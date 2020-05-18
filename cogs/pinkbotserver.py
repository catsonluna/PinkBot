import aiohttp
import discord
from discord import Guild
from discord.ext import commands
from discord.utils import get

from main import bot


class PinkBotServer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        g = member.guild.id
        channel = bot.get_channel(681911212740575297)
        if g == 681561708052873358:
            await channel.send(f"Welcome {member.mention} to PinkBots support server, check out the info channel")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        g = member.guild.id
        channel = bot.get_channel(681911212740575297)
        if g == 681561708052873358:
            await channel.send(f"Aww {member.mention} just left :c, hope we see them again")


def setup(bot):
    bot.add_cog(PinkBotServer(bot))
