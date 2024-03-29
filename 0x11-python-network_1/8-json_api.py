#!/usr/bin/python3
"""
    Python script that takes in a URL and an email address, sends a POST reques
    to the passed URL with the email as a parameter, and finally displays the
    body of the response.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"
    data = ""
    if len(argv) == 2:
        data = {"q": argv[1]}

    res = requests.post(url, data=data)
    try:
        result = res.json()
        if result == {}:
            print("No result")
        else:
            print(f"[{result['id']}] {result['name']}")
    except ValueError:
        print("Not a valid JSON")
