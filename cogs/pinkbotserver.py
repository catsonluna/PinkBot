import aiohttp
import discord
from discord import Guild
from discord.ext import commands
from discord.utils import get

from main import bot


class PinkBotServer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(PinkBotServer(bot))
