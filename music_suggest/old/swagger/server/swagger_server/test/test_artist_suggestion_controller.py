# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.artist_list import ArtistList
from swagger_server.models.artist_not_found import ArtistNotFound
from swagger_server.models.default_error_response import DefaultErrorResponse
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestArtistSuggestionController(BaseTestCase):
    """ ArtistSuggestionController integration test stubs """

    def test_get_suggestion(self):
        """
        Test case for get_suggestion

        Get similar artists list
        """
        response = self.client.open('/v1/{artist_name}',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
