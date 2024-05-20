import os

import requests
import typer
from rich import print_json

users = typer.Typer(no_args_is_help=True)


def _get_github_token() -> str:
    token = os.getenv('GITHUB_MEISTER_TOKEN')
    if not token:
        raise Exception('No GitHub access token found in environment')
    return token


@users.command(help="Get the authenticated user")
def get_authenticated_user() -> dict:
    token = _get_github_token()
    res = requests.get('https://api.github.com/user', headers={'Authorization': f'Bearer {token}'})
    # print_json(data=res.json())
    return res.json()
