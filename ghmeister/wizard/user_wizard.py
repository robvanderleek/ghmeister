from InquirerPy import inquirer

from ghmeister.Context import Context
from ghmeister.commands.github.Users import get_authenticated_user
from ghmeister.wizard.user_repositories_wizard import user_repositories_wizard


def user_wizard():
    login = get_authenticated_user().json()['login']
    Context.console.print(f'[link=https://www.willmcgugan.com]{login}[/link] >', style='bold white')

    selection = inquirer.select(message='', choices=['Repositories']).execute()

    if selection == 'Repositories':
        user_repositories_wizard(login)
