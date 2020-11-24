import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Examples are Ready')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!!!")
        print("ping was called from cog.example")


def setup(client):
    client.add_cog(Example(client))
