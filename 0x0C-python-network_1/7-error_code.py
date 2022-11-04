#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    http = requests.get(url)
    if http.status_code >= 400:
        print("Error code: {}".format(http.status_code))
    else:
        print(http.text)
