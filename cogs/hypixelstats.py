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
        channel = ctx.message.channel
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.slothpixel.me/api/players/{arg1}') as resp:
                player = await resp.json()
        if arg1 is None:
            await ctx.send("I need an IGN", delete_after=5)
            return
        if 'error' in player:
            await ctx.send(f'`{arg1}` is not a valid username')
        else:
            if arg2 is None:
                async with channel.typing():
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
                    if "error" in guild:
                        embed.add_field(name="Guild:", value=f"{arg1} isn't in a guild")
                    else:
                        embed.add_field(name="Guild:", value=guild["name"])
                    embed.add_field(name="Discord:", value=player["links"]["DISCORD"], inline=False)
                    embed.add_field(name="Online:", value=player['online'], inline=False)
                    embed.add_field(name="Minecraft version:", value=player['mc_version'], inline=False)
                    embed.add_field(name="Last game played:", value=player['last_game'], inline=False)
                    await ctx.send(embed=embed)
                    print(player)
            elif arg2 == "bedwars":
                async with channel.typing():
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
            elif arg2 == "duels":
                async with channel.typing():
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
            elif arg2 == "guild":
                async with channel.typing():
                    async with aiohttp.ClientSession() as session:
                        async with session.get(f'https://api.slothpixel.me/api/guilds/{arg1}') as resp:
                            guild = await resp.json()
                            color = ctx.author.color
                        if "error" in guild:
                            embed = discord.Embed(title=f"{arg1} is not in a Guild", colour=color,
                                                  timestamp=datetime.datetime.utcnow())
                            await ctx.send(embed=embed)
                        else:
                            embed = discord.Embed(title=f"{arg1} Guild", colour=color, timestamp=datetime.datetime.utcnow())
                            embed.add_field(name="Guild name:", value=guild["name"], inline=False)
                            embed.add_field(name="Guild tag:", value=guild["tag"], inline=False)
                            embed.add_field(name="Guild level:", value=guild["level"], inline=False)
                            embed.add_field(name="Guild legacy ranking:", value=guild["legacy_ranking"], inline=False)
                            embed.add_field(name="Guild description:", value=guild["description"], inline=False)
                            await ctx.send(embed=embed)
            elif arg2 == "buildbattle":
                async with channel.typing():
                    async with aiohttp.ClientSession() as session:
                        async with session.get(f'https://api.slothpixel.me/api/players/{arg1}') as resp:
                            player = await resp.json()
                    color = ctx.author.color
                    embed = discord.Embed(title=f'{arg1} BuildBattle stats', colour=color, timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Wins:", value=player["stats"]["BuildBattle"]["wins"], inline=False)
                    embed.add_field(name="Total votes:", value=player["stats"]["BuildBattle"]["total_votes"], inline=False)
                    embed.add_field(name="Coins:", value=player["stats"]["BuildBattle"]["coins"], inline=False)
                    embed.add_field(name="Correct guesses(guess the build):", value=player["stats"]["BuildBattle"]["correct_guesses"], inline=False)
                    embed.add_field(name="Super votes:", value=player["stats"]["BuildBattle"]["super_votes"], inline=False)
                    await ctx.send(embed=embed)
            elif arg2 == "pit":
                async with channel.typing():
                    async with aiohttp.ClientSession() as session:
                        async with session.get(f'https://api.slothpixel.me/api/players/{arg1}') as resp:
                            player = await resp.json()
                    color = ctx.author.color
                    embed = discord.Embed(title=f'{arg1} Duel stats', colour=color, timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Kills:", value=player["stats"]["Pit"]["kills"], inline=False)
                    embed.add_field(name="Assists:", value=player["stats"]["Pit"]["assists"], inline=False)
                    embed.add_field(name="Deaths:", value=player["stats"]["Pit"]["deaths"], inline=False)
                    embed.add_field(name="k/d ratio:", value=player["stats"]["Pit"]["kd_ratio"], inline=False)
                    embed.add_field(name="Melee hits:", value=player["stats"]["Pit"]["sword_hits"], inline=False)
                    embed.add_field(name="Bow accuracy:", value=player["stats"]["Pit"]["arrow_accuracy"],
                                    inline=False)
                    embed.add_field(name="Gold:", value=player["stats"]["Pit"]["gold"], inline=False)
                    embed.add_field(name="Xp:", value=player["stats"]["Pit"]["xp"], inline=False)
                    embed.add_field(name="Prestige:", value=player["stats"]["Pit"]["prestige"], inline=False)
                    await ctx.send(embed=embed)
            else:
                await ctx.send(f"i dont have the stats for `{arg2}`, or maybe you just misspelled")


def setup(bot):
    bot.add_cog(HypixelStats(bot))
