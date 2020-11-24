import discord
from discord.ext import commands


class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Tests are Ready')

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Test were completed, everything running smoothly")
        print("Test Completed")


def setup(client):
    client.add_cog(Test(client))
