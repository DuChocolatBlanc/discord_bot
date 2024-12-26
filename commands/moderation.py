import discord
from discord.ext import commands

class ModerationCommands(commands.Cog):
    """Commandes de modération pour gérer les rôles et les membres."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def add_role(self, ctx, member: discord.Member, role: discord.Role):
        """Ajoute un rôle à un membre."""
        await member.add_roles(role)
        await ctx.send(f"Rôle {role.name} attribué à {member.display_name}.")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        """Supprime un rôle d'un membre."""
        await member.remove_roles(role)
        await ctx.send(f"Rôle {role.name} retiré à {member.display_name}.")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick un membre."""
        await member.kick(reason=reason)
        await ctx.send(f"{member.display_name} a été kické. Raison : {reason}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban un membre."""
        await member.ban(reason=reason)
        await ctx.send(f"{member.display_name} a été banni. Raison : {reason}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member_name):
        """Déban un membre."""
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            if user.name == member_name:
                await ctx.guild.unban(user)
                await ctx.send(f"{member_name} a été débanni.")
                return
        await ctx.send(f"Aucun utilisateur nommé {member_name} n'est banni.")

async def setup(bot):
    await bot.add_cog(ModerationCommands(bot))
