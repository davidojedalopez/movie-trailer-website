__author__ = 'David'

import movies
import fresh_tomatoes
from imdb import IMDb


def get_movie_from_imdb(movie_title):
    """
    Get a movie from IMDB database
    :param movie_title: Title of movie to search for
    :return: an IMDB movie object
    """
    movie_list = ia.search_movie(movie_title)
    movie_object = ia.get_movie(movie_list[0].getID())
    return movie_object


def add_movie(movie_title, youtube_video_url):
    """
    Adds a movie to a list
    :param movie_title: Title of movie to add
    :param youtube_video_url: Youtube URL for the movie
    """
    movie_object = get_movie_from_imdb(movie_title)
    movie = create_own_movie_object(movie_object, youtube_video_url)
    movies_list.append(movie)


def create_own_movie_object(movie_object, youtube_video_url):
    """
    Mirros IMDB movie object with our own Movie object
    :param movie_object: A movie object from IMDB
    :param youtube_video_url: Youtube URL for the movie
    :return: Our own Movie object
    """
    movie = movies.Movie(movie_object['title'],
                         movie_object['plot outline'],
                         movie_object['cover url'],
                         youtube_video_url,
                         movie_object['rating']
                         )
    return movie

movies_list = []

# IMDbPY access method
ia = IMDb()

# Movies to add to movies_list
add_movie("Toy Story", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
add_movie("The Matrix", "https://www.youtube.com/watch?v=MsAniqGowKE")
add_movie("Spirited Away", "https://www.youtube.com/watch?v=ByXuk9QqQkk")
add_movie("Back to the Future", "https://www.youtube.com/watch?v=qvsgGtivCgs")

# Open web browser with previous movies information
fresh_tomatoes.open_movies_page(movies_list)
