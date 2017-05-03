#! /usr/local/bin/python3

import requests
import json
import re
from bs4 import BeautifulSoup
from url_encoder import URLEncoder

BASE_URL = 'https://www.music-map.com/'
SEARCH_PAT = re.compile('Aid\[0\]=new Array\((.*?)\)')

encoder = URLEncoder()
url_extension = encoder.encode('Simon & Garfunkel')
web_r = requests.get(BASE_URL+url_extension)
if web_r.status_code != 200:
    print('Error '+web_r.status_code)
soup = BeautifulSoup(web_r.text, 'lxml')
scripts = soup.find_all('script')
artists = soup.find_all('a', 'S')

def test():
    for item in scripts:
    #        print(item.string)
        if item.string is not None:
            match = re.search(SEARCH_PAT, item.string)
            if match is not None:
                result_list = [float(x) for x in match.groups()[0].split(',')]
                print(result_list)

def test2():
    for item in artists:
        if item.string is not None:
            print(item.string)

if __name__ == '__main__':
    test()
    test2()
