from InquirerPy import inquirer

from ghmeister.Context import Context
from ghmeister.commands.github.Repositories import Repositories


def issues_wizard():
    repo = Repositories.get(Context.get_owner(), Context.get_repo()).json()

    Context.console.print(f'[link=https://www.willmcgugan.com]{repo["full_name"]}[/link] >', style='bold white')

    selection = inquirer.select(message='', choices=['Issues', 'Pull Requests']).execute()
