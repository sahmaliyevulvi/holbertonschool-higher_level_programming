#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status using urllib
"""

from urllib import request

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = request.Request(url, headers={'cfclearance': 'true'})

    with request.urlopen(req) as response:
        body = response.read()

        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
