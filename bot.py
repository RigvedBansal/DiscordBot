import discord
from discord.ext import commands, tasks
import random
import time
import os
from itertools import cycle

client = commands.Bot(command_prefix='.')

status = cycle(['That Fine Butt', 'Your Ass'])


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))


@client.event
async def on_ready():
    change_status.start()
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


@client.command(aliases=['giveme'])
async def drugs(ctx, *, substance):
    await ctx.send(f"here you go, get high on {substance}")


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

if __name__ == "__main__":

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

    client.run()
