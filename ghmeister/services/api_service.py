import os

from ghmeister.services.github.endpoints.Users import get_authenticated_user

github = None


def _get_github_token() -> str:
    token = os.getenv('GITHUB_MEISTER_TOKEN')
    if not token:
        raise Exception('No GitHub access token found in environment')
    return token


def get_username() -> str:
    return get_authenticated_user()['login']


def get_avatar():
    return get_authenticated_user()['avatar_url']
