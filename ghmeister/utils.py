from ghmeister.Context import Context
from ghmeister.commands.github.types.Issue import Issue
from ghmeister.commands.github.types.Repository import Repository


def pretty_print_json(data: dict):
    Context.console.print_json(data=data)


def fmt_short(item: any) -> str:
    if isinstance(item, Repository):
        return f'{item.owner.login}/{item.name}'
    elif isinstance(item, Issue):
        return f'#{item.number}'
    else:
        return str(item)


def fmt_oneline(item: any) -> str:
    if isinstance(item, Issue):
        return f'#{item.number}: {item.title}'
    else:
        return fmt_short(item)
