import datetime

import discord
import aiohttp
from discord.ext import commands


class Countries(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def country(self, ctx, name: str = None):
        if name is None:
            ctx.send("Please specify a country")
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://restcountries.eu/rest/v2/name/{name}') as resp:
                    country = (await resp.json())[0]
                color = ctx.author.color
                embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                embed.add_field(name="Country name:", value=country["name"], inline=False)
                embed.add_field(name="Time zone(s):", value=country["timezones"], inline=False)
                embed.add_field(name="Region:", value=country["region"], inline=False)
                embed.add_field(name="Population:", value=country["population"], inline=False)
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Countries(bot))
