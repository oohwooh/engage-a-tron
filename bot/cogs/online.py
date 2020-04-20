import discord
import sys
import logging

from helpers import role_filter

from discord.ext import commands
from main import include_roles, exclude_roles


class Online(commands.Cog, name="Online"):
    """ A cog that monitors status change events and uses these to check
        if a user has been online on discord in the past day

    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        # Checks if a user's status changed, meaning they used discord in some way today
        if (
            not after.bot
            and role_filter.check_roles(after)
            and str(before.status) != str(after.status)
        ):
            logging.info(f"{after.name} has gone {after.status.name}.")


def setup(bot):
    bot.add_cog(Online(bot))
