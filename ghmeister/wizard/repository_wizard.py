from InquirerPy import inquirer

from ghmeister.Context import Context
from ghmeister.commands.github.Repositories import Repositories
from ghmeister.wizard.issues_wizard import issues_wizard
from ghmeister.wizard.user_wizard import user_wizard
from ghmeister.wizard.wizard_utils import register_shortcut_back


def repository_wizard():
    repo = Repositories.get(Context.get_owner(), Context.get_repo()).json()

    Context.console.print(f'[link=https://www.willmcgugan.com]{repo["full_name"]}[/link] >', style='bold white')

    prompt = inquirer.select(message='Select:', choices=['Issues', 'Pull Requests'])
    register_shortcut_back(prompt)
    selection = prompt.execute()
    command = selection['command'] if 'command' in selection else 'select'
    if command == 'back':
        user_wizard()
    elif command == 'select':
        issues_wizard()
