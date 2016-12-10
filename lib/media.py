import webbrowser

#makes a movie class to store indivual movie info
class Movie():
    def __init__(self, movie):
      self.title = movie["title"]
      self.year = movie["year"]
      self.storyline = movie["storyline"]
      self.poster_image_url = movie["poster_image_url"]
      self.youtube_trailer_url = movie["youtube_trailer_url"]
    
    def show_trailer(self):
      webbrowser.open(self.trailer_youtube_url)