import sys
from typing import Annotated, Optional

import typer
from dotenv import load_dotenv
from requests import Response

from ghmeister.Context import Context
from ghmeister.commands import Utils
from ghmeister.commands.github import Issues, Users
from ghmeister.commands.github.Repositories import Repositories
from ghmeister.commands.github.Users import get_authenticated_user
from ghmeister.utils import pretty_print_json, pretty_print
from ghmeister.version import version
from ghmeister.wizard.wizard import repository_wizard, user_wizard

load_dotenv()


def handle_response(response: Response, version: Optional[bool] = None, json: bool = False):
    if response.ok:
        res_json = response.json()
        if res_json:
            if json:
                pretty_print_json(res_json)
            else:
                pretty_print(res_json)
        else:
            Context.console.print("[green]Success[/green]")
    else:
        Context.console.print(f"[red]Error: {response.status_code}[/red]")
        sys.exit(1)


cli = typer.Typer(no_args_is_help=True, add_completion=False, result_callback=handle_response)
cli.add_typer(Users.users, name="users", help="GitHub endpoints for users (alias: user)")
cli.add_typer(Users.users, name="user", hidden=True)
cli.add_typer(Issues.issues, name="issues", help="GitHub endpoints for issues (alias: issue)")
cli.add_typer(Issues.issues, name="issue", hidden=True)
cli.add_typer(Repositories.app, name="repositories", help="GitHub endpoints for repositories")
cli.add_typer(Utils.utils, name="utils", help="Various utilities")


def _version_callback(show: bool):
    if show:
        print(f"GitHub Meister version: {version}")
        raise typer.Exit()


@cli.callback(invoke_without_command=False)
def callback(
        version: Annotated[
            Optional[bool],
            typer.Option(
                "--version", "-V", help="Show version", callback=_version_callback
            )
        ] = None,
        json: Annotated[bool, typer.Option(
            "--json", "-j", help="Output as JSON", show_default=False
        )
        ] = False
):
    """GH Meister: GitHub management made easy."""
    if version:
        raise typer.Exit()


def wizard():
    owner = Context.get_owner()
    repo = Context.get_repo()
    if owner and repo:
        repository_wizard(owner, repo)
    else:
        login = get_authenticated_user().json()['login']
        user_wizard(login)


def main():
    Context.init()
    if len(sys.argv) == 1:
        try:
            wizard()
        except KeyboardInterrupt:
            pass
        print('\u2B50 Please star GH Meister on GitHub! https://github.com/robvanderleek/ghmeister')
    else:
        cli()


if __name__ == '__main__':
    main()
