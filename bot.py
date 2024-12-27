import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configurer les intents
intents = discord.Intents.default()
intents.message_content = True  # Nécessaire pour lire les messages
intents.members = True  # Nécessaire pour interagir avec les membres

# Créer une instance du bot
bot = commands.Bot(command_prefix="!", intents=intents)

# Charger dynamiquement les extensions (cogs)
@bot.event
async def on_ready():
    print(f"{bot.user.name} est prêt et en ligne !")
    for filename in os.listdir('./commands'):
        if filename.endswith('.py') and not filename.startswith('__'):
            await bot.load_extension(f'commands.{filename[:-3]}')

# Lancer le bot
bot.run(TOKEN)
