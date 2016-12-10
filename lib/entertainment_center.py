import media
import fresh_tomatoes
import csv

movies = []
with open('./data/movies.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
      movies.append(media.Movie(row))

fresh_tomatoes.open_movies_page(movies)