Author: David Ojeda
Email: david.ojeda.lopez@gmail.com


I. File list
------------
movies.css		CSS for the movie website
movies.js		JS for the movie website
fresh_tomatoes.py	HTML template and render methods for movie website
freash_tomatoes.html 	HTML output example
movie_center.py		Main file. Manages the search and adding of movies3
movies.py		Contains Movie class
IMDbPY-5.0		Folder containing IMDbPY package
README.txt		This file
------------


II. Installation
------------
Movies Trailer Website uses IMDbPY Python package retrieve and manage the data of
the IMDb movie database. Therefore, installation of the module may be needed. 
To install it, follow one of the three following methods:
	1. Use easy_install:
		easy_install IMDbPY
	2. Use pip:
		pip install IMDbPY
	3. Use the IMDbPY folder provided. From the command line and under the package folder directory:
		python setup.py install
------------


III. Usage
------------
To run this Python script do the following:
	1. Extract the .zip file to a known directory. 
	2. Open the command line.
	3. Move to: wherever_you_extracted_the_files\movies
	4. Run: python movie_center.py
	5. Enjoy! :)

To add a movie of your own open the movie_center.py file, and, below the "# Movies to add to movies_list" comment, use the add_movie method to add any movie you want. 
------------


IV. Comments and cited work 
------------
The method to display star rating is based on this example: http://codepen.io/Bluetidepro/pen/GkpEa. Just made modification to show 10 stars instead of 5. 