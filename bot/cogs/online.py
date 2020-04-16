import discord
import sys

from discord.ext import commands


class Online(commands.Cog, name="Online"):
    """ A cog that monitors status change events and uses these to check
        if a user has been online on discord in the past day

    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        # Checks if a user's status changed, meaning they used discord in some way today
        role = discord.utils.find(lambda r: r.name == 'Student', after.guild.roles)
        if after.bot == False and role in after.roles:
            if str(before.status) != str(after.status):
                print("{} has gone {}.".format(after.name, after.status))


def setup(bot):
    bot.add_cog(Online(bot))
