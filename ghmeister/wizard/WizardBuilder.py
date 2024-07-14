from typing import Callable

from InquirerPy import inquirer

from ghmeister.wizard.wizard_utils import register_shortcut_back


class WizardBuilder:
    def __init__(self, title: str, choices: dict[str, Callable]):
        self.title = title
        self.choices = choices

    def execute(self):
        while True:
            print(self.title.center(80))
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
