#!/usr/bin/python3
"""
    Python script that takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the
        body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    from sys import argv
    from urllib import error, request
    

    url = argv[1]
    try:
        with request.urlopen(uril) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
