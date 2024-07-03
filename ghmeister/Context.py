import os
import sys

from rich.console import Console
from sh import git, ErrorReturnCode

from ghmeister.auth import load_github_token_from_cache_file, get_config_yml_path


class Context:
    console = Console()
    token: str | None = None
    owner: str | None = None
    repo: str | None = None

    @staticmethod
    def init():
        Context._init_github_api_token()
        Context._init_github_repository_details()

    @staticmethod
    def _init_github_api_token():
        Context.token = os.getenv('GITHUB_MEISTER_TOKEN')
        if not Context.token:
            Context.token = load_github_token_from_cache_file()
        if not Context.token:
            Context.console.print(
                'GitHub access token not found in environment variable GITHUB_MEISTER_TOKEN\n'
                f'or YAML configuration file at {str(get_config_yml_path())}', style="red")
            sys.exit(1)

    @staticmethod
    def _init_github_repository_details():
        try:
            origin: str = git('remote', 'get-url', 'origin')
        except ErrorReturnCode:
            return
        origin = origin.strip()
        if 'github.com' in origin:
            origin = origin.replace('git@github.com:', '')
            origin = origin.replace('.git', '')
            parts = origin.split('/')
            if len(parts) == 2:
                Context.owner = parts[0]
                Context.repo = parts[1]

    @staticmethod
    def get_owner() -> str:
        return Context.owner

    @staticmethod
    def get_repo() -> str:
        return Context.repo
