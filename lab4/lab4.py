from movies import pg_movie, pg13_movie, restricted_movie
"""
    lab4.py
    Lab #4

    This lab allows us to explore complex if statements.
    The Movie Night program will randomly select some movies
    for the user to watch and how they can get to the movie
    theater based on their entered age.
"""
__author__ = "Joel Mercado"

# Part I
print ( "Welcome to Movie Night! Your random decider for what to watch." )
age = int ( input ( "Enter your age: " ) )

# Part II
print ( "What are you going to watch: " );
print ( f"You can watch \"{pg_movie()}\"" )

# Part III
print ( "How you getting to the theater: " );
if age < 4:
    print ( "Mommy better carry me" )
elif age < 13:
    print ( "I'll get a ride from dad" )
elif age < 15:
    print ( "I'm gonna get an uber" )
elif age < 16:
    print ( "Grandma can ride along, i've got my permit" )
elif age < 90:
    print ( "I'm driving" )
else:
    print ( "No driving after dark" )