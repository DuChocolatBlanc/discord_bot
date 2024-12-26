import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configurer les intents
intents = discord.Intents.default()
intents.members = True

# Créer une instance du bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Charger dynamiquement les cogs depuis le dossier "commands"
for filename in os.listdir('./commands'):
    if filename.endswith('.py') and not filename.startswith('__'):
        bot.load_extension(f'commands.{filename[:-3]}')

# Événement : prêt
@bot.event
async def on_ready():
    print(f"{bot.user.name} est prêt et en ligne !")

# Lancer le bot
bot.run(TOKEN)
