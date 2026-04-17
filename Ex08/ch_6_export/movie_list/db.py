import sqlite3
from contextlib import closing

from objects import Category, Movie

conn = None

def connect():
    """
    Establishes a connection to the SQLite database.

    This function initializes the global `conn` variable with a connection
    to the database file `movies.sqlite`. It also sets the row factory to
    `sqlite3.Row` for easier access to row data by column name.
    """
    global conn
    if not conn:
        DB_FILE = "movies.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    """
    Closes the connection to the SQLite database.

    If a connection exists, this function closes it to release resources.
    """
    if conn:
        conn.close()

def make_category(row):
    """
    Creates a Category object from a database row.

    Args:
        row (sqlite3.Row): A row containing category data.

    Returns:
        Category: An instance of the Category class.
    """
    return Category(row["categoryID"], row["categoryName"])

def make_movie(row):
    """
    Creates a Movie object from a database row.

    Args:
        row (sqlite3.Row): A row containing movie data.

    Returns:
        Movie: An instance of the Movie class.
    """
    return Movie(row["movieID"], row["name"], row["year"], row["minutes"],
            make_category(row))

def make_movie_list(results):
    """
    Converts a list of database rows into a list of Movie objects.

    Args:
        results (list): A list of rows containing movie data.

    Returns:
        list: A list of Movie objects.
    """
    movies = []
    for row in results:
        movies.append(make_movie(row))
    return movies

def get_categories():
    """
    Retrieves a list of categories from the database.

    This function executes a SQL query to fetch all category IDs and names 
    from the 'Category' table. It processes the results and returns a list 
    of category objects created using the `make_category` function.

    Returns:
        list: A list of category objects, where each object represents a 
              category with its ID and name.

    Raises:
        Any database-related exceptions that may occur during the execution 
        of the SQL query or while fetching the results.
    """
    query = '''SELECT categoryID, name as categoryName
               FROM Category'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    categories = []
    for row in results:
        categories.append(make_category(row))
    return categories

def get_category(category_id):
    """
    Retrieve a category from the database based on the given category ID.

    Args:
        category_id (int): The ID of the category to retrieve.

    Returns:
        object or None: An object representing the category with keys 
        'categoryID' and 'categoryName' if found, otherwise None.
    """
    query = '''SELECT categoryID, name AS categoryName
               FROM Category WHERE categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        row = c.fetchone()
        if row:
            return make_category(row)
        else:
            return None

def get_movies_by_category(category_id):
    """
    Retrieves movies from the database based on the given category ID.

    Args:
        category_id (int): The ID of the category to filter movies by.

    Returns:
        list: A list of Movie objects belonging to the specified category.
    """
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID,
                      Category.name as categoryName
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE Movie.categoryID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (category_id,))
        results = c.fetchall()

    return make_movie_list(results)

def get_movies_by_year(year):
    """
    Retrieves movies from the database based on the given year.

    Args:
        year (int): The year to filter movies by.

    Returns:
        list: A list of Movie objects released in the specified year.
    """
    query = '''SELECT movieID, Movie.name, year, minutes,
                      Movie.categoryID,
                      Category.name as categoryName
               FROM Movie JOIN Category
                      ON Movie.categoryID = Category.categoryID
               WHERE year = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (year,))
        results = c.fetchall()

    return make_movie_list(results)

def add_movie(movie):
    """
    Adds a new movie to the database.

    Args:
        movie (Movie): The Movie object to be added to the database.

    Returns:
        None
    """
    sql = '''INSERT INTO Movie (categoryID, name, year, minutes) 
             VALUES (?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie.category.id, movie.name, movie.year,
                        movie.minutes))
        conn.commit()

def delete_movie(movie_id):
    """
    Deletes a movie from the database based on the given movie ID.

    Args:
        movie_id (int): The ID of the movie to delete.

    Returns:
        None
    """
    sql = '''DELETE FROM Movie WHERE movieID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(sql, (movie_id,))
        conn.commit()