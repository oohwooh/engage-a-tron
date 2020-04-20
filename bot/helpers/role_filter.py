from discord import Member
from bot.main import include_roles as main_included_roles
from bot.main import exclude_roles as main_excluded_roles


def check_roles(
    member: Member,
    include_roles: list = main_included_roles,
    exclude_roles: list = main_excluded_roles,
) -> bool:
    member_roles = [r.name for r in member.roles]
    if include_roles in member_roles and exclude_roles not in member_roles:
        return True
    return False
