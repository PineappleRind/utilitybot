import discord
import discord.ext 
from discord.ext import commands
import datetime

# This class represents all the different categorys of commands
class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def commands(self, ctx, category):


        if 'error' in category:
            await ctx.send(":x:That category isn't availaible")
        

        if category == "moderation":
            color = ctx.author.color
            embed = discord.Embed(
                title="Moderation commands",
                description="Here is a list of all the moderation commands!",
                color = color

            )
def setup(bot):
    bot.add_cog(Commands(bot))
    bot.logging.info("Loaded cog Commands")