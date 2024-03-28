#!/usr/bin/python3
"""
    a Python script that fetches https://alx-intranet.hbtn.io/status
    use the package requests
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    res = requests.get(url)
    print(res.headers['X-Request-Id'])
