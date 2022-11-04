#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a
`POST` request to the passed URL with the email as
a parameter, and displays the body of the response
(decoded in `utf-8`)."""
from urllib import request, parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = parse.urlencode(value).encode('utf-8')
    http = request.Request(url, data)
    with request.urlopen(http) as response:
        print(response.read().decode('utf-8'))
