import discord
import sys

from discord.ext import commands


class Text(commands.Cog, name="Online"):
    """A cog that monitors messages being sent to monitor engagement"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, message):
        # Checks that a sent message is not from a bot
        if message.


def setup(bot):
    bot.add_cog(Text(bot))
