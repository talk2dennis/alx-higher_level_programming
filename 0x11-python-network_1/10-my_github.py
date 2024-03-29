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

    uname = argv[1]
    pwd = argv[2]
    basic = HTTPBasicAuth(uname, pwd)
    url = f"https://api.github.com/users/{uname}"

    res = requests.get(url, auth=basic)
    print(res.text)

    try:
        result = res.json()
        if result == {}:
            print("None")
        else:
            print(f"{result['id']}")
    except ValueError:
        print("None")
