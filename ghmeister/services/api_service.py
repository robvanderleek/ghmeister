from typing import TypeVar, get_args, Type, get_origin

import requests
from pydantic import BaseModel
from requests import Response

from ghmeister.Context import Context

BASE_URL = 'https://api.github.com'

T = TypeVar('T', bound=BaseModel)


def api_delete(endpoint: str) -> Response:
    response = requests.delete(f'{BASE_URL}/{endpoint}', headers=_get_headers())
    response.raise_for_status()
    return response


def api_get(endpoint: str, params: dict[str, any] | None = None, response_model: type[T | list[T] | None] = None) \
        -> T | list[T] | dict:
    response = requests.get(f'{BASE_URL}/{endpoint}', headers=_get_headers(), params=params)
    response.raise_for_status()
    if response_model:
        if get_origin(response_model) == list:
            m = get_args(response_model)[0]
        else:
            m = response_model
        json = response.json()
        if isinstance(json, list):
            return [m.model_validate(item) for item in json]
        else:
            return m.model_validate(response.json())
    else:
        return response.json()


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
