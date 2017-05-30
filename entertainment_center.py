"""This stores the details of movies and displays them on a website."""
import fresh_tomatoes
import media

def main():
    """This creates 6 movie objects and initialises these with the title, storyline, poster,
trailer and the release date."""
titantic = media.Movie("Titantic",
                       "Romance and disaster",
                       "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                       "https://www.youtube.com/watch?v=2e-eXJ6HgkQ",
                       "November 1, 1997")

forest_gump = media.Movie("Forest Gump",
                          "War hero, mogul and a prophet",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Forrest_Gump_poster.jpg/220px-Forrest_Gump_poster.jpg",
                          "https://www.youtube.com/watch?v=rNzRJ4IsZJU",
                          "June 23, 1994")

dumb_dumber = media.Movie("Dumb and Dumber",
                          "Two stupid friends",
                          "https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg",
                          "https://www.youtube.com/watch?v=MSu25pQ4iFw",
                          "December 16, 1994")

rocky = media.Movie("Rocky",
                    "Unlikely Hero",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/1/18/Rocky_poster.jpg/220px-Rocky_poster.jpg",
                    "https://www.youtube.com/watch?v=UjgmZAvJU3c",
                    "November 21, 1976")

the_dark_knight = media.Movie("The Dark Knight",
                              "True Justice",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=5y2szViJlaY",
                              "July 14, 2008")

hunger_games = media.Movie("The Hunger Games",
                           "A fight for their lives",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=LrXIG4oK7Ew",
                           "March 12, 2012")

# Stores a list of the movie objects
movies = [titantic, forest_gump, dumb_dumber, rocky, the_dark_knight, hunger_games]

# Opens the movie website in the users browser
fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()



