from random import randrange, choice
"""
    This module allows random movies to be selected.
"""
__author__ = "Ken Loomis"

def pg_movie ( ):
        """ Produces 1 of 5 PG-rated movies titles from 2021-22 """
        choice = randrange(0, 5)
        if choice == 0:
            return "Hocus Pocus 2"
        elif choice == 1:
            return "Turning Red"
        elif choice == 2:
            return "Pinocchio: A True Story"
        elif choice == 3:
            return "The Bad Guys"
        else:
            return "Sonic the Hedgehog 2"

def pg13_movie ( ):
        """ Produces 1 of 5 PG13-rated movies titles from 2021-22 """
        choice = randrange(0, 5)
        movies = ( "Spider-Man: No Way Home",
                  "Death on the Nile",
                  "The Batman",
                  "Morbius",
                  "Doctor Strange in the Multiverse of Madness",
                  "Top Gun: Maverick" )
        return movies [ choice ]

def restricted_movie ( ):
        """ Produces 1 of 5 R-rated movies titles from 2021-22 """
        movies = ( "Spiderhead",
                    "Bullet Train",
                    "Nope",
                    "Don't Look Up",
                    "The King's Man" )
        return choice ( movies )
