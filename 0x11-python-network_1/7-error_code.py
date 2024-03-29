#!/usr/bin/python3
"""
    Python script that takes in a URL and an email address, sends a POST reques
    to the passed URL with the email as a parameter, and finally displays the
    body of the response.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]

    res = requests.get(url)
    if res.status_code >= 400:
        print(f"Error code: {res.status_code}")
    else:
        print(res.text)
