#!/usr/bin/python3
"""
Takes a letter and sends a POST request to search_user
Displays the id and name if JSON is valid and not empty
"""

import requests
import sys

if __name__ == "__main__":
    # Komanda sətrindən arqument götür, əgər yoxdursa q=""
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    try:
        response = requests.post(url, data=data)
        result = response.json()  # JSON cavabını dict-ə çevir

        if result:
            print(f"[{result.get('id')}] {result.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
