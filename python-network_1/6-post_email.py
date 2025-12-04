#!/usr/bin/python3
"""
Takes a URL and an email, sends a POST request with the email,
and displays the body of the response
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # POST sorğusu üçün data dictionary
    data = {"email": email}

    # POST sorğusunu göndər
    response = requests.post(url, data=data)

    # Cavabı ekrana çıxar
    print(response.text)
