from unittest.mock import patch

from ghmeister.commands.github import Repositories


@patch('ghmeister.commands.github.Repositories.api_get')
def test_get(mock_api_get):
    Repositories.get('robvanderleek', 'ghmeister')

    mock_api_get.assert_called_once_with('repos/robvanderleek/ghmeister')
