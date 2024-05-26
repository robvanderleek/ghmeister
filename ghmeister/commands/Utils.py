import typer

utils = typer.Typer(no_args_is_help=True)

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
