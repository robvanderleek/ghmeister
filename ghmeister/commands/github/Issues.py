from typing import Annotated, Optional

import typer
from requests import Response

from ghmeister.commands.github.types.Issue import Issue
from ghmeister.commands.github.types.LockReason import LockReason
from ghmeister.services.api_service import api_post, api_get, api_put, api_delete

issues = typer.Typer(no_args_is_help=True)


@issues.command(help=f"Create an issue")
def create(owner: str,
           repo: str,
           title: str,
           body: Annotated[str, typer.Option()] = None,
           milestone: Annotated[str, typer.Option()] = None,
           labels: Annotated[Optional[list[str]], typer.Option()] = None,
           assignees: Annotated[Optional[list[str]], typer.Option()] = None
           ) -> Response:
    data = {'title': title, 'body': body, 'milestone': milestone, 'labels': labels, 'assignees': assignees}
    return api_post(f'repos/{owner}/{repo}/issues', data)


@issues.command(help=f"List repository issues")
def list_repository_issues(owner: str, repo: str) -> list[Issue]:
    return api_get(f'repos/{owner}/{repo}/issues', response_model=list[Issue])


@issues.command(help=f"Lock an issue")
def lock(owner: str, repo: str, issue_number: int, lock_reason: Annotated[LockReason, typer.Option()] = None):
    return api_put(f'repos/{owner}/{repo}/issues/{issue_number}/lock', {'lock_reason': lock_reason})


@issues.command(help=f"Unlock an issue")
def unlock(owner: str, repo: str, issue_number: int):
    return api_delete(f'repos/{owner}/{repo}/issues/{issue_number}/lock')
