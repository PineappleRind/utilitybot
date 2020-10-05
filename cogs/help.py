import discord
from discord.ext import commands
from discord.ext.commands import errors



class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Global help command (there will be help commands for each module)"""

    async def help(self, ctx, module_name: str):
        if module_name is None:
            embed = discord.Embed(
                title = "Modules",
                description = "List of all the modules you can search up!",
                colour = discord.Colour.blue()
            )
        
            embed.add_field(name=":tada: Fun Commands", value="Fun commands", inline=False)
            embed.add_field(name=":frame_photo: Images", value="Image commands ", inline=False) 
            embed.add_field(name=":wrench:, Utility", value="utility commands", inline=False)
            embed.add_field(name=":information_source :Info", value="u!info")

        
            await ctx.send(embed=embed)
        

        
def setup(bot):
    bot.add_cog(bot(Help))