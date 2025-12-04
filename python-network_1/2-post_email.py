#!/usr/bin/python3
"""
Sends a POST request with an email and displays the UTF-8 response
"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # POST üçün göndəriləcək məlumat (dict formatında)
    data = {"email": email}

    # Məlumatı urlencode edib bytes-a çeviririk
    data = parse.urlencode(data).encode("utf-8")

    # POST sorğusu yaratmaq
    req = request.Request(url, data=data)

    # Sorğu göndərmək və cavabı almaq
    with request.urlopen(req) as response:
        body = response.read().decode("utf-8")
        print(body)
