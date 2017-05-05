import connexion
from swagger_server.models.artist_list import ArtistList
from swagger_server.models.artist_not_found import ArtistNotFound
from swagger_server.models.default_error_response import DefaultErrorResponse
from swagger_server.models.invalid_syntax import InvalidSyntax
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

from pymongo.errors import DuplicateKeyError
from pymongo import MongoClient 

# Local MongoDB client
# client = MongoClient('localhost', 27017)

# Dockerized MongoDB client
client = MongoClient('reco-storage-router', 27017)

# Set up MongoDB database
db = client['artist_db']

# Set up MongoDB collection
collec = db['artist_tree']


def add_artist(artist_name, artist_conn=None):
    """
    Add artist to database
    
    :param artist_name: Artist to add
    :type artist_name: str
    :param artist_conn: Added artist's connections
    :type artist_conn: dict | bytes

    :rtype: None
    """
    try:
        if connexion.request.is_json:
            artist_conn = ArtistList.from_dict(connexion.request.get_json())
        else:
            raise ValueError()

    except ValueError as e:
        return InvalidSyntax('invalid_JSON', 'Invalid JSON object'), 400

    db_data = artist_conn.to_dict()
    db_data['_id'] = artist_name

    try:
        collec.insert_one(db_data)
    except DuplicateKeyError as e:
        return "Artist exists; use POST", 303

    return 'Success', 200


def delete_artist(artist_name):
    """
    Delete artist from database
    
    :param artist_name: Artist to delete
    :type artist_name: str

    :rtype: None
    """
    del_count = collec.delete_one({'_id': artist_name}).deleted_count

    if del_count:
        return 'Success', 200
    else:
        return ArtistNotFound('artist_name',
            'Unable to delete; this artist is not in the database'), 404


def get_artist(artist_name):
    """
    Get stored similar artists list
    
    :param artist_name: Requested artist
    :type artist_name: str

    :rtype: ArtistList
    """
    result = collec.find_one({'_id': artist_name})
    if result:
        return ArtistList.from_dict(result)
    else:
        return ArtistNotFound('artist_name',
            'Unable to retrieve; this artist is not in the database'), 404



def update_artist(artist_name, artist_conn):
    """
    Update artist in database
    
    :param artist_name: Artist to add
    :type artist_name: str
    :param artist_conn: Updated artist&#39;s connections
    :type artist_conn: dict | bytes

    :rtype: None
    """

    try:
        if connexion.request.is_json:
            artist_conn = ArtistList.from_dict(connexion.request.get_json())
        else:
            raise ValueError()
    except ValueError:
        return InvalidSyntax('invalid_JSON', 'Invalid JSON object'), 400


    upd_count = collec.replace_one({'_id': artist_name},
                                    artist_conn.to_dict()).matched_count

    if upd_count:
        return 'Success', 200
    else:
        return ArtistNotFound('artist_name',
            'Unable to update; this artist is not in the database'), 404

