from typing import Annotated

import typer
from requests import Response

from ghmeister.commands.github.types.Repository import Repository
from ghmeister.commands.github.types.Visibility import Visibility
from ghmeister.services.api_service import api_get

repositories = typer.Typer(no_args_is_help=True)


@repositories.command(help=f"Get a repository")
def get(owner: Annotated[str, typer.Option(show_default=False)],
        repo: Annotated[str, typer.Option(show_default=False)],
        ) -> Repository:
    return api_get(f'repos/{owner}/{repo}', response_model=Repository)


@repositories.command(help=f"List repositories for the authenticated user")
def user_repos(visibility: Visibility = Visibility.all,
               affiliation: str = 'owner,collaborator,organization_member') -> Response:
    return api_get('user/repos', params={'visibility': visibility.value, 'affiliation': affiliation})
