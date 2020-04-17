import asyncio

import discord
import datetime
import discord.utils
from discord import guild
from discord.ext import commands

from main import bot, BlacklistedUsers, PinkBotPS


class BotInfo(commands.Cog):

    def __init__(self, botc):
        self.bot = botc

    @commands.command(name="botinfo")
    async def botinfo(self, ctx):
        guilds = len(list(bot.guilds))
        support = "https://discord.gg/Fykpshg"
        color = ctx.author.color
        embed = discord.Embed(title='PinkBot info', url=support, colour=color, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Servers in:", value=str(guilds), inline=False)
        embed.add_field(name="Description:",
                        value=f"PinkBot is made to be multi functional, it will get updated frequently, for any suggestions/bugs/feedback join the support server by [clicking here](https://discord.gg/TUkcgWt)",
                        inline=False)
        embed.add_field(name="Developer:", value="Pinkulu", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def suggest(self, ctx, *, message: str):
        member = ctx.message.author
        if ctx.message.author.id in BlacklistedUsers:
            await ctx.send(
                f"You may not use this command as you are blacklisted on PinkBot, for more info join PinkBots support server https://discord.gg/TUkcgWt")
        else:
            channel = bot.get_channel(698581537066582066)
            channel2 = bot.get_channel(698581569371373610)
            color = ctx.author.color
            embed = discord.Embed(title=f'{member} Suggestion', colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Name:", value=f'{member}', inline=False)
            embed.add_field(name="Suggestion:", value=f"{message}", inline=False)
            sent = await channel.send(embed=embed)
            await ctx.send("Your suggestion has been sent")

            def check(reaction, user):
                return reaction.message.id in sent.id

            try:
                reaction, _ = await self.bot.wait_for('reaction_add', timeout=86400.0, check=check)
                if reaction.emoji == "\U0001F44D":
                    color = ctx.author.color
                    embed = discord.Embed(title=f'{member} Suggestion', colour=color,
                                          timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Name:", value=f'{member}', inline=False)
                    embed.add_field(name="Suggestion:", value=f"{message}", inline=False)
                    sent2 = await channel2.send(embed=embed)
                    await sent2.add_reaction(emoji="\U0001F44D")
                    await sent2.add_reaction(emoji="\U0001F44E")
                    channel = await member.create_dm()
                    await channel.send(
                        f"Hello {member.mention}, your suggestion `{message}` has been approved to go on the main bord https://discord.gg/TUkcgWt where people can vote on your idea!")

                elif reaction.emoji == "\U0001F44E":
                    channel = await member.create_dm()
                    await channel.send(
                        f"Hello {member}, your suggestion `{message}` wasnt approved, this can be do to:\n1 your suggestion was spam/wasnt real \n2 This feature is already in the bot \n if you have any questions you can ask them in the support server https://discord.gg/TUkcgWt")
            except asyncio.TimeoutError:
                await ctx.send(f"Suggestion: {message} by {member.mention} has wasnt approved in time")

    @commands.command()
    @commands.dm_only()
    async def dm(self, ctx, *, message: str):
        if ctx.message.author.id in BlacklistedUsers:
            await ctx.send(
                f"You may not use this command as you are blacklisted on PinkBot, for more info join PinkBots support server [here](https://discord.gg/TUkcgWt)")
        else:
            channel = bot.get_channel(698635497966403636)
            color = ctx.author.color
            member = ctx.message.author
            embed = discord.Embed(title=f'Dm from {member}', colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Name:", value=f'{member}', inline=False)
            embed.add_field(name="Message:", value=f"{message}", inline=False)
            await channel.send(embed=embed)
            await ctx.send(
                "Your dm has been sent and will be proceed soon, remember, abuse of this or any other system could get you banned from doing these commands, dms and suggestions are monitored by PinkBots staff team")

    @commands.command(name="links")
    async def links(self, ctx):
        color = ctx.author.color
        embed = discord.Embed(title='PinkBot liks', colour=color, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Support server:", value=f"[here](https://discord.gg/TUkcgWt)", inline=False)
        embed.add_field(name="Invite the bot to your server:",
                        value=f"[here](https://discordapp.com/api/oauth2/authorize?client_id=697887266307047424&permissions=8&scope=bot)",
                        inline=False)
        embed.add_field(name="GitHub:", value="[here](https://github.com/pinkulu/pinkbot)", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="partner")
    async def partner(self, ctx):
        guild = ctx.guild
        color = ctx.author.color
        embed = discord.Embed(title='PinkBot partner info', colour=color, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Info:", value=f"PinkBot partner server is a server that gets some advantages from PinkBot, if you want to be a PinkBot partner server join the discord here and dm me or something like that so we can discus it [here](https://discord.gg/TUkcgWt)", inline=False)
        embed.add_field(name="Advantages:", value=f"at the moment there are no advantages, but there's gonna be some soon ;)", inline=False)
        partnered = 'This server is a PinkBot partner' if guild.id in PinkBotPS else 'This server isnt a PinkBot partner'
        embed.add_field(name="This server:", value=partnered, inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(BotInfo(bot))
