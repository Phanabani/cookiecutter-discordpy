from discord.ext.commands import Bot

from .cog import MyCog


def setup(bot: Bot):
    bot.add_cog(MyCog(bot))
