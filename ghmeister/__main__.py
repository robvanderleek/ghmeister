import sys
from typing import Annotated, Optional

import typer
from dotenv import load_dotenv
from requests import Response, HTTPError

from ghmeister.Context import Context
from ghmeister.commands import Utils
from ghmeister.commands.github import Issues, Users, Repositories
from ghmeister.commands.github.Users import get_authenticated_user
from ghmeister.menu.menu import repository_menu, user_menu
from ghmeister.utils import pretty_print_json, format_data
from ghmeister.version import version

load_dotenv()


def handle_response(response: Response, version: Optional[bool] = None, json: bool = False):
    if response.ok:
        if response.status_code == 204:
            Context.console.print("[green]Success[/green]")
            return
        res_json = response.json()
        if res_json:
            if json:
                pretty_print_json(res_json)
            else:
                format_data(res_json)
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
cli.add_typer(Repositories.repositories, name="repositories", help="GitHub endpoints for repositories")
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
        r = Repositories.get(owner, repo)
        repository_menu(owner, repo)
    else:
        login = get_authenticated_user().json()['login']
        user_menu(login)


def main():
    Context.init()
    if len(sys.argv) == 1:
        try:
            wizard()
        except KeyboardInterrupt:
            pass
        print('\u2B50 Please star GH Meister on GitHub! https://github.com/robvanderleek/ghmeister')
    else:
        try:
            cli()
        except HTTPError as e:
            Context.console.print(f"[red]{e.args[0]}[/red]")
            sys.exit(1)


if __name__ == '__main__':
    main()
