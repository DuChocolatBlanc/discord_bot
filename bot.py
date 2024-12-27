import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils.helpers import setup_logger

# Configurer le logger personnalisé
logger = setup_logger('discord_bot', 'bot.log')

# Charger les variables d'environnement
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configurer les intents
intents = discord.Intents.default()
intents.message_content = True  # Pour lire les messages
intents.members = True  # Pour interagir avec les membres

# Créer une instance du bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Log au démarrage du bot
@bot.event
async def on_ready():
    logger.info(f"{bot.user.name} est prêt et en ligne !")

# Log pour les commandes
@bot.event
async def on_command(ctx):
    logger.info(f"Commande reçue : {ctx.command} par {ctx.author}")

# Log pour les erreurs de commandes
@bot.event
async def on_command_error(ctx, error):
    logger.error(f"Erreur sur la commande {ctx.command}: {error}")
    await ctx.send(f"Une erreur est survenue : {error}")

# Charger dynamiquement les cogs
@bot.event
async def on_ready():
    logger.info("Chargement des cogs...")
    for filename in os.listdir('./commands'):
        if filename.endswith('.py') and not filename.startswith('__'):
            await bot.load_extension(f'commands.{filename[:-3]}')
    logger.info("Tous les cogs ont été chargés.")

# Lancer le bot
bot.run(TOKEN)
