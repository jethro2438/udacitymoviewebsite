"""Defines the Movie class that contains the details of a movie."""
import webbrowser

class Movie(object):
    """This class provides a way to store movie related information.
    Attributes:
        title: Stores the title of the movie.
        storyline: Stores the basic plot of the movie.
        poster_image_url: Stores the URL of the movie poster.
        trailer_youtube_url: Stores the URL of the movie trailer.
        release_date: Stores the release date of the movie.
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_release_date):
        """Runs Movie class instance variables."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date

    def show_trailer(self):
        """Plays movie trailer in the web browser."""
        webbrowser.open(self.trailer_youtube_url)
