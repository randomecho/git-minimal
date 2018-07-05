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

def get_quote(raw_html):
    html = BeautifulSoup(raw_html, 'html.parser')
    quote = html.find('span', attrs={'class': 'quotable-quote'})

    if quote is not None:
        return quote.text.strip()
    else:
        return None

def get_author(raw_html):
    html = BeautifulSoup(raw_html, 'html.parser')
    author = html.find('cite', attrs={'class': 'quoteable-author'})

    if author is not None:
        return author.text.strip()
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
    quote = get_quote(html)
    author = get_author(html)
    display_quote(quote, author)
