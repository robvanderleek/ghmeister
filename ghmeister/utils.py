from ghmeister.Context import Context


def pretty_print_json(data: dict):
    Context.console.print_json(data=data)


def pretty_print(data: dict | list):
    if isinstance(data, list):
        for item in data:
            pretty_print_item(item)
    else:
        pretty_print_item(data)


def pretty_print_item(item: dict):
    node_id = item['node_id'] if 'node_id' in item else None
    if not node_id:
        Context.console.print_json(data=item)
    else:
        if node_id.startswith('I_'):
            print(f'{item["number"]}: {item["title"]}')
        else:
            print(f'{node_id}')
