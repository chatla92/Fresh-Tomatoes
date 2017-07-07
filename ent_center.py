import media
import fresh_tomatoes

f = open("movies_trailers.csv")  # Read the Data from Input
list_movies = f.read().split("\n")  # Split up into entries
movies = []  # List of movies which will be displayed on the website

for each_movie in list_movies:
    if(each_movie!=""):
        each=each_movie.split(":::")
        print each
        movies.append(media.Movie(each[0], each[1], each[2], each[3], each[4], each[5], each[6]))

fresh_tomatoes.open_movies_page(movies)  # Creates website
