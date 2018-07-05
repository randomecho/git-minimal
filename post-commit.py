#!/usr/bin/env python3

from bs4 import BeautifulSoup
from textwrap import wrap
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

def get_extract(raw_html, html_tag, css_class):
    html = BeautifulSoup(raw_html, 'html.parser')
    extract = html.find(html_tag, attrs={'class': css_class})

    if extract is not None:
        return extract.text.strip()
    else:
        return None

def display_quote(quote, author):
    if quote is not None and author is not None:
        print()
        print("\n".join(wrap(quote, 70)))
        print(('{0:>70}').format(author))
        print()

url = 'http://minimalmaxims.com/'
html = get_page(url)

if html is not None:
    quote = get_extract(html, 'span', 'quotable-quote')
    author = get_extract(html, 'cite', 'quoteable-author')
    display_quote(quote, author)
