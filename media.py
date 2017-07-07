class Movie:
    """This class provides structures for movies to be stored"""

    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer, director, runtime, rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer = movie_trailer
        self.director = director
        self.runtime = runtime
        self.rating = rating
