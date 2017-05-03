# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.artist_list import ArtistList
from swagger_server.models.artist_not_found import ArtistNotFound
from swagger_server.models.default_error_response import DefaultErrorResponse
from swagger_server.models.invalid_syntax import InvalidSyntax
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestArtistSuggestionStorageController(BaseTestCase):
    """ ArtistSuggestionStorageController integration test stubs """

    def test_add_artist(self):
        """
        Test case for add_artist

        Add artist to database
        """
        artist_conn = ArtistList()
        response = self.client.open('/v1/{artist_name}'.format(artist_name='artist_name_example'),
                                    method='POST',
                                    data=json.dumps(artist_conn),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_artist(self):
        """
        Test case for delete_artist

        Delete artist from database
        """
        response = self.client.open('/v1/{artist_name}'.format(artist_name='artist_name_example'),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_artist(self):
        """
        Test case for get_artist

        Get stored similar artists list
        """
        response = self.client.open('/v1/{artist_name}'.format(artist_name='artist_name_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_artist(self):
        """
        Test case for update_artist

        Update artist in database
        """
        artist_conn = ArtistList()
        response = self.client.open('/v1/{artist_name}'.format(artist_name='artist_name_example'),
                                    method='PUT',
                                    data=json.dumps(artist_conn),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
