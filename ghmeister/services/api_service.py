import requests
from requests import Response

from ghmeister.Context import Context

BASE_URL = 'https://api.github.com'


def api_get(endpoint: str) -> Response:
    response = requests.get(f'{BASE_URL}/{endpoint}', headers=_get_headers())
    response.raise_for_status()
    return response


def api_post(endpoint: str, data: dict) -> Response:
    response = requests.post(f'{BASE_URL}/{endpoint}', json=data, headers=_get_headers())
    response.raise_for_status()
    return response


def _get_headers() -> dict:
    return {'Accept': 'application/vnd.github+json', 'Authorization': f'Bearer {Context.token}',
            'X-GitHub-Api-Version': '2022-11-28'}
