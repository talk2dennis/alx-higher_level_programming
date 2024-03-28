#!/usr/bin/python3
"""
    a Python script that fetches https://alx-intranet.hbtn.io/status
    use the package urllib
"""

if __name__ == '__main__':
    import urllib.request
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print(f"\t- {type(html)}")
        print(f"\t- {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")

