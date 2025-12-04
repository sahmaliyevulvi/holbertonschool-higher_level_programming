#!/usr/bin/python3
"""
Sends a request to a URL and displays the body.
Handles HTTP errors and prints the error code.
"""

from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = request.Request(url)

    try:
        with request.urlopen(req) as response:
            body = response.read().decode("utf-8")
            print(body)
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
