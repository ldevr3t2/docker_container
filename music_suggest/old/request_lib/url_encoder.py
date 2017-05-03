#! /usr/bin/python3
# coding: utf-8

from urllib.parse import quote_plus, quote
from urllib.parse import unquote_plus, unquote

# URL encoder class
class URLEncoder():
    """
    URLEncoder class is meant for translating strings into appropriate
    url extensions
    In case of suggestion service, artist name is encoded so it can be
    used to query music map service
    """
    def __init__(self):
        """
        URLEncoder - basic encoder class to translate strings
        into url extensions, ex. 'Led Zeppelin' => 'led+zeppelin'
        """
        # these characters require special attention, ex. '/' in 'ac/dc'

    @classmethod
    def encode(cls, str_to_encode):
        """
        Returns string that represents encoded url

        :param s: Python string
        :type: str
        :return: Encoded Url
        :rtype: str
        """
        temp = ''
        if '+' in str_to_encode and ' ' not in str_to_encode:
            temp = quote(str_to_encode.lower(), safe='+-')
        else:
            temp = quote_plus(str_to_encode.lower(), safe='-')

        if '%' in temp:
            temp = temp.replace('%', '-')

        return temp.lower()

    @classmethod
    def decode(cls, str_to_decode):
        """
        Returns string that represents dencoded url

        :param s: Python string
        :type: str
        :return: Result String
        :rtype: str
        """
        temp = str_to_decode
        if '-' in str_to_decode:
            temp = temp.replace('-', '%')
        temp = unquote_plus(temp)
        return temp
