import media
import fresh_tomatoes
import csv

#Opens a movie csv and turns each row into a movie instance
movies = []
with open('./data/movies.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
      movies.append(media.Movie(row))

#Calls open_movies_page method on the arraw of movie objects
fresh_tomatoes.open_movies_page(movies)