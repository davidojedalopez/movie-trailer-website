__author__ = 'David'

import webbrowser


class Movie:
    """
    The Movie class allows the creation of a Movie instance.
    It has five instance variables:
        - movie_title: The title of the movie.
        - movie_summary: A brief summary of the movie.
        - movie_poster_image_url: An URL to the poster image of the movie.
        - movie_trailer_youtube_url: An URL to the Youtube video trailer.
        - movie_rating: The IMDB rating the movie has earned.
    """
    def __init__(self, movie_title, movie_summary, movie_poster_image_url, movie_trailer_youtube_url, movie_rating):
        self.movie_title = movie_title
        self.movie_summary = movie_summary
        self.movie_poster_image_url = movie_poster_image_url
        self.movie_trailer_youtube_url = movie_trailer_youtube_url
        self.movie_rating = movie_rating

    def show_trailer(self):
        """
        Shows the trailer of the movie
        """
        webbrowser.open(self.movie_trailer_youtube_url)

