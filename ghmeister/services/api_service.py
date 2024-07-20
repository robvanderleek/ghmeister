import requests
from requests import Response

from ghmeister.Context import Context

BASE_URL = 'https://api.github.com'


def api_delete(endpoint: str) -> Response:
    response = requests.delete(f'{BASE_URL}/{endpoint}', headers=_get_headers())
    response.raise_for_status()
    return response


def api_get(endpoint: str, params: dict[str, any] | None = None) -> Response:
    response = requests.get(f'{BASE_URL}/{endpoint}', headers=_get_headers(), params=params)
    response.raise_for_status()
    return response


def api_post(endpoint: str, data: dict) -> Response:
    data = {k: v for k, v in data.items() if v is not None}
    response = requests.post(f'{BASE_URL}/{endpoint}', json=data, headers=_get_headers())
    response.raise_for_status()
    return response


def api_put(endpoint: str, data: dict) -> Response:
    data = {k: v for k, v in data.items() if v is not None}
    response = requests.put(f'{BASE_URL}/{endpoint}', json=data, headers=_get_headers())
    response.raise_for_status()
    return response


def _get_headers() -> dict:
    return {'Accept': 'application/vnd.github+json', 'Authorization': f'Bearer {Context.token}',
            'X-GitHub-Api-Version': '2022-11-28'}
