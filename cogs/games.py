import datetime

import aiohttp
import discord
import random

from discord.ext import commands

insults = ['you smell bad',
           'I would rather look at the sun than your ugly face',
           'Ew',
           'Your mom didnt even call you good looking',
           'You have such a punchable face',
           'Ur mom gay',
           'Your face is so disturbing im on my way to help noah build the ark',
           'you are more disappointing than an unsalted pretzel',
           'your face makes onions cry',
           'Your feet smell',
           'The only thing smaller than your brain is your pp',
           'Shut up',
           'Im a bot with no eyes and i can tell that your ugly',
           'Literally 3 apples high',
           'Smol pp',
           'The difference between you and a flea is that you are more annoying than the flea',
           'There are wonderful things called dreams.  Your dreams are like the 1900s, fading away',
           'If you dont think pink is best then you are big flea',
           'you are like my mom, she likes boys...',
           'your mom has a bigger d than you',
           "Weirdo.",
           "Sucker of big brown dirty eggs!",
           "Idiot.",
           "Licker of salmon-fried fish!"
           "Moron.",
           "Raider of the lost fart!",
           "Rump-roast!",
           "Licker of dirty chicken butts!",
           "Buttfish!",
           "Soiler of towels!",
           "You're in big trouble, little pal. I eat pieces of shit like you for breakfast!",
           "Were you always this stupid or did you take lessons?",
           "100,000 sperm and... you were the fastest?",
           "You're what the French call, 'Les Incompetents'.",
           "You are literally too stupid to insult.",
           "Fat, drunk, and stupid is no way to go through life, son.",
           "Gentlemen, he here may talk like an idiot, and look like an idiot, but don't let that fool you. He really is an idiot.",
           "I didn't know they stacked shit that high!",
           "Hey man, what's wrong with that breath? I can smell it over here!Your breath is so stinky, people look forward to your farts.",
           "Man... you are one pathetic loser.",
           "Did anyone ever tell you you look like a penis with a little hat on?",
           "I wouldn't let you sleep in my room if you were GROWING on my ASS!",
           "Hey! Where did you get those clothes, at the... toilet store?",
           "Mung-tongue!",
           "Math tutor.",
           "Pinhead!",
           "Prison barber.",
           "Mother lover.",
           "Near-sighted gynecologist.",
           "Lying, crying, spying, prying ultra-pig!",
           "You lewd crude bag of pre-chewed food dude!",
           'bad'
           ]


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rostme(self, ctx):
        await ctx.send(random.choice(insults))

    @commands.command()
    async def coin(self, ctx):
        choices = ('Heads', 'Tails')
        coin = random.choice(choices)
        await ctx.send(coin)

    @commands.command()
    async def rps(self, ctx, arg1: str = None):
        choices = ('Rock', 'Paper', 'Scissors')
        rps = random.choice(choices)
        if arg1 is None:
            await ctx.send("please say rock paper or scissors")
        elif arg1 == "rock" or "paper" or "scissors" or "Rock" or "Paper" or "Scissors":
            color = ctx.author.color
            member = ctx.message.author
            embed = discord.Embed(title=f'Rock, paper, scissors with {member}', colour=color,
                                  timestamp=datetime.datetime.utcnow())
            embed.add_field(name=f"{member} choice:", value=f'{arg1}', inline=False)
            embed.add_field(name="Bots choice:", value=f"{rps}", inline=False)
            await ctx.send(embed=embed)

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command(name='crab')
    async def crab(self, ctx, *, crabswag: str = 'You need to give me a message for me to crabify it'):
        message = discord.utils.escape_mentions(crabswag)
        message = message.split(' ')
        message = ':crab:'.join(message)
        await ctx.send(message + ':crab:')


def setup(bot):
    bot.add_cog(Games(bot))
