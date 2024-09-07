import json
import os

# Define the path to the movies JSON file - adjust as necessary
file_path = 'movies.json'  # Relative path, change to absolute if needed

# Check the current working directory
print(f"Current working directory: {os.getcwd()}")

# Verify if the file exists at the specified path
if not os.path.isfile(file_path):
    print(f"Error: File {file_path} not found. Please check the file path.")
    exit()

# If file exists, proceed to read and process it
try:
    with open(file_path, 'r') as json_file:
        movies = json.load(json_file)
except FileNotFoundError:
    print(f"Error: File {file_path} not found.")
    exit()
except json.JSONDecodeError as e:
    print(f"Error reading JSON file: {e}")
    exit()

new_crime_movies = []
old_drama_movies = []
new_century_movies = []

# Track skipped movies for debugging
skipped_movies = []

# Debug: Check how many movies are in the JSON
print(f"Total movies found: {len(movies)}")

for movie in movies:
    year = movie.get('year')
    genres = movie.get('genre', [])

    # Debug: Print the movie details for each iteration
    print(f"Processing movie: {movie}")

    # Ensure year is not None, is an integer, and genres is a list
    if isinstance(year, int) and isinstance(genres, list):
        # Check for Crime genre and year > 2000
        if year > 2000 and 'Crime' in genres:
            updated_genres = ['New_Crime' if genre == 'Crime' else genre for genre in genres]
            movie['genre'] = updated_genres
            new_crime_movies.append(movie)
            print(f"Added to new_crime_movies: {movie}")

        # Check for Drama genre and year < 2000
        elif year < 2000 and 'Drama' in genres:
            updated_genres = ['Old_Drama' if genre == 'Drama' else genre for genre in genres]
            movie['genre'] = updated_genres
            old_drama_movies.append(movie)
            print(f"Added to old_drama_movies: {movie}")

        # Check for movies released exactly in 2000
        elif year == 2000:
            movie['genre'].append('New_Century')
            new_century_movies.append(movie)
            print(f"Added to new_century_movies: {movie}")

    else:
        # Log movies skipped due to missing or incorrect year/genre
        skipped_movies.append(movie)
        print(f"Skipped movie due to invalid data (year or genre): {movie}")

# Combine all modified movie lists
updated_movies = new_crime_movies + old_drama_movies + new_century_movies

# Check if the updated_movies list is empty
if not updated_movies:
    print("No movies met the criteria and were added to updated_movies.")
else:
    print(f"Number of movies updated: {len(updated_movies)}")

# Write the modified movies back to updated_movies.json
output_file_path = 'updated_movies.json'
with open(output_file_path, 'w') as json_file:
    json.dump(updated_movies, json_file, indent=4)

# Debug: Log the skipped movies if any
if skipped_movies:
    print(f"Skipped movies due to missing or incorrect year values: {len(skipped_movies)}")
else:
    print("No movies were skipped due to missing or incorrect year values.")
