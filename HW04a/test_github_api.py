import unittest
from unittest.mock import patch
from HW04a.github_api import get_github_repos_commits


class TestGitHubAPI(unittest.TestCase):
    @patch('HW04a.github_api.requests.get')
    def test_get_github_repos_commits(self, mock_get):
        mock_get.side_effect = [
            unittest.mock.Mock(status_code=200, json=lambda: [
                {'name': 'repo1'}, {'name': 'repo2'}
            ]),
            unittest.mock.Mock(status_code=200, json=lambda: [{'commit': 'Commit A'}, {'commit': 'Commit B'}]),
            unittest.mock.Mock(status_code=200, json=lambda: [{'commit': 'Commit X'}])
        ]

        commits = get_github_repos_commits("test_user")

        self.assertEqual(commits, [('repo1', 2), ('repo2', 1)])


if __name__ == '__main__':
    unittest.main()
