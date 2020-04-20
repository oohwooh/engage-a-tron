import discord
import sys
import logging

from discord.ext import commands


class Text(commands.Cog, name="Online"):
    """A cog that monitors messages being sent to monitor engagement"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, member):
        # Checks that a sent message is not from a bot and is from a user with a student role
        role = discord.utils.find(lambda r: r.name == 'Student', member.guild.roles)  # TODO: Is this too slow?
        if not member.author.bot and role in member.author.roles:
            logging.info(f"{member.author.name} has sent a message in {member.channel}")


def setup(bot):
    bot.add_cog(Text(bot))
