import webbrowser


class Movie():
    """ This class provides a way to store movie related information

        Attributes:
            movie_title (str):     The movie's title
            poster_image (str):    URL to image of the movie poster
            trailer_youtube (str): URL to YouTube movie trailer

       Methods:
           show_trailer: Opens YouTube URL
    """

    # class constructor and instance variables
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # instance method to show youtube url in the browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
