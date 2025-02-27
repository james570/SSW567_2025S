import requests

def get_github_repos_commits(user_id):
    repos_url = f"https://api.github.com/users/{user_id}/repos"
    repos_response = requests.get(repos_url)

    if repos_response.status_code != 200:
        return f"Error: Unable to fetch repositories for user {user_id}"

    repos = repos_response.json()
    result = []

    for repo in repos:
        repo_name = repo['name']
        commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        commits_response = requests.get(commits_url)

        if commits_response.status_code != 200:
            commit_count = "Unknown"
        else:
            commit_count = len(commits_response.json())

        result.append((repo_name, commit_count))

    return result

# 測試
if __name__ == "__main__":
    user = "richkempinski"
    print(get_github_repos_commits(user))
