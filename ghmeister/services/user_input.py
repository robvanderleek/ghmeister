from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator


def input_text(message: str, default='') -> str:
    return inquirer.text(message=message, default=default, validate=EmptyInputValidator()).execute()
