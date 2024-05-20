import os

import requests

github = None


def _get_github_token() -> str:
    token = os.environ['GITHUB_MEISTER_TOKEN']
    if not token:
        raise Exception('No GitHub access token found in environment')
    return token


def get_user() -> dict:
    token = _get_github_token()
    res = requests.get('https://api.github.com/user', headers={'Authorization': f'Bearer {token}'})
    return res.json()


def get_username() -> str:
    return get_user()['login']


def get_avatar():
    return get_user()['avatar_url']
