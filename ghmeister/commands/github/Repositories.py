from typing import Annotated

import typer
from requests import Response

from ghmeister.services.api_service import api_get


class Repositories:
    app = typer.Typer(no_args_is_help=True)

    @staticmethod
    @app.command(help=f"Get a repository")
    def get(owner: Annotated[str, typer.Option(show_default=False)],
            repo: Annotated[str, typer.Option(show_default=False)],
            ) -> Response:
        return api_get(f'repos/{owner}/{repo}')
