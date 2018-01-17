# Project Overview

You will develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

You develop a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication. 

### Requiremnets 

1- Install the dependency libraries (Flask, sqlalchemy, requests and oauth2client)

2- Install postgreSQL and pgAdmin 



## Running the Sports App

Create a database with the name **sportsapp** through pgAdmin. 

Now type **python database_setup.py** to initialize the database.

Type **python filldb.py** to populate the database with restaurants and menu items. (Optional)

Type **python project.py** to run the Flask web server. In your browser visit **http://localhost:8000** to view the sports app.  You should be able to view, add, edit, and delete items(created by you) 


## JSON endpoint

visit **http://localhost:8000/category/<path:category_name>/JSON** to view the item of a specific category
visit **http://localhost:8000/category/JSON** to view the list of categories   
