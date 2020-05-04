import asyncio
import datetime

import discord
from discord.ext import commands


class HelpCommand(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        color = ctx.author.color
        embed = discord.Embed(title='PinkBot help', colour=color, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Links:", value=f"[Commands](https://docs.pinkbot.xyz/) "
                                             f"\n[Support server](https://discord.gg/TUkcgWt) "
                                             f"\n[Invite the bot](https://discordapp.com/api/oauth2/authorize?client_id=697887266307047424&permissions=8&scope=bot)"
                                             f"\n[Github](https://github.com/pinkulu/pinkbot)"
                                             f"\n[Vote for the bot](https://top.gg/bot/697887266307047424)", inline=False)
        embed.add_field(name="Developer:", value="Pinkulu", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCommand(bot))
