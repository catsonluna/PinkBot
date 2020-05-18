import datetime
import aiohttp
import discord

from discord.ext import commands

from main import BlacklistedUsers, AdminList, PinkBotStaff, PinkBotContributors, PinkBotPS, PinkBotPSO


class UserInfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="userinfo")
    async def userinfo(self, ctx, member: discord.User = None):
        member = ctx.author if not member else member
        member_id = str(member.id)
        user = await self.bot.pg_con.fetchrow("SELECT * FROM global_level WHERE user_id = $1", member_id, )
        pfp = member.avatar_url
        color = ctx.author.color
        uid = member.id
        dt = datetime.datetime.strptime(f"{member.created_at}", "%y-%m-%d %H-%M-%S")
        embed = discord.Embed(title=f'{member} info', colour=color, timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=pfp)
        embed.add_field(name="Account created:", value=f"{dt}", inline=False)
        embed.add_field(name="PinkBot level", value=user['lvl'], inline=False)

        if member.id in AdminList:
            embed.add_field(name="PinkBot admin?:", value="Yes", inline=False)
        else:
            embed.add_field(name="PinkBot admin?:", value="No", inline=False)
        if member.id in PinkBotStaff:
            embed.add_field(name="PinkBot staff?:", value="Yes", inline=False)
        else:
            embed.add_field(name="PinkBot staff?:", value="No", inline=False)
        if member.id in PinkBotContributors:
            embed.add_field(name="PinkBot contributor?:", value="Yes", inline=False)
        else:
            embed.add_field(name="PinkBot contributor?:", value="No", inline=False)
        if member.id in PinkBotPSO:
            embed.add_field(name="PinkBot partner?:", value="Yes", inline=False)
        else:
            embed.add_field(name="PinkBot partner?:", value="No", inline=False)
        if member.id in BlacklistedUsers:
            embed.add_field(name="Blacklisted on PinkBot?:", value="Yes", inline=False)
        else:
            embed.add_field(name="Blacklisted on PinkBot?:", value="No", inline=False)
        embed.add_field(name="UserID:", value=f"{uid}", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="serverinfo", aliases=["server"])
    async def serverinfo(self, ctx):
        guild = ctx.guild
        color = ctx.author.color
        embed = discord.Embed(title=f'{guild} info', colour=color, timestamp=datetime.datetime.utcnow())
        if guild.icon_url:
            embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="Server name:", value=guild.name, inline=False)
        embed.add_field(name="Server id:", value=guild.id, inline=False)
        embed.add_field(name="Server member count:", value=str(guild.member_count), inline=False)
        embed.add_field(name="Owner:", value=guild.owner)
        partnered = 'yes' if guild.id in PinkBotPS else 'no'
        embed.add_field(name="PinkBot partnered:", value=partnered, inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="servericon")
    async def servericon(self, ctx, guild: discord.Guild = None):
        if guild is None:
            guild = ctx.guild
            color = ctx.author.color
            embed = discord.Embed(title=f'{guild} Picture', colour=color, timestamp=datetime.datetime.utcnow())
            if guild.icon_url:
                embed.set_image(url=guild.icon_url)
                await ctx.send(embed=embed)
        else:
            color = ctx.author.color
            embed = discord.Embed(title=f'{guild} Picture', colour=color, timestamp=datetime.datetime.utcnow())
            if guild.icon_url:
                embed.set_image(url=guild.icon_url)
                await ctx.send(embed=embed)

    @commands.command(name="avatar", aliases=["pfp"])
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
            pfp = member.avatar_url
            member = ctx.author
            color = ctx.author.color
            embed = discord.Embed(title=f'{member} Picture', colour=color, timestamp=datetime.datetime.utcnow())
            embed.set_image(url=pfp)
            await ctx.send(embed=embed)
        else:
            pfp = member.avatar_url
            member = ctx.author
            color = ctx.author.color
            embed = discord.Embed(title=f'{member} Picture', colour=color, timestamp=datetime.datetime.utcnow())
            embed.set_image(url=pfp)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(UserInfo(bot))
