from ghmeister.commands.github.types.Issue import Issue
from ghmeister.commands.github.types.Repository import Repository
from ghmeister.menu.MenuBuilder import MenuBuilder


def issue_menu(repository: Repository, issue: Issue):
    print(f'Issue {issue.number}')
    menu = MenuBuilder([repository, issue])
    # menu = MenuBuilder(f'{owner}/{repo} | Open Issues')
    # issues = Issues.list_repository_issues(owner, repo).json()
    # for issue in issues:
    #     menu.add_choice(format_data(issue), lambda: 1)
    # menu.execute()
