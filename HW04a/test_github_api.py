import unittest
from unittest.mock import patch

from HW04a.github_api import get_github_repos_commits

class TestGitHubAPI(unittest.TestCase):

    @patch("requests.get")
    def test_valid_user(self, mock_get):
        mock_get.side_effect = [
            MockResponse([{"name": "Repo1"}, {"name": "Repo2"}], 200),
            MockResponse([{}, {}, {}], 200),
            MockResponse([{}, {}, {}, {}], 200),
        ]

        expected_output = [("Repo1", 3), ("Repo2", 4)]
        self.assertEqual(get_github_repos_commits("validuser"), expected_output)

    @patch("requests.get")
    def test_invalid_user(self, mock_get):
        mock_get.return_value = MockResponse(None, 404)
        self.assertEqual(get_github_repos_commits("invaliduser"), "Error: Unable to fetch repositories for user invaliduser")

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

#test
if __name__ == '__main__':
    unittest.main()