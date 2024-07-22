from typing import Callable

from ghmeister.commands.github import Repositories, Issues
from ghmeister.commands.github.types.Repository import Repository
from ghmeister.menu.MenuBuilder import MenuBuilder
from ghmeister.menu.issue_menu import issue_menu
from ghmeister.utils import fmt_oneline, fmt_short


def issues_list_menu(repository: Repository):
    menu = MenuBuilder([fmt_short(repository), 'Open Issues'])
    issues = Issues.list_repository_issues(repository.owner.login, repository.name)
    for issue in issues:
        menu.add_choice(fmt_oneline(issue), lambda r=repository, i=issue: issue_menu(r, i))
    menu.execute()


def issues_menu(repository: Repository):
    MenuBuilder([fmt_short(repository), 'Issues'],
                {'List': lambda r=repository: issues_list_menu(r)}).execute()


def repository_menu(repository: Repository):
    MenuBuilder(fmt_short(repository), {'Issues': lambda r=repository: issues_menu(r)}).execute()


def user_menu(login: str):
    MenuBuilder(login, {'Repositories': lambda: user_repositories_menu(login)}).execute()


def user_repositories_menu(login: str):
    repos = Repositories.user_repos(affiliation='owner').json()
    choices: dict[str, Callable] = {}
    for repo in repos:
        choices[repo['name']] = lambda lgn=login, r=repo['name']: repository_menu(lgn, r)
    MenuBuilder(f'{login} | Repositories', choices).execute()
