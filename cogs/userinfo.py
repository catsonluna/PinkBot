import datetime
import aiohttp
import discord

from discord.ext import commands

from main import BlacklistedUsers, AdminList, PinkBotStaff, PinkBotContributors


class UserInfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="userinfo")
    async def userinfo(self, ctx, member: discord.User = None):
        if member is None:
            await ctx.send('please specify a member')
        else:
            pfp = member.avatar_url
            color = ctx.author.color
            uid = member.id
            embed = discord.Embed(title=f'{member} info', colour=color, timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url=pfp)
            embed.add_field(name="Account created:", value=str(member.created_at))
            if member.id in BlacklistedUsers:
                embed.add_field(name="Blacklisted on PinkBot?:", value="Yes", inline=False)
            else:
                embed.add_field(name="Blacklisted on PinkBot?:", value="No", inline=False)
            if member.id in AdminList:
                embed.add_field(name="PinkBot admin?:", value="Yes", inline=True)
            else:
                embed.add_field(name="PinkBot admin?:", value="No", inline=True)
            if member.id in PinkBotStaff:
                embed.add_field(name="PinkBot staff?:", value="Yes", inline=True)
            else:
                embed.add_field(name="PinkBot staff?:", value="No", inline=True)
            if member.id in PinkBotContributors:
                embed.add_field(name="PinkBot contributor?:", value="Yes", inline=True)
            else:
                embed.add_field(name="PinkBot contributor?:", value="No", inline=True)
            embed.add_field(name="UserID:", value=f"{uid}", inline=False)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(UserInfo(bot))
