#!/usr/bin/python3
"""
    a Python script that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id
"""

if __name__ == '__main__':
    from sys import argv
    import urllib.request
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as res:
        print(f"{res.headers['X-Request-Id']}")
