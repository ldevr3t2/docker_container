import connexion
from swagger_server.models.artist_list import ArtistList
from swagger_server.models.artist_not_found import ArtistNotFound
from swagger_server.models.default_error_response import DefaultErrorResponse
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_suggestion(artist_name):
    """
    Get similar artists list
    
    :param artist_name: Artist to be searched
    :type artist_name: str

    :rtype: ArtistList
    """
    return 'do some magic!'
