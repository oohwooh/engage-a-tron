import discord
import sys

from discord.ext import commands


class Voice(commands.Cog, name="Voice"):
    """A cog that monitors users joining voice channels to keep track of engamenent"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        # Checks that the user joined a VC (before none, now not none) and that it isn't the AFK channel
        if before.channel is None and after.channel is not None and not after.afk:
            print("{} has joined {}.".format(member.name, after.channel))


def setup(bot):
    bot.add_cog(Voice(bot))