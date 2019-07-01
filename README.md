[![Codacy Badge](https://api.codacy.com/project/badge/grade/004a38500bf04451bd81398662c9e3ea)](https://www.codacy.com/app/david-ojeda-lopez/tournament-database)

# Movie Trailer Website :movie_camera:

## About

Server-side code to store a list of movie titles, box art, poster images and movie trailer URLs. The data is expressed on a web page and allow users to review the movies and watch the trailers. 

## File List

| File | Description | 
|------|-------------|
| movies.py | Contains the Movie Class |
| movie_center.py | Main file. Manages the search and adding of movies |
| fresh_tomatoes.py | HTML template and render methods for movie website |
| fresh_tomatoes.html | HTML output example |
| movies.css | CSS for the movie website |
| movies.js | JS for the movie website |
| IMDBPY-5.0 | Folder containing the IMDbPY package |
| README.txt | This file |


## Installation

Movies Trailer Website uses IMDbPY Python package retrieve and manage the data of
the IMDb movie database. Therefore, installation of the module may be needed. 
To install it, follow one of the three following methods:

- **Use easy_install:**
	- easy_install IMDbPY
- **Use pip:**
	- pip install IMDbPY
- **Use the IMDbPY folder provided. From the command line and under the package folder directory:**
	- python setup.py install

## Usage

To run this Python script do the following:

1. Extract the .zip file to a known directory. 
2. Open the command line.
3. Move to: wherever_you_extracted_the_files\movies
4. Run: python movie_center.py
5. Enjoy! :)

To add a movie of your own open the movie_center.py file, and, below the "# Movies to add to movies_list" comment, use the add_movie method to add any movie you want. 

## Comments and cited work 

The method to display star rating is based on this example: [Star Rating][1]. Just made modification to show 10 stars instead of 5.

[1]: http://codepen.io/Bluetidepro/pen/GkpEa
