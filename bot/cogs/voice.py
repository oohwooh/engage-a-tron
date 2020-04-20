import discord
import sys

from discord.ext import commands
from helpers import role_filter, team_channel
import logging


class Voice(commands.Cog, name="Voice"):
    """A cog that monitors users joining voice channels to keep track of engamenent"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        # Checks that the user joined a VC (before none, now not none) and that it isn't the AFK channel
        if (
            not member.bot
            and role_filter.check_roles(member)
            and before.channel is None
            and after.channel is not None
            and not after.afk
        ):
            if team_channel.is_team_channel(after.channel):
                logging.info(f"{member.name} has joined team channel {after.channel}.")
            else:
                logging.info(f"{member.name} has joined non-team channel {after.channel}.")


def setup(bot):
    bot.add_cog(Voice(bot))
