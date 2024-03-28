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
    data = {"email": argv[2]}

    res = requests.post(url, data=data)
    print(res.text)
