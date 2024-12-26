import random
from discord.ext import commands

def setup_games(bot):
    @bot.command()
    async def rps(ctx, choice: str):
        """Joue à Pierre, Papier, Ciseaux."""
        choices = ["pierre", "papier", "ciseaux"]
        bot_choice = random.choice(choices)

        if choice not in choices:
            await ctx.send("Choisis entre `pierre`, `papier`, ou `ciseaux`.")
            return

        if choice == bot_choice:
            result = "Égalité !"
        elif (choice == "pierre" and bot_choice == "ciseaux") or \
             (choice == "papier" and bot_choice == "pierre") or \
             (choice == "ciseaux" and bot_choice == "papier"):
            result = "Tu gagnes ! 🎉"
        else:
            result = "Tu perds ! 😢"

        await ctx.send(f"Tu as choisi {choice}, j'ai choisi {bot_choice}. {result}")
