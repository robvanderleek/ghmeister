from typing import Annotated

import typer

from ghmeister.Context import Context

issues = typer.Typer(no_args_is_help=True)


@issues.command(help="Create an issue")
def create(owner: Annotated[str, typer.Argument(default_factory=Context.get_owner)],
           repo: Annotated[str, typer.Argument(default_factory=Context.get_repo)]):
    print(f'Creating issue for {owner}/{repo}')
    print('Creating issue')
