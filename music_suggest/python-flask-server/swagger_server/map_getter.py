#! /usr/bin/python3
# coding: utf-8

import requests
import json
import re
from bs4 import BeautifulSoup
from swagger_server.models.artist import Artist
from swagger_server.models.artist_list import ArtistList
#from url_encoder import URLEncoder

class MapGetter():
    """
    MapGetter class sends requests to music map
    website and parses the response
    The returned data features a list of suggested artists
    with their respected scores
    """
    __base_url = 'https://www.music-map.com/'
    __artist_pat = re.compile(r'Aid\[0\]=new Array\((.*?)\)')
    __storage_url = 'http://reco-storage-web:8080/v1/artist='

    def __init__(self):
        """
        MapGetter - sends request to music map, returns processed
        results
        """
        # initialize some of the variables here

    @classmethod
    def retrieve_artist_by_url(cls, artist_url):
        try:
            request = requests.get(cls.__storage_url+artist_url, timeout=1)
        except requests.exceptions.Timeout:
            artist_list = cls.__get_from_music_map(cls, artist_url)
            cls.__post_data_to_storage(cls, artist_url, artist_list)
            return artist_list

        if request.status_code != 200:
            print('Error: Failed to retrieve suggestions for '+artist_url)
            print('Status Code: '+str(request.status_code))
            artist_list = cls.__get_from_music_map(cls, artist_url)
            cls.__post_data_to_storage(cls, artist_url, artist_list)
            return artist_list
        return request.text

    def __get_from_music_map(self, artist_url):
        try:
            request = requests.get(self.__base_url+artist_url, timeout=1)
        except requests.exceptions.Timeout:
            return []

        if request.status_code != 200:
            print('Error: Failed to retrieve suggestions for '+artist_url)
            print('Status Code: '+str(request.status_code))
            return []
        soup = BeautifulSoup(request.text, 'lxml')
        artist_names = self.get_artists_from_soup(soup)
        artist_scores = self.get_scores_from_soup(soup, self.__artist_pat)
        return list(zip(artist_names, artist_scores))

    def __post_data_to_storage(self, artist_url, data):
        try:
            request = requests.post(self.__storage_url+artist_url, json=self.artists_json(data), timeout=1)
            print('Posting to storage')
            print(request.status_code)
            print(request.text)
        except requests.exceptions.Timeout:
            print('Post to storage failed')

    @staticmethod
    def get_artists_from_soup(soup):
        # in the html we receive artists are inside <a> tag
        # and designated to "S" class
        artists = soup.find_all('a', 'S')
        artist_names = [item.string for item in artists]
        return artist_names

    @staticmethod
    def get_scores_from_soup(soup, re_pattern):
        # getting scores if a bit more difficult
        # first parse all of the javascript objects
        scripts = soup.find_all('script')
        for item in scripts:
            if item.string is not None:
                match = re.search(re_pattern, item.string)
                if match is not None:
                    artist_scores = [float(x) for x in match.groups()[0].split(',')]
                    return artist_scores
        return []

    @staticmethod
    def artists_json(data):
        return ArtistList([Artist(name, score)
                           for name, score in data]).to_dict()
