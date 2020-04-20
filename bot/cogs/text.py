import discord
import sys
import logging

from discord.ext import commands
from helpers import role_filter, team_channel


class Text(commands.Cog, name="Online"):
    """A cog that monitors messages being sent to monitor engagement"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Checks that a sent message is not from a bot and is from a user with a student role
        if (
                not message.author.bot
                and role_filter.check_roles(message.author)
        ):
            if team_channel.is_team_channel(message.channel):
                logging.info(f"{message.author.name} has sent a message in team channel {message.channel}")
            else:
                logging.info(f"{message.author.name} has sent a message in non-team channel {message.channel}")



def setup(bot):
    bot.add_cog(Text(bot))
