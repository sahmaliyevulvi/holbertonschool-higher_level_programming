#!/usr/bin/python3
"""
Takes GitHub credentials and displays the user id
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]  # personal access token

    url = "https://api.github.com/user"
    try:
        response = requests.get(url, auth=(username, token))
        data = response.json()
        print(data.get("id"))
    except Exception:
        print(None)
