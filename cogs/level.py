import datetime

import discord
from discord.ext import commands

from main import PinkBotPS, bot


class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        member = message.author
        author_id = str(message.author.id)
        user = await self.bot.pg_con.fetchrow("SELECT * FROM global_level WHERE user_id = $1", author_id)
        cur_xp = user['xp']
        cur_lvl = user['lvl']
        if not user:
            await self.bot.pg_con.execute(
                "INSERT INTO global_level (user_id, lvl, xp, dm, msgs) VALUES ($1, 1, 0, 1, 0)",
                author_id)
        else:
            await self.bot.pg_con.execute("UPDATE global_level SET xp = $1 WHERE user_id = $2",
                                          user["xp"] + 1,
                                          author_id)
            await self.bot.pg_con.execute("UPDATE global_level SET msgs = $1 WHERE user_id = $2", user["msgs"] + 1,
                                          author_id)

            if cur_xp >= round(4 * (cur_lvl ** 3) / 5):
                await self.bot.pg_con.execute("UPDATE global_level SET lvl = $1 WHERE user_id = $2", cur_lvl + 1,
                                              user["user_id"])
                lvl_c = bot.get_channel(707593824385368145)
                pfp = member.avatar_url
                embed = discord.Embed(title=f'{member} has leveled up ^^', colour=0xe99ae2,
                                      timestamp=datetime.datetime.utcnow())
                embed.set_thumbnail(url=pfp)
                embed.add_field(name="Level:", value=user["lvl"] + 1, inline=False)
                embed.add_field(name="XP:", value=user["xp"], inline=False)
                embed.add_field(name="Msgs sent:", value=user["msgs"], inline=False)
                embed.add_field(name="Server in:", value=message.guild.name, inline=False)
                embed.add_field(name="Server id:", value=message.guild.id, inline=False)
                embed.add_field(name="Note:",
                                value="This is a global level system, to disable theses dms plase use >lvlToggle, to join the support server do >help",
                                inline=False)
                await lvl_c.send(embed=embed)

                dm = await member.create_dm()
                if user['dm'] == 1:
                    await dm.send(embed=embed)
                elif user['dm'] == 0:
                    return

    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        user = await self.bot.pg_con.fetchrow("SELECT * FROM global_level WHERE user_id = $1", member_id, )

        if not user:
            await ctx.send(f"`{member}` Has no xp")
        else:
            pfp = member.avatar_url
            color = ctx.author.color
            embed = discord.Embed(title=f'{member} Info', colour=color, timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url=pfp)
            embed.add_field(name="Level:", value=user["lvl"], inline=False)
            embed.add_field(name="XP:", value=user["xp"], inline=False)
            embed.add_field(name="Msgs sent:", value=user["msgs"], inline=False)
            if user["dm"] == 1:
                embed.add_field(name="dm status:", value="Level up dms are enabled", inline=False)
            elif user["dm"] == 0:
                embed.add_field(name="dm status:", value="Level up dms are disabled", inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    async def lvlToggle(self, ctx):
        author_id = str(ctx.author.id)
        user = await self.bot.pg_con.fetchrow("SELECT * FROM global_level WHERE user_id = $1", author_id)
        if user["dm"] == 1:
            await self.bot.pg_con.execute("UPDATE global_level SET dm = $1 WHERE user_id = $2",
                                          user["dm"] - 1,
                                          author_id)
            await ctx.send("Level up dms have been disabled")
        elif user["dm"] == 0:
            await self.bot.pg_con.execute("UPDATE global_level SET dm = $1 WHERE user_id = $2",
                                          user["dm"] + 1,
                                          author_id)
            await ctx.send("Level up dms have been enabled")

    @commands.command()
    async def dmStatus(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        author_id = str(member.id)
        user = await self.bot.pg_con.fetchrow("SELECT * FROM global_level WHERE user_id = $1", author_id)
        if user["dm"] == 1:
            await ctx.send("Your level up dms are enabled")
        elif user["dm"] == 0:
            await ctx.send("Your level up dms are disabled")


def setup(bot):
    bot.add_cog(Levels(bot))
