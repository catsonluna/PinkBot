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
        embed.add_field(name="Hypixel:",
                        value=f">hypixel username \n>hypixel username bedwars",
                        inline=False)
        embed.add_field(name="Mod:",
                        value=f">clean number \n>kick username reason \n>ban username reason",
                        inline=False)
        embed.add_field(name="Useful:",
                        value=f">BotInfo \n>UserInfo \n >suggest and then write the suggestion \n>dm your message here (can be only used in dms with PinkBot, this will send a message to PinkBots staff team) \n>links",
                        inline=False)
        embed.add_field(name="Fun commands:",
                        value=f">rostme \n>coin \n>8ball \n>crab + text \n>dabon @mention the person",
                        inline=False)
        embed.add_field(name="Photo commands:",
                        value=f"List of all photo tags(also can be used with no tag)",
                        inline=False)
        embed.add_field(name=">meme", value="pepe \ndoge \nkappa \ndab \nbirb \nfbi \nclap", inline=True)
        embed.add_field(name=">cute", value="dpg \nkiss \npat \nhug \nfox \nlick \nheadrub \ncat \ntickle", inline=True)
        embed.add_field(name=">nsfw", value="hentai \nhentai_gif \nneko \nass", inline=True)
        embed.add_field(name=">wikihow", value="no tags", inline=True)
        embed.add_field(name="Bot prefixes:",
                        value=f"If you want to, you can also just @me or use . as a prefix, insted of >",
                        inline=False)
        embed.add_field(name="Private commands in PinkNations server:",
                        value=f">guild \n>verifyme username",
                        inline=False)
        embed.add_field(name="Future of the bot:",
                        value="More things will be added soon, im constantly updating the bot, for support server please click the title",
                        inline=False)
        embed.add_field(name="Something else?:", value=f"if you didnt find what your looking for, or need something else you can always join out support server [here](https://discord.gg/TUkcgWt)")
        embed.add_field(name="Invite?:", value=f"if you want to invite the bot to your server [click here](https://discordapp.com/api/oauth2/authorize?client_id=697887266307047424&permissions=8&scope=bot)")
        embed.add_field(name="Developer:", value="Pinkulu", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCommand(bot))
