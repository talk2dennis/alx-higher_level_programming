#!/usr/bin/python3
"""
    a Python script that fetches https://alx-intranet.hbtn.io/status
    use the package requests
"""

if __name__ == '__main__':
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    html = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(html.text)}")
    print(f"\t- content: {html.text}")
    print(f"\t- utf8 content: {html.text}")
