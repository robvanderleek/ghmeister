import requests

from ghmeister.Context import Context

BASE_URL = 'https://api.github.com'


def api_get(endpoint: str) -> dict:
    return requests.get(f'{BASE_URL}/{endpoint}', headers=_get_headers()).json()


def api_post(endpoint: str, data: dict) -> dict:
    print(endpoint, data)
    return requests.post(f'{BASE_URL}/{endpoint}', json=data, headers=_get_headers()).json()


def _get_headers() -> dict:
    return {'Accept': 'application/vnd.github+json', 'Authorization': f'Bearer {Context.token}',
            'X-GitHub-Api-Version': '2022-11-28'}
