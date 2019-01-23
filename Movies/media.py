#Imports the default web browser
import webbrowser

#Stores information to create class Movie
class Movie():

    #Takes input for movie_title, poster_image, and trailer_youtube and returns self
    #to create parameters for class Movie
    def __init__(self, movie_title, poster_image,
                 trailer_youtube):
        #Inputs movie title string and returns the name of the movie
        self.title = movie_title
        #Inputs the poster image link and returns the poster image
        self.poster_image_url = poster_image
        #Inputs the movie trailer link and returns the movie trailer
        self.trailer_youtube_url = trailer_youtube

    #Defines how movie trailer function will play trailer in browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
