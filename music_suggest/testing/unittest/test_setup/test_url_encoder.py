#! /usr/local/bin/python3
# coding: utf-8

from url_encoder import URLEncoder
import unittest

class TestUrlEncoderMethods(unittest.TestCase):
    test_values = (('test', 'test'),
                   ('test test', 'test+test'),
                   ('test/test', 'test-2ftest'),
                   ('Test', 'test'),
                   ('TEST', 'test'),
                   ('Guns\'N\'Roses', 'guns-27n-27roses'),
                   ('AC/DC', 'ac-2fdc'),
                   ('Denmark + Winter', 'denmark+-2b+winter'),
                   ('Lost Frequencies Feat. Janieck Devy',
                    'lost+frequencies+feat.+janieck+devy'),
                   ('*Nsync', '-2ansync'))

    def test_string_to_url(self):
        print('\nConverting artist name strings to urls')
        print('*** string => url ***')
        test = URLEncoder()
        for string, url in self.test_values:
            self.assertEqual(test.encode(string), url)
            print(string+' => '+url)

    def test_for_unwanted_url_mutations(self):
        print('\nTrying to reencode the urls to')
        print('check for unwanted mutations')
        print('*** url => url ***')
        test = URLEncoder()
        for string, url in self.test_values:
            self.assertEqual(test.encode(url), url)
            print(url+' => '+url)

    def test_url_to_string(self):
        print('\nConverting urls back to strings')
        print('*** url => string ***')
        test = URLEncoder()
        for string, url in self.test_values:
            self.assertEqual(test.decode(url), string.lower())
            print(url+' => '+string)


if __name__ == '__main__':
    unittest.main()
