#!/usr/bin/env/python3

import db
from objects import Movie

def display_welcome():
    print("The Movie List program")
    print()    
    display_menu()

def display_menu():
    print("COMMAND MENU")
    print("cat  - View movies by category")
    print("year - View movies by year")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit program")
    print()    

def display_categories():
    print("CATEGORIES")
    categories = db.get_categories()    
    for category in categories:
        print(f"{category.id}. {category.name}")
    print()
    
def display_movies(movies, title_term):
    print(f"MOVIES - {title_term}")

    print(f"{'ID':4}{'Name':38}{'Year':6}" 
          f"{'Mins':6}{'Category':10}")
    print("-" * 63)
    for movie in movies:
        print(f"{movie.id:<4d}{movie.name:38}{movie.year:<6d}"
              f"{movie.minutes:<6d}{movie.category.name:10}")                               
    print()  

def get_int(prompt):
    """
    Prompt the user to input a whole number and validate the input.

    This function repeatedly prompts the user with the given message until a valid
    integer is entered. If the user enters an invalid value, an error message is
    displayed, and the prompt is shown again.

    Args:
        prompt (str): The message to display to the user when requesting input.

    Returns:
        int: The integer value entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid whole number. Please try again.\n")

def display_movies_by_category():
    """
    Displays a list of movies belonging to a specific category.
    Prompts the user to input a category ID, retrieves the corresponding 
    category from the database, and displays all movies associated with 
    that category. If the category ID is invalid or does not exist, 
    an appropriate message is displayed.
    Dependencies:
        - get_int: Function to prompt the user for an integer input.
        - db.get_category: Function to retrieve a category by its ID.
        - db.get_movies_by_category: Function to retrieve movies by category ID.
        - display_movies: Function to display a list of movies.
    Output:
        - Prints the list of movies in the specified category or an error 
          message if the category ID is invalid.
    """
    category_id = get_int("Category ID: ")
    category = db.get_category(category_id)
        
    if category == None:
        print("There is no category with that ID.\n")
    else:
        print()
        movies = db.get_movies_by_category(category_id)
        display_movies(movies, category.name.upper())

def display_movies_by_year():
    year = get_int("Year: ")
    print()
    movies = db.get_movies_by_year(year)
    display_movies(movies, year)

def add_movie():
    name        = input("Name: ")
    year        = get_int("Year: ")
    minutes     = get_int("Minutes: ")
    category_id = get_int("Category ID: ")

    category = db.get_category(category_id)
    if category == None:
        print("There is no category with that ID. Movie NOT added.\n")
    else:
        movie = Movie(name=name, year=year, minutes=minutes,
                      category=category)
        db.add_movie(movie)
        print(f"{name} was added to database.\n")
    
def delete_movie():
    movie_id = get_int("Movie ID: ")
    db.delete_movie(movie_id)
    print(f"Movie ID {movie_id} was deleted from database.\n")
        
def main():
    db.connect()
    display_welcome()
    display_categories()
    
    while True:        
        command = input("Command: ").lower()
        if command == "cat":
            display_movies_by_category()
        elif command == "year":
            display_movies_by_year()
        elif command == "add":
            add_movie()
        elif command == "del":
            delete_movie()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
            
    db.close()
    print("Bye!")

if __name__ == "__main__":
    main()
