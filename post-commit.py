#!/usr/bin/env python

import requests

def get_page(url):
    response = requests.get(url)

    try:
        if response.status_code == 200:
            return response.content
        else:
            return None
    except requests.Timeout as e:
        return str(e)

url = 'http://minimalmaxims.com/'
html = get_page(url)
print(html)
