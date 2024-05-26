import typer

from ghmeister.services.api_service import api_get

users = typer.Typer(no_args_is_help=True)


@users.command(help="Get the authenticated user")
def get_authenticated_user() -> dict:
    return api_get('user')
