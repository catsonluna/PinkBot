import discord
import aiohttp
import datetime
import discord.utils
from discord.ext import commands


class HypixelStats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hypixel", description="Get hypixel stats")
    async def hypixel(self, ctx, arg1: str = None, arg2: str = None):
        if arg1 is None:
            await ctx.send("I need an IGN", delete_after=5)
            return
        if arg2 is None:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.slothpixel.me/api/players/{arg1}') as resp:
                    player = await resp.json()
                async with session.get(f'https://api.slothpixel.me/api/guilds/{arg1}') as resp:
                    guild = await resp.json()

            color = ctx.author.color
            embed = discord.Embed(title=f'{arg1} Hypixel stats', colour=color, timestamp=datetime.datetime.utcnow())
            if player['rank'] == "MVP_PLUS_PLUS":
                embed.add_field(name="PlayerRank", value="MVP++", inline=False)
            elif player['rank'] == "MVP_PLUS":
                embed.add_field(name="PlayerRank", value="MVP+", inline=False)
            elif player['rank'] == "VIP_PLUS":
                embed.add_field(name="PlayerRank", value="VIP+", inline=False)
            else:
                embed.add_field(name="PlayerRank", value=player['rank'], inline=False)
            embed.add_field(name="Level:", value=player["level"], inline=False)
            embed.add_field(name="Discord:", value=player["links"]["DISCORD"], inline=False)
            embed.add_field(name="Online:", value=player['online'], inline=False)
            embed.add_field(name="Minecraft version:", value=player['mc_version'], inline=False)
            embed.add_field(name="Last game played:", value=player['last_game'], inline=False)
            await ctx.send(embed=embed)
            return
        if arg2 == "bedwars":
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.slothpixel.me/api/players/{arg1}') as resp:
                    player = await resp.json()
            color = ctx.author.color
            embed = discord.Embed(title=f'{arg1} BedWars stats', colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Stars:", value=player["stats"]["BedWars"]["level"], inline=False)
            embed.add_field(name="Wins:", value=player["stats"]["BedWars"]["wins"], inline=False)
            embed.add_field(name="Games played:", value=player["stats"]["BedWars"]["games_played"], inline=False)
            embed.add_field(name="W/l ratio:", value=player["stats"]["BedWars"]["w_l"], inline=False)
            embed.add_field(name="Final Kills:", value=player["stats"]["BedWars"]["final_kills"], inline=False)
            embed.add_field(name="Final Deaths:", value=player["stats"]["BedWars"]["final_deaths"], inline=False)
            embed.add_field(name="Normal Kills:", value=player["stats"]["BedWars"]["kills"], inline=False)
            embed.add_field(name="Normal Deaths:", value=player["stats"]["BedWars"]["deaths"], inline=False)
            embed.add_field(name="FKDR:", value=player["stats"]["BedWars"]["final_k_d"], inline=False)
            embed.add_field(name="Current Winstreak:", value=player["stats"]["BedWars"]["winstreak"], inline=False)
            await ctx.send(embed=embed)
            return
        if arg2 == "duels":
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.slothpixel.me/api/players/{arg1}') as resp:
                    player = await resp.json()
            color = ctx.author.color
            embed = discord.Embed(title=f'{arg1} Duel stats', colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Wins:", value=player["stats"]["Duels"]["wins"], inline=False)
            embed.add_field(name="Kills:", value=player["stats"]["Duels"]["kills"], inline=False)
            embed.add_field(name="Deaths:", value=player["stats"]["Duels"]["deaths"], inline=False)
            embed.add_field(name="Bow hits:", value=player["stats"]["Duels"]["bow_hits"], inline=False)
            embed.add_field(name="Melee hits:", value=player["stats"]["Duels"]["melee_hits"], inline=False)
            embed.add_field(name="Best winstreak:", value=player["stats"]["Duels"]["best_overall_winstreak"],
                            inline=False)
            await ctx.send(embed=embed)
        if arg2 == "uhc":
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api.slothpixel.me/api/players/{arg1}') as resp:
                    player = await resp.json()
            color = ctx.author.color
            embed = discord.Embed(title=f'{arg1} Duel stats', colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Score:", value=player["stats"]["UHC"]["score"], inline=False)
            embed.add_field(name="Wins:", value=player["stats"]["UHC"]["wins"], inline=False)
            embed.add_field(name="Kills:", value=player["stats"]["UHC"]["kills_solo"], inline=False)
            embed.add_field(name="Deaths:", value=player["stats"]["UHC"]["deaths_solo"], inline=False)
            embed.add_field(name="Win/loss:", value=player["stats"]["UHC"]["win_loss"], inline=False)
            embed.add_field(name="Heads eaten:", value=player["stats"]["UHC"]["heads_eaten"], inline=False)
            embed.add_field(name="Coins:", value=player["stats"]["UHC"]["coins"], inline=False)

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HypixelStats(bot))
