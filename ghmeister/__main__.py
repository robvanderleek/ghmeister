import sys

import typer
from dotenv import load_dotenv
from requests import Response

from ghmeister.Context import Context
from ghmeister.commands import Utils
from ghmeister.commands.github import Issues, Users
from ghmeister.commands.github.Repositories import Repositories
from ghmeister.utils import pretty_print_json
from ghmeister.wizard.repository_wizard import repository_wizard
from ghmeister.wizard.user_wizard import user_wizard

load_dotenv()


def handle_response(response: Response):
    if response.ok:
        json = response.json()
        if json:
            pretty_print_json(json)
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


@cli.callback(invoke_without_command=False)
def callback(ctx: typer.Context):
    """GH Meister: GitHub management made easy."""


def wizard():
    if Context.get_owner() and Context.get_repo():
        repository_wizard()
    else:
        user_wizard()


def main():
    Context.init()
    if len(sys.argv) == 1:
        try:
            wizard()
        except KeyboardInterrupt:
            print('\u2B50 Please star GH Meister on GitHub! https://github.com/robvanderleek/ghmeister')
    else:
        cli()


if __name__ == '__main__':
    main()
