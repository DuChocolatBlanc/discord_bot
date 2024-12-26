import os
from dotenv import load_dotenv
from discord.ext import commands
import discord

def get_role_by_name(guild, role_name):
    """Retourne un rôle par son nom."""
    return discord.utils.get(guild.roles, name=role_name)
