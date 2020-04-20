from discord.abc import GuildChannel


def is_team_channel(channel: GuildChannel, team_category_name="Teams") -> bool:
    if channel.category == team_category_name:
        return True
    return False
