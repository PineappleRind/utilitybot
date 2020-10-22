import discord
from discord.ext import commands
from discord import utils
import asyncpg
import asyncio
import re


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: discord.Member, reason=None):

        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} was banned for {reason}.")

        for reasons in reason:
            if not reasons:
                await ctx.send(f"Please specify a reason to ban {member}.")

        for members in member:
            if not members:
                await ctx.send(f"Pleasy specify a member to ban {member.mention}")

    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} was kicked for {reason}")

        for reasons in reason:
            if not reasons:
                await ctx.send(f"Please specify a reason to ban {member}.")

        for members in member:
            if not members:
                await ctx.send(f"Pleasy specify a member to ban {member.mention}")

    @commands.has_permissions(mute_members=True)
    @commands.bot_has_permissions(mute_members=True)
    @commands.command(aliases=["silence, stfu"])
    async def mute(self, ctx, member: discord.Member, reason=None):
        if not reason:
            reason = "No Reason Provided."

        discord.utils.get(
            # Pull default muted role or the custom muted role from the server
            ctx.roles, name="Muted"
        )  
    
    @commands.has_permissions(mute_members=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        pass

    """Set the muted default muted role by utility bot to a custom one."""
    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def mutedrole(self, ctx, role_id: int):
        pass
    
    @commands.has_permissions(mute_members=True)
    @commands.command()
    async def warn(self, ctx, member: discord.Member, reason="No reason specified"):
        
        await ctx.send(f"{member.mention} was warned for {reason}")

        """Error Handlers"""
        if not member:
            await ctx.send("You have specify a member to warn")
            
        if len(reason) > 250:
            await ctx.send("Reason's have to be less than 250 characters.")

        if ctx.author.id != ctx.guild.owner.id:
            await ctx.send("You can't warn the Owner of the Server!")

        if ctx.author == member:
            await ctx.send("You can't wwarn your self.")
            
        
        # Update warnings for the user in db

def setup(bot):
    bot.add_cog(Moderation(bot))