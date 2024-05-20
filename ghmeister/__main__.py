import os
import pprint
import sys

import typer
from dotenv import load_dotenv
from rich import print_json
from rich.console import Console

from ghmeister.services.GitHubService import get_username
from ghmeister.services.github import Users

load_dotenv()

console = Console()

cli = typer.Typer(no_args_is_help=True, add_completion=False, result_callback=pprint.pprint)
cli.add_typer(Users.users, name="users", help="Endpoints for users")

# @cli.command(help="Create a changelog")
# def changelog(repository: str = typer.Argument(help='Full repository name, for example: my-org/my-repo'),
#               from_sha: str = typer.Argument(help='From SHA'),
#               to_sha: str = typer.Argument(help='To SHA')):
#     github = get_github()
#     repo = github.get_repo(repository)
#     comparison = repo.compare(from_sha, to_sha)
#     print(f'## Changelog for {repository}')
#     print(f'### Commits {from_sha}...{to_sha}')
#     commits = comparison.commits
#     for commit in commits:
#         message = commit.commit.message
#         header = message.split('\n')[0]
#         title = header[:72]
#         print(f'- {title}')


@cli.callback(invoke_without_command=False)
def callback(ctx: typer.Context):
    """GH Meister: GitHub management made easy."""
    if ctx.invoked_subcommand:
        print('Running subcommand')
    else:
        print('Running default')


def main():
    token = os.getenv('GITHUB_MEISTER_TOKEN')
    if not token:
        console.print('[red]GitHub access token not found in environment variable GITHUB_MEISTER_TOKEN[/red]')
        sys.exit(1)
    if len(sys.argv) == 1:
        print(get_username())
    else:
        cli()


if __name__ == '__main__':
    main()
