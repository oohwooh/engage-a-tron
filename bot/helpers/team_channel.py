from discord.abc import GuildChannel


def is_team_channel(channel: GuildChannel, team_category_name="teams") -> bool:
    """Matches the channel category to team_category_name, default is `teams`. Not case sensitive."""
    if channel.category.name.lower() == team_category_name.lower():
        return True
    return False
