from typing import Annotated, Optional

import typer
from requests import Response

from ghmeister.Context import Context
from ghmeister.services.api_service import api_post

issues = typer.Typer(no_args_is_help=True)


@issues.command(help=f"Create an issue: {Context.get_owner()}")
def create(owner: Annotated[str, typer.Option(show_default=False)],
           repo: Annotated[str, typer.Option(show_default=False)],
           title: Annotated[str, typer.Option(show_default=False)],
           body: Annotated[str, typer.Option(show_default=False)] = None,
           milestone: Annotated[str, typer.Option(show_default=False)] = None,
           labels: Annotated[Optional[list[str]], typer.Option(show_default=False)] = None,
           assignees: Annotated[Optional[list[str]], typer.Option(show_default=False)] = None
           ) -> Response:
    # title = input_text('Title')
    data = {'title': title}
    if body:
        data['body'] = body
    if milestone:
        data['milestone'] = milestone
    if labels:
        data['labels'] = labels
    if assignees:
        data['assignees'] = assignees
    return api_post(f'repos/{owner}/{repo}/issues', data)
