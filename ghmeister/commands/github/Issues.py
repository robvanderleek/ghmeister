from typing import Annotated, Optional

import typer
from requests import Response

from ghmeister.services.api_service import api_post, api_get

issues = typer.Typer(no_args_is_help=True)


@issues.command(help=f"Create an issue")
def create(owner: str,
           repo: str,
           title: str,
           body: Annotated[str, typer.Option(show_default=False)] = None,
           milestone: Annotated[str, typer.Option(show_default=False)] = None,
           labels: Annotated[Optional[list[str]], typer.Option(show_default=False)] = None,
           assignees: Annotated[Optional[list[str]], typer.Option(show_default=False)] = None
           ) -> Response:
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


@issues.command(help=f"List repository issues")
def list_repository_issues(owner: str, repo: str):
    return api_get(f'repos/{owner}/{repo}/issues')
