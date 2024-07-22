from typing import Callable

from InquirerPy import inquirer

from ghmeister.Context import Context
from ghmeister.menu.menu_utils import register_shortcut_back


class MenuBuilder:
    def __init__(self, breadcrumbs: str | list[str], choices: dict[str, Callable] | None = None):
        self.breadcrumbs = breadcrumbs if isinstance(breadcrumbs, list) else [breadcrumbs]
        self.breadcrumbs[-1] = f'[bold]{self.breadcrumbs[-1]}[/bold]'
        self.choices: dict[str, Callable] = choices if choices else {}

    def add_choice(self, key: str, value: Callable):
        self.choices[key] = value

    def execute(self):
        while True:
            title = ' | '.join(self.breadcrumbs)
            Context.console.print(title.center(80))
            prompt = inquirer.select(
                message='Select:',
                choices=[str(k) for k in self.choices.keys()],
                long_instruction='[enter]:Select, [o]rgs',
                mandatory=False,
                raise_keyboard_interrupt=False
            )
            register_shortcut_back(prompt)
            selection = prompt.execute()
            if not selection:
                break
            command = selection['command'] if 'command' in selection else 'select'
            if command == 'back':
                break
            if command == 'select':
                self.choices[selection]()
