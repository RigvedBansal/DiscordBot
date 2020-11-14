import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is Ready!!!")

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server!!!")

@client.event
async def on_member_remove(member):
    print(f"{member} has left/ been removed the server!!!")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! This message took {round(client.latency * 1000)} ms to send')

@client.command()
async def fate(ctx):
    responses = ['Don’t count on it.',
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Outlook good.',
            'Reply hazy, try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.' ,
            'Yes – definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.']
    await ctx.send(f'{random.choice(responses)}')






client.run('Nzc3MjI4NDk3MTc3MDE4NDM4.X7AYcQ.-_VqtTv-SPfZmRkEDRnoXiSMwUA')