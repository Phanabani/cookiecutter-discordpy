{% set class_name = cookiecutter.project_name|title|replace(' ', '') -%}
import logging
from pathlib import Path
import sys

import discord
import discord.ext.commands as commands

from {{ cookiecutter.project_slug }}.config import *

__all__ = [
    '{{ class_name }}',
    'run_bot'
]

logger = logging.getLogger('{{ cookiecutter.project_slug }}')


# noinspection PyMethodMayBeStatic
class {{ class_name }}(commands.Bot):

    def __init__(self, config: ConfigBot):

        intents = discord.Intents(
            guilds=True,
            members=True
        )
        allowed_mentions = discord.AllowedMentions(users=True)
        activity = discord.Game(f'{config.command_prefix}help')

        super().__init__(
            # Client params
            max_messages=None,
            intents=intents,
            allowed_mentions=allowed_mentions,
            activity=activity,
            # Bot params
            command_prefix=config.command_prefix,
            description=config.description
        )

        self.load_extension('{{ cookiecutter.project_slug }}.my_extension')

    async def on_connect(self):
        logger.info('Client connected')

    async def on_disconnect(self):
        logger.info('Client disconnected')

    async def on_resumed(self):
        logger.info('Session resumed')

    async def on_ready(self):
        logger.info('Client started')

    async def on_error(self, event_method: str, *args, **kwargs):
        exc_type, __, __ = sys.exc_info()

        if exc_type is discord.HTTPException:
            logger.warning('HTTP exception', exc_info=True)
        elif exc_type is discord.Forbidden:
            logger.warning('Forbidden request', exc_info=True)

        elif event_method == 'on_message':
            msg: discord.Message = args[0]
            logger.error(
                f'Unhandled in on_message (content: {msg.content!r} '
                f'author: {msg.author} channel: {msg.channel})',
                exc_info=True
            )
        else:
            logger.error(
                f"Unhandled in {event_method} (args: {args} kwargs: {kwargs})",
                exc_info=True
            )


def run_bot():
    # Load config
    config_path = Path(__file__).parent / 'config.json'
    config = Config.parse_file(config_path)

    # {{ cookiecutter.project_name }} logging
    logger = logging.getLogger('{{ cookiecutter.project_slug }}')
    logger.setLevel(config.logging.{{ cookiecutter.project_slug }}_logging_level)
    logger.addHandler(config.logging.handler)

    # Discord logging
    logger = logging.getLogger('discord')
    logger.setLevel(config.logging.discord_logging_level)
    logger.addHandler(config.logging.handler)

    # Run bot
    {{ cookiecutter.project_slug }} = {{ class_name }}(config.bot)
    {{ cookiecutter.project_slug }}.loop.set_debug(True)
    {{ cookiecutter.project_slug }}.run(config.bot_token.get_secret_value())
