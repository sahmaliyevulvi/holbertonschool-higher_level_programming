#!/usr/bin/python3
"""
Script that takes a URL, sends a request and displays X-Request-Id header
"""

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = request.Request(url, headers={'cfclearance': 'true'})

    with request.urlopen(req) as response:
        headers = response.headers
        print(headers.get("X-Request-Id"))
