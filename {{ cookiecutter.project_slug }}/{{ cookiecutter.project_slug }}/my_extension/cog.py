import logging

import discord
from discord.ext import commands

__all__ = [
    'MyCog'
]

logger = logging.getLogger('{{ cookiecutter.project_slug }}.my_extension')


class MyCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, context: commands.Context):
        await context.reply('Pong!')
