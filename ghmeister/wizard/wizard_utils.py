from InquirerPy.prompts import ListPrompt


def register_shortcut_back(prompt: ListPrompt):
    _register_shortcut(prompt, 'left', 'back')


def _register_shortcut(prompt: ListPrompt, key: str, command: str, enable=True):
    @prompt.register_kb(key, filter=enable)
    def _(event):
        event.app.exit(result={'value': prompt.result_value, 'command': command})
