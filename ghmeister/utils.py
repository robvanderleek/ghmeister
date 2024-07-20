import json

from ghmeister.Context import Context


def pretty_print_json(data: dict):
    Context.console.print_json(data=data)


def format_data(data: dict | list) -> str:
    if isinstance(data, list):
        result = ''
        for item in data:
            result += format_item(item) + '\n'
        return result
    else:
        return format_item(data)


def format_item(item: dict) -> str:
    node_id = item['node_id'] if 'node_id' in item else None
    if not node_id:
        return json.dumps(item)[:80]
    else:
        if node_id.startswith('I_'):
            return f'{item["number"]}: {item["title"]}'[:80]
        else:
            return f'{node_id}'[:80]
