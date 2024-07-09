from InquirerPy import inquirer

from ghmeister.Context import Context
from ghmeister.commands.github.Repositories import Repositories
from ghmeister.wizard.issues_wizard import issues_wizard
from ghmeister.wizard.wizard_utils import register_shortcut_back


def user_repositories_wizard(login: str):
    # Context.console.print(f'[link=https://www.willmcgugan.com]{repo["full_name"]}[/link] >', style='bold white')

    repos = Repositories.user_repos(affiliation='owner').json()
    choices = [repo['name'] for repo in repos]
    prompt = inquirer.fuzzy(message='Repository:', choices=choices)
    register_shortcut_back(prompt)
    selection = prompt.execute()
    command = selection['command'] if 'command' in selection else 'select'
    if command == 'back':
        return
    elif command == 'select':
        issues_wizard()
