from discord.ext import commands

class FunCommands(commands.Cog):
    """Commandes fun comme des blagues ou mini-jeux."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """Commande fun qui dit bonjour."""
        await ctx.send("Salut ! 👋")

    @commands.command()
    async def dice(self, ctx):
        """Lance un dé et donne un nombre entre 1 et 6."""
        import random
        result = random.randint(1, 6)
        await ctx.send(f"🎲 Tu as obtenu : {result}")

async def setup(bot):
    await bot.add_cog(FunCommands(bot))
