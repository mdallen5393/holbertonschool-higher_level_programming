#!/usr/bin/python3
"""
Script that fetches `https://intranet.hbtn.io/status`.
"""
if __name__ == "__main__":
    from urllib import request
    req = request.Request('https://intranet.hbtn.io/status')
    with request.urlopen(req) as response:
        html = response.read()
    print("""Body response:
    - type: {}
    - content: {}
    - utf8 content: {}"""
          .format(type(html), html, html.decode('utf8')))
