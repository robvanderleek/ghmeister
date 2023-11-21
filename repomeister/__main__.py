import typer
from github import Auth, Github

from repomeister.auth import get_github_token

cli = typer.Typer(no_args_is_help=True, add_completion=False)


@cli.command(help="Create a changelog")
def changelog(repository: str = typer.Argument(help='Full repository name, for example: my-org/my-repo'),
              from_sha: str = typer.Argument(help='From SHA'),
              to_sha: str = typer.Argument(help='To SHA')):
    token = get_github_token()
    auth = Auth.Token(token['access_token'])
    github = Github(auth=auth)
    repo = github.get_repo(repository)
    comparison = repo.compare(from_sha, to_sha)
    print(f'## Changelog for {repository}')
    print(f'### Commits {from_sha}...{to_sha}')
    commits = comparison.commits
    for commit in commits:
        message = commit.commit.message
        header = message.split('\n')[0]
        title = header[:72]
        print(f'- {title}')


@cli.callback()
def main():
    """Repo Meister: GitHub Repository Manager."""
    pass


if __name__ == '__main__':
    cli()
