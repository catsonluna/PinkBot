import datetime

import aiohttp
import discord
from discord import Guild
from discord.ext import commands
from discord.utils import get

from main import bot


class GuildCommandCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Add the role if in guild")
    async def verifyme(self, ctx, arg1: str = None, arg2: str = None, ):
        if ctx.guild.id == 696786836613496934:
            if arg1 is None:
                await ctx.send("I need an IGN", delete_after=5)
                return
            if arg2 is None:
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'https://api.slothpixel.me/api/players/{arg1}') as resp:
                        player = await resp.json()
                    async with session.get(f'https://api.slothpixel.me/api/guilds/{arg1}') as resp:
                        guild = await resp.json()
                    if player['links']['DISCORD'] == str(ctx.author):
                        if guild["name"] == "PinkNation":
                            member = ctx.message.author
                            role = get(member.guild.roles, name="Guild Members")

                            await member.add_roles(role)
                            await ctx.send("You have been verified", delete_after=5)
                            channel = bot.get_channel(697516184794562600)
                            await channel.send(f'{ctx.author.mention} is now a verified guild member with ign {arg1}')
                        else:
                            await ctx.send("You are not in the guild", delete_after=5)
                    else:
                        await ctx.send("Connect your discord and try again, or maybe your just not in the guild",
                                       delete_after=5)
        else:
            await ctx.send('This is PinkNations Discord servers private command')

    @commands.command(description="Guilds info")
    async def guild(self, ctx):
        if ctx.guild.id == 696786836613496934:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.slothpixel.me/api/guilds/pinkulu') as resp:
                    guild = await resp.json()
            color = ctx.author.color
            embed = discord.Embed(title=f'PinkNation`s stats', colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Tag:", value=guild["tag"], inline=False)
            embed.add_field(name="Level:", value=guild["level"], inline=False)
            embed.add_field(name="Exp:", value=guild["exp"], inline=False)
            embed.add_field(name="Description:", value=guild["description"], inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send('This is PinkNations Discord servers private command')


def setup(bot):
    bot.add_cog(GuildCommandCog(bot))
