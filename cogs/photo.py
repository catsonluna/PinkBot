import ksoftapi
import discord

from discord.ext import commands

from main import KSoft_api

client = ksoftapi.Client(api_key=KSoft_api)


class Meme(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="meme")
    async def meme(self, ctx, arg1: str = None):
        if arg1 is None:
            img = await client.random_meme()
            embed = discord.Embed()
            embed.set_image(url=str(img.url))
            await ctx.send(embed=embed)
        else:
            image = await client.random_image(tag=arg1, nsfw=False)
            if image.url is None:
                await ctx.send("Couldnt find that tag, make sure you spelled it right, or maybe it just dosnt exist")
            else:
                embed = discord.Embed()
                embed.set_image(url=str(image.url))
                embed.set_footer(text=str(image.snowflake))
                await ctx.send(embed=embed)

    @commands.command(name="cute")
    async def cute(self, ctx, arg1: str = None):
        if arg1 is None:
            img = await client.random_aww()
            embed = discord.Embed()
            embed.set_image(url=str(img.url))
            await ctx.send(embed=embed)
        else:
            image = await client.random_image(tag=arg1, nsfw=False)
            if image.url is None:
                await ctx.send("Couldnt find that tag, make sure you spelled it right, or maybe it just dosnt exist")
            else:
                embed = discord.Embed()
                embed.set_image(url=str(image.url))
                await ctx.send(embed=embed)

    @commands.command(name="wikihow")
    async def wikihow(self, ctx, member: discord.User = None):
        image = await client.random_wikihow()
        embed = discord.Embed()
        embed.set_image(url=str(image.url))
        await ctx.send(embed=embed)

    @commands.command(name="nsfw")
    @commands.is_nsfw()
    async def nsfw(self, ctx, arg1: str = None):
        if arg1 is None:
            img = await client.random_nsfw()
            embed = discord.Embed()
            embed.set_image(url=str(img.url))
            await ctx.send(embed=embed)
        else:
            image = await client.random_image(tag=arg1, nsfw=True)
            if image.url is None:
                await ctx.send("Couldnt find that tag, make sure you spelled it right, or maybe it just dosnt exist")
            else:
                embed = discord.Embed()
                embed.set_image(url=str(image.url))
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Meme(bot))
