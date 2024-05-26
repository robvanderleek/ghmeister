from typing import Annotated

import typer

from ghmeister.Context import Context
from ghmeister.services.api_service import api_post
from ghmeister.services.user_input import input_text

issues = typer.Typer(no_args_is_help=True)


@issues.command(help="Create an issue")
def create(owner: Annotated[str, typer.Argument(default_factory=Context.get_owner)],
           repo: Annotated[str, typer.Argument(default_factory=Context.get_repo)]) -> dict:
    title = input_text('Title')
    return api_post(f'repos/{owner}/{repo}/issues',
                    {'title': title, 'body': 'This is the body of the issue'})
