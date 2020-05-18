import datetime
import json

import discord.utils

from discord.ext import commands

from main import bot, AdminList, BlacklistedUsers, PinkBotPSO, private, PinkBotStaff


class PrivateCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, channel_id: int, *, message: str):
        if ctx.author.id in AdminList:
            channel = bot.get_channel(channel_id)
            await channel.send(message)

    @commands.command()
    async def sayhere(self, ctx, *, message: str):
        if ctx.author.id in AdminList:
            await ctx.send(message)
            await ctx.message.delete()

    @commands.command()
    async def dmsend(self, ctx, user_id: int, *, message: str):
        if ctx.author.id in AdminList:
            member = bot.get_user(user_id)
            channel = await member.create_dm()
            channel2 = bot.get_channel(698635545408045087)
            color = ctx.author.color
            embed = discord.Embed(title=f'Dm from PinkBot', colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Name of the receiver:", value=f"{member}")
            embed.add_field(name="Message:", value=f"{message}", inline=False)
            embed.add_field(name="Note:",
                            value="If you want to send us a message please use >dm your message here(only works in dms), abuse of this or any other features can get you banned from doing commands in the future",
                            inline=False)
            await channel.send(embed=embed)
            await channel2.send(embed=embed)

    @commands.command()
    async def pStaff(self, ctx, arg1: str = None, member: discord.User = None):
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

    @commands.command()
    async def pAdmin(self, ctx, arg1: str = None, member: discord.User = None):
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
            elif arg1 == "lvl clear:":
                author_id = str(ctx.author.id)
                user = await self.bot.pg_con.fetchrow("SELECT * FROM users WHERE user_id = $1", author_id)
                if user["dm"] == 1:
                    await self.bot.pg_con.execute("UPDATE users SET dm = $1 WHERE user_id = $2",
                                                  user["dm"] - 1,
                                                  author_id)
                    await ctx.send("Level up dms have been disabled")
                elif user["dm"] == 0:
                    await self.bot.pg_con.execute("UPDATE users SET dm = $1 WHERE user_id = $2",
                                                  user["dm"] + 1,
                                                  author_id)
                    await ctx.send("Level up dms have been enabled")


def setup(bot):
    bot.add_cog(PrivateCommands(bot))
