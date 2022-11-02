#!/usr/bin/python3
"""
Script that fetches `https://intranet.hbtn.io/status`.
"""
from urllib import request


if __name__ == "__main__":
    req = request.Request('https://intranet.hbtn.io/status')
    with request.urlopen(req) as response:
        html = response.read()
        print("""Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}"""
            .format(type(html), html, html.decode('utf8')))
