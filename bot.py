import os
from dotenv import load_dotenv
from discord.ext import commands
import discord

# Charger les variables d'environnement
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configurer les intents nécessaires
intents = discord.Intents.default()
intents.members = True

# Créer le bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Charger les commandes depuis commands.py
from commands import setup_commands
setup_commands(bot)

# Événement quand le bot est prêt
@bot.event
async def on_ready():
    print(f"{bot.user.name} est connecté et prêt à l'emploi !")

# Lancer le bot
bot.run(TOKEN)
