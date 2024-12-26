from discord.ext import commands

class UtilityCommands(commands.Cog):
    """Commandes utilitaires comme ping et infos."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Répond avec Pong !"""
        await ctx.send("Pong ! 🏓")

    @commands.command()
    async def info(self, ctx):
        """Donne des informations sur le serveur."""
        server = ctx.guild
        await ctx.send(f"Nom du serveur : {server.name}\nNombre de membres : {server.member_count}")

async def setup(bot):
    await bot.add_cog(UtilityCommands(bot))
