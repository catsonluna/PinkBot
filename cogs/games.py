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
ezMsgs = [
    f"Wait... This isn't what I typed!",
    "Anyone else really like Rick Astley?",
    "Hey helper, how play game?",
    "Sometimes I sing soppy, love songs in the car.",
    "I like long walks on the beach and talking on this discord server ",
    "Please go easy on me, this is my first game!",
    'Please go easy on me, this is my first game!',
    'Youre a great person! Do you want to talk on discord with me?',
    'In my free time I like to watch cat videos on Youtube',
    'When I saw the witch with the potion, I knew there was trouble brewing.',
    'If the Discord world is infinite, how is the sun spinning around it?',
    'Hello everyone! I am an innocent player who loves everything Discord.',
    'Plz give me doggo memes!',
    'I heard you like Discord, so I built a computer in Discord in your Discord so you can Discord while you Discord',
    'Why cant the Ender Dragon read a book? Because he always starts at the End.',
    'Maybe we can have a rematch?',
    'I sometimes try to say bad things then this happens :(',
    'Behold, the great and powerful, my magnificent and almighty nemisis!',
    'Doin a bamboozle fren.',
    'Your clicks per second are godly.',
    'What happens if I add chocolate milk to macaroni and cheese?',
    'Can you paint with all the colors of the wind',
    'Blue is greener than purple for sure',
    'I had something to say, then I forgot it.',
    'When nothing is right, go left.',
    'I need help, teach me how to play!',
    'Your personality shines brighter than the sun.',
    'You are very good at the game friend.',
    'I like pineapple on my pizza',
    'I like pasta, do you prefer nachos?',
    'I like Discord pvp but you are truly better than me!',
    'I have really enjoyed playing with you! <3',
    'ILY <3',
    'Pineapple doesnt go on pizza!',
    'Lets be friends instead of fighting okay?',
]


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roastme(self, ctx):
        await ctx.send(random.choice(insults))

    @commands.command()
    async def coin(self, ctx):
        choices = ('Heads', 'Tails')
        coin = random.choice(choices)
        await ctx.send(coin)

    @commands.command()
    async def dabon(self, ctx, member: discord.Member):
        await ctx.send(
            f"<:Dab:700667528976007308> {member.mention} <:Dab:700667528976007308> got <:Dab:700667528976007308> dabbed <:Dab:700667528976007308> on <:Dab:700667528976007308>")

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
        await ctx.send(":crab:" + message + ':crab:')

    @commands.command(name='random', aliases=['number', 'randomnumber'])
    async def random(self, ctx, arg1: int = None, arg2: int = None,):
        if arg1 is None:
            await ctx.send("enter min number")
        elif arg2 is None:
            await ctx.send("enter max number")
        else:
            await ctx.send(random.randint(arg1, arg2))

    @commands.Cog.listener()
    async def on_message(self, message):
        member = message.author
        if message.content.startswith('ez'):
            await message.delete()
            await message.channel.send(f"{member.mention} just said: \n{random.choice(ezMsgs)}")


def setup(bot):
    bot.add_cog(Games(bot))
