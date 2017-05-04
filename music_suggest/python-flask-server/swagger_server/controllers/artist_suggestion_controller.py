import connexion
import json
import urllib
from swagger_server.models.artist import Artist
from swagger_server.models.artist_list import ArtistList
from swagger_server.models.artist_not_found import ArtistNotFound
from swagger_server.models.default_error_response import DefaultErrorResponse
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from swagger_server.url_encoder import URLEncoder
from swagger_server.map_getter import MapGetter

def get_suggestion(artist_name):
    """
    Get similar artists list

    :param artist_name: Artist to be searched
    :type artist_name: str

    :rtype: ArtistList
    """
    encoder = URLEncoder()
    temp = encoder.encode(artist_name)
    if temp == 'test':
        a1 = Artist('test artist1', -1)
        a2 = Artist('test artist2', 1.45)
        return ArtistList([a1, a2])
    else:
        music_map = MapGetter()
        artist_score_list = music_map.retrieve_artist_by_url(temp)
        if not artist_score_list:
            return ArtistNotFound('404', 'Artist '+artist_name+' not found')
        
        return ArtistList([Artist(entry['name'], entry['score'])
                          for entry in artist_score_list['artists']])
