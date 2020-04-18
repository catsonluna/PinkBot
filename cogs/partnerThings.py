import datetime
import discord

from discord.ext import commands

from main import PinkBotPSC, BlacklistedUsers


class Partner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in PinkBotPSC:
            for channel_id in PinkBotPSC:
                if channel_id != message.channel.id:
                    if message.author.bot:
                        return
                    elif message.author.id in BlacklistedUsers:
                        return
                    else:
                        channel = self.bot.get_channel(channel_id)
                        embed = discord.Embed(colour=message.author.color, timestamp=datetime.datetime.utcnow())
                        embed.add_field(name="Sender:", value=message.author, inline=True)
                        embed.add_field(name="Server name:", value=message.guild.name, inline=True)
                        embed.add_field(name="Message:", value=message.content or "\u200b", inline=False)
                        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Partner(bot))
