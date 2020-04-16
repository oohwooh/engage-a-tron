from os import getenv
import logging
import traceback

from discord.ext.commands import Bot

BOT_TOKEN = getenv("BOT_TOKEN")
logging.basicConfig(level=logging.INFO)

bot = Bot(
    command_prefix="e!",
    command_not_found="Nope, that command doesn't seem right! Maybe try something else?",
    description="How's your day going?",
)

initial_cogs = [
    "cogs.online",
    "cogs.voice",
    "cogs.text",
]

# Here we load our extensions(cogs) listed above in [initial_extensions].
for cog in initial_cogs:
    # noinspection PyBroadException
    try:
        bot.load_extension(cog)
        logging.info(f"Successfully loaded extension {cog}")
    except Exception as e:
        logging.exception(
            f"Failed to load extension {cog}.", exc_info=traceback.format_exc()
        )


@bot.event
async def on_message(message):
    # Insures the other commands are still processed, it's a whole thing
    await bot.process_commands(message)


bot.run(BOT_TOKEN, bot=True, reconnect=True)
