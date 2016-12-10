# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest

import media


class MediaTests(unittest.TestCase):

    def setUp(self):
        self.movie = media.Movie({'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/f/f9/The_Lincoln_Lawyer_Poster.jpg',
                                    'year': '2011',
                                    'storyline': 'Mick Haller is a defense lawyer who works out of his Lincoln.',
                                    'youtube_trailer_url': 'https://www.youtube.com/watch?v=IFwE3UgCMIk', 
                                    'title': 'The Lincoln Lawyer'})

    def test_movie_class_exits(self):
        self.assertTrue(self.movie)

    def test_movie_has_title(self):
        self.assertEqual('The Lincoln Lawyer', self.movie.title)
        
    def test_movie_has_year(self):
        self.assertEqual('2011', self.movie.year)
        
    def test_movie_has_storyline(self):
        self.assertEqual('Mick Haller is a defense lawyer who works out of his Lincoln.', self.movie.storyline)
        
    def test_movie_has_poster_image_url(self):
        self.assertEqual('https://upload.wikimedia.org/wikipedia/en/f/f9/The_Lincoln_Lawyer_Poster.jpg', self.movie.poster_image_url)
        
    def test_movie_has_youtube_trailer_url(self):
        self.assertEqual('https://www.youtube.com/watch?v=IFwE3UgCMIk', self.movie.youtube_trailer_url)
        

if __name__ == '__main__':
    unittest.main()