from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator


def input_text(message: str, default='', optional=False) -> str:
    if optional:
        return inquirer.text(message=message + ' (optional)', default=default).execute()
    return inquirer.text(message=message, default=default, validate=EmptyInputValidator()).execute()
