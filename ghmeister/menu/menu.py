from typing import Callable

from ghmeister.commands.github import Repositories, Issues
from ghmeister.commands.github.types.Issue import Issue
from ghmeister.menu.MenuBuilder import MenuBuilder
from ghmeister.menu.issue_menu import issue_menu
from ghmeister.utils import format_data


def issues_list_menu(owner: str, repo: str):
    menu = MenuBuilder(f'{owner}/{repo} | Open Issues')
    issues = Issues.list_repository_issues(owner, repo).json()
    for issue in issues:
        menu.add_choice(format_data(issue), lambda i=issue: issue_menu(Issue.model_validate(i)))
    menu.execute()


def issues_menu(owner: str, repo: str):
    MenuBuilder(f'{owner}/{repo} | Issues', {'List': lambda o=owner, r=repo: issues_list_menu(o, r)}).execute()


def repository_menu(owner: str, repo: str):
    MenuBuilder(f'{owner}/{repo}',
                {'Issues': lambda o=owner, r=repo: issues_menu(o, r)}).execute()


def user_menu(login: str):
    MenuBuilder(login, {'Repositories': lambda: user_repositories_menu(login)}).execute()


def user_repositories_menu(login: str):
    repos = Repositories.user_repos(affiliation='owner').json()
    choices: dict[str, Callable] = {}
    for repo in repos:
        choices[repo['name']] = lambda lgn=login, r=repo['name']: repository_menu(lgn, r)
    MenuBuilder(f'{login} | Repositories', choices).execute()
