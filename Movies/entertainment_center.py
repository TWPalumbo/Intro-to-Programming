#imports fresh_tomatoes and media abstracts
import fresh_tomatoes
import media

#creates instances for each movie class
there_will_be_blood = media.Movie("There Will Be Blood",
                        "https://upload.wikimedia.org/wikipedia/en/d/da/There_Will_Be_Blood_Poster.jpg",
                        "https://www.youtube.com/watch?v=f3THVbr4hlY")

fight_club = media.Movie("Fight Club",
                        "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")

grand_budapest_hotel = media.Movie("The Grand Budapest Hotel",
                        "https://upload.wikimedia.org/wikipedia/en/1/1c/The_Grand_Budapest_Hotel.png",
                        "https://www.youtube.com/watch?v=1Fg5iWmQjwk")

the_matrix = media.Movie("The Matrix",
                        "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                        "https://www.youtube.com/watch?v=UM5yepZ21pI")


#exports each movie in fresh tomatoes layout
movies = [there_will_be_blood, fight_club, grand_budapest_hotel, the_matrix]
fresh_tomatoes.open_movies_page(movies)

                     
     
                     
