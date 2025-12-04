#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using requests
and displays the body of the response
"""

import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    response = requests.get(url)
    body = response.text

    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
