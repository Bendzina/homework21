import json
import os

file_path = 'movies.json'  

print(f"Current working directory: {os.getcwd()}")

if not os.path.isfile(file_path):
    print(f"Error: File {file_path} not found. Please check the file path.")
    exit()

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


skipped_movies = []

print(f"Total movies found: {len(movies)}")

for movie in movies:
    year = movie.get('year')
    genres = movie.get('genre', [])

    
    print(f"Processing movie: {movie}")

 
    if isinstance(year, int) and isinstance(genres, list):
        if year > 2000 and 'Crime' in genres:
            updated_genres = ['New_Crime' if genre == 'Crime' else genre for genre in genres]
            movie['genre'] = updated_genres
            new_crime_movies.append(movie)
            print(f"Added to new_crime_movies: {movie}")

      
        elif year < 2000 and 'Drama' in genres:
            updated_genres = ['Old_Drama' if genre == 'Drama' else genre for genre in genres]
            movie['genre'] = updated_genres
            old_drama_movies.append(movie)
            print(f"Added to old_drama_movies: {movie}")

       
        elif year == 2000:
            movie['genre'].append('New_Century')
            new_century_movies.append(movie)
            print(f"Added to new_century_movies: {movie}")

    else:
        skipped_movies.append(movie)
        print(f"Skipped movie due to invalid data (year or genre): {movie}")


updated_movies = new_crime_movies + old_drama_movies + new_century_movies


if not updated_movies:
    print("No movies met the criteria and were added to updated_movies.")
else:
    print(f"Number of movies updated: {len(updated_movies)}")

output_file_path = 'updated_movies.json'
with open(output_file_path, 'w') as json_file:
    json.dump(updated_movies, json_file, indent=4)

if skipped_movies:
    print(f"Skipped movies due to missing or incorrect year values: {len(skipped_movies)}")
else:
    print("No movies were skipped due to missing or incorrect year values.")
