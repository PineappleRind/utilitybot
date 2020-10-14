import discord
from discord.ext import commands
from discord import utils
import asyncpg
import asyncio
import re


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command
    async def ban(self, ctx, member: discord.Member, reason=None):
        pass

    @commands.command(aliases=["silence, stfu"])
    async def mute(self, ctx, member: discord.Member, reason=None):
        pass

    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        pass

    """Set the muted default muted role by utility bot to a custom one."""
    @commands.command()
    async def mutedrole(self, ctx, role_id: int):
        
    
    
    @commands.command()
    async def warn(self, ctx, reason=None):
        pass

def setup(bot):
    bot.add_cog(Moderation(bot))