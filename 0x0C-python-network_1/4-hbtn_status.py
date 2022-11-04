#!/usr/bin/python3
"""
Python script that fetches `https://intranet.hbtn.io/status`.
"""
import requests


if __name__ == "__main__":
    http = requests.get('https://intranet.hbtn.io/status')
    print("""Body response:
\t- type: {}
\t- content: {}"""
          .format(type(http.text), http.text))
