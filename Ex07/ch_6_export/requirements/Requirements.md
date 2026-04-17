# Movies Program Requirements Document

## Overview
The Movies Program is a command line interface (CLI) application that allows users to store and manage information about movies. The program will support adding new movies, listing all movies, and searching for movies by title.

## Functional Requirements

### 1. Add a New Movie
- **Description**: The user can add a new movie to the database.
- **Inputs**:
  - Title (string)
  - Release Year (integer)
  - Genre (string)
  - Duration (integer, in minutes)
- **Outputs**: Confirmation message indicating the movie was added successfully.

### 2. List All Movies
- **Description**: The user can list all movies stored in the database.
- **Inputs**: None
- **Outputs**: A list of all movies with the following details:
  - Title
  - Release Year
  - Genre
  - Duration

### 3. Search for a Movie by Title
- **Description**: The user can search for a movie by its title.
- **Inputs**:
  - Title (string)
- **Outputs**: Details of the movie matching the title, if found:
  - Title
  - Release Year
  - Genre
  - Duration
  - If no movie is found, an appropriate message is displayed.

### 4. Exit the Program
- **Description**: The user can exit the program.
- **Inputs**: None
- **Outputs**: A goodbye message.

## Non-Functional Requirements

### 1. Usability
- The program should be easy to use with clear prompts and messages.

### 2. Performance
- The program should handle a reasonable number of movies without significant performance degradation.

### 3. Portability
- The program should run on any system with Python installed.

## User Interface

### Command Line Interface (CLI)
- The program will interact with the user through a text-based command line interface.
- The user will be presented with a menu of options to choose from.

## Example User Interaction

```
Welcome to the Movie Database CLI!

Please choose an option:
1. Add a new movie
2. List all movies
3. Search for a movie by title
4. Exit

Enter your choice: 1

Enter movie title: Inception
Enter release year: 2010
Enter genre: Sci-Fi
Enter duration (in minutes): 148

Movie added successfully!

Please choose an option:
1. Add a new movie
2. List all movies
3. Search for a movie by title
4. Exit

Enter your choice: 2

Movies in the database:
1. Inception (2010) - Genre: Sci-Fi, Duration: 148 minutes

Please choose an option:
1. Add a new movie
2. List all movies
3. Search for a movie by title
4. Exit

Enter your choice: 4

Goodbye!
```

## Data Storage
- The program will store movie data in memory for the duration of the session.
- Persistent storage is not required for this version of the program.