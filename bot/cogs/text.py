import discord
import sys

from discord.ext import commands


class Text(commands.Cog, name="Online"):
    """A cog that monitors messages being sent to monitor engagement"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, message):
        # Checks that a sent message is not from a bot and is from a user with a student role
        role = discord.utils.find(lambda r: r.name == 'Student', message.guild.roles)
        if message.author.bot == False and role in message.author.roles:
            print("{} has sent a message in {}".format(message.author.name, message.channel))


        




def setup(bot):
    bot.add_cog(Text(bot))
