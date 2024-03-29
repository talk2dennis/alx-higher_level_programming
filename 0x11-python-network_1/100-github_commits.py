#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
Usuage: ./10-my_github.py username PAT
"""

if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"

    res = requests.get(url)
    result = res.json()
    for repo in result:
        sha = repo.get("sha")
        author = repo.get("commit").get("author").get("name")
        print(f"{sha}: {author}")
