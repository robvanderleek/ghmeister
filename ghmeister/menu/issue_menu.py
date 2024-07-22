from ghmeister.commands.github import Issues
from ghmeister.commands.github.types.Issue import Issue
from ghmeister.commands.github.types.Repository import Repository
from ghmeister.menu.MenuBuilder import MenuBuilder
from ghmeister.utils import fmt_short


def issue_menu(repository: Repository, issue: Issue):
    menu = MenuBuilder([fmt_short(repository), fmt_short(issue)])
    menu.add_choice('Lock', lambda r=repository, i=issue: Issues.lock(r.owner.login, r.name, i.number))
    # menu = MenuBuilder(f'{owner}/{repo} | Open Issues')
    # issues = Issues.list_repository_issues(owner, repo).json()
    # for issue in issues:
    #     menu.add_choice(format_data(issue), lambda: 1)
    menu.execute()
