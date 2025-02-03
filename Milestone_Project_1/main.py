# Main Python File

# List of movies stored using a list of dictionaries
movies = [
    {
        "title": "The Shawshank Redemption",
        "year": 1994,
        "rating": 9.2,
        "director": "Frank Darabont",
        "genre": "Crime, Drama",
    },
    {
        "title": "The Godfather",
        "year": 1972,
        "rating": 9.2,
        "director": "Francis Ford Coppola",
        "genre": "Crime, Drama",
    },
    {
        "title": "The Godfather: Part II",
        "year": 1974,
        "rating": 9.0,
        "director": "Francis Ford Coppola",
        "genre": "Crime, Drama",
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "rating": 9.0,
        "director": "Christopher Nolan",
        "genre": "Action, Crime, Drama",
    },
    {
        "title": "12 Angry Men",
        "year": 1957,
        "rating": 8.9,
        "director": "Sidney Lumet",
        "genre": "Drama",
    },
    {
        "title": "Schindler's List",
        "year": 1993,
        "rating": 9.2,
        "director": "Steven Spielberg",
        "genre": "Biography, Drama, History",
    },
    {
        "title": "The Lord of the Rings: The Return of the King",
        "year": 2003,
        "rating": 8.9,
        "director": "Peter Jackson",
        "genre": "Action, Adventure, Drama",
    },
    {
        "title": "Pulp Fiction",
        "year": 1994,
        "rating": 8.9,
        "director": "Quentin Tarantino",
        "genre": "Crime, Drama",
    },
    {
        "title": "The Good, the Bad and the Ugly",
        "year": 1966,
        "rating": 9.0,
        "director": "Sergio Leone",
        "genre": "Action, Adventure, Crime",
    },
    {
        "title": "Fight Club",
        "year": 1999,
        "rating": 8.8,
        "director": "David Fincher",
        "genre": "Drama",
    }
]


# Add a new movie to the list

def add_movie(title, year, rating, director, genre):
    movie = {
        "title": title,
        "year": year,
        "rating": rating,
        "director": director,
        "genre": genre,
    }
    movies.append(movie)


# Remove a movie from the list

def remove_movie(title):
    for movie in movies:
        if movie["title"] == title:
            movies.remove(movie)
            break  # Exit the loop if the movie is found
    else:
        print(f"Movie '{title}' not found.")
        

# List all the movies in the list

def list_movies():
    for movie in movies:
        print(f"{movie['title']} ({movie['year']}) - {movie['rating']} stars, Directed by {movie['director']}, Genre: {movie['genre']}")
        

# Find a movie by title

def find_movie(title):
    for movie in movies:
        if movie["title"] == title:
            print(f"Movie found: {movie['title']} ({movie['year']}) - {movie['rating']} stars, Directed by {movie['director']}, Genre: {movie['genre']}")
            return
    else:
        print(f"Movie '{title}' not found.")


# Calling the functions

# run = input("Do you want to run the program? (y/n): ")
K = True
while K==True:
    user_choice = input("What do you want to do? (add, remove, list, find): ")
    if user_choice == "add":
        title = input("Enter the title of the movie: ")
        year = int(input("Enter the year of the movie: "))
        rating = float(input("Enter the rating of the movie: "))
        director = input("Enter the director of the movie: ")
        genre = input("Enter the genre of the movie: ")
        add_movie(title, year, rating, director, genre)
        print("Movie added successfully.")
    elif user_choice == "remove":
        title = input("Enter the title of the movie: ")
        remove_movie(title)
        print("Movie removed successfully.")
    elif user_choice == "list":
        print("Here is the list of movies: ")
        list_movies()
    elif user_choice == "find":
        title = input("Enter the title of the movie: ")
        find_movie(title)
    elif user_choice == "q":
        print("Quitting...")
        K = False
    else:
        print("Invalid choice.")
        exit()
    print()  # Print an empty line
    