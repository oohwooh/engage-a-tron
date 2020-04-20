from discord import Member


def check_roles(
    member: Member, include_roles: list = ["Student"], exclude_roles: list = [],
) -> bool:
    member_roles = [r.name for r in member.roles]
    if any(ele in member_roles for ele in include_roles) and not any(
        ele not in member_roles for ele in exclude_roles
    ):
        return True
    return False
