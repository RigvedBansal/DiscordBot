import discord
from discord.ext import commands
import random
import time

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("Bot is Ready!!!")


@client.event
async def on_member_join(member):
    print(f"{member} has joined the server!!!")


@client.event
async def on_member_remove(member):
    print(f"{member} has left/ been removed the server!!!")


@client.command(aliases=['8ball', 'ball', 'fortune'])
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
                 'Yes.',
                 'Yes – definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.']
    await ctx.send(f'{random.choice(responses)}')
    print("Someone Called the 8 ball")


@client.command(aliases=['cls'])
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    print(f"The chat was cleared, {amount} messages were deleted")
    await ctx.send(f"The chat was cleared, {amount} messages were deleted")
    time.sleep(2)
    await ctx.channel.purge(limit=1)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.command(aliases=['hey', 'Hey', 'Hello', "hola", "Hola"])
async def hello(ctx):
    responses = ["Hello there", "Hey dude", "wassup",
                 "Hey how you doin'", "Hola", "Hey fellow discord member"]
    await ctx.send(f"{random.choice(responses)}")


client.run('')
