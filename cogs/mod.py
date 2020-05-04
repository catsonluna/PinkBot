import discord
from discord.ext import commands


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['clear'])
    @commands.has_permissions(manage_messages=True)
    async def clean(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send(f'{limit} massages cleared by {ctx.author.mention}', delete_after=5)


def setup(bot):
    bot.add_cog(Mod(bot))
