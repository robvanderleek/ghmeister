from typing import Callable

from ghmeister.commands.github.Repositories import Repositories
from ghmeister.wizard.WizardBuilder import WizardBuilder


def issues_wizard(owner: str, repo: str):
    WizardBuilder(f'{owner}/{repo} | Issues', {'List': lambda: 1}).execute()


def repository_wizard(owner: str, repo: str):
    WizardBuilder(f'{owner}/{repo}',
                  {'Issues': lambda o=owner, r=repo: issues_wizard(o, r)}).execute()


def user_repositories_wizard(login: str):
    repos = Repositories.user_repos(affiliation='owner').json()
    choices: dict[str, Callable] = {}
    for repo in repos:
        choices[repo['name']] = lambda lgn=login, r=repo['name']: repository_wizard(lgn, r)
    print(choices)
    WizardBuilder(f'{login} | Repositories', choices).execute()


def user_wizard(login: str):
    WizardBuilder(login, {'Repositories': lambda: user_repositories_wizard(login)}).execute()
