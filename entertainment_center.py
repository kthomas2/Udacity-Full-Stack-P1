import json
import fresh_tomatoes
import media

# Load movie data from a json file
movie_file = open("media.json")
movie_data = json.load(movie_file)

# Loop through the movie data, instantiate the movie objects
# and create an array of movie objects
movies = []
for m in movie_data:
    movie = media.Movie(
        m['title'],
        m['poster_image_url'],
        m['trailer_youtube_url']
        )
    movies.append(movie)

movie_file.close()

# Pass the list of movies to the function that
# generates the HTML page
fresh_tomatoes.open_movies_page(movies)
