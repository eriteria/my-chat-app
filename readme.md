# Riachat
#### Video Demo: https://youtu.be/o2Ib9q5FxOk
#### Live Demo: https://chateria.herokuapp.com
### Description:
Riachat is a real-time chat app made with Django, a web framework for python. You can chat in real time in chat rooms. Users can also create these aforementioned rooms and also join them. This is my final project for CS50x

This project was built with a third-party django module called **Django Channels**. It is also hosted on heroku. It uses Postgres for it's database, provided by heroku. I also use redis as the channel_layer for django channels. Channel Layers allow us to create interaction between different instances of an application

#### Folders
    account
    core
    djangochat
    room
    staticfiles

-----------------------

#### "djangochat" folder:
This folder contains the core files found in a django project.
##### Files and Folders:    
    1. __init__.py: An empty python file that the pythin intepreter uses to differentiate between a regular folder and a module.
    2. asgi.py
    3. settings.py: Contains all the variables that are important in the django application
    4. urls.py: contains the route to each of the applications in the django project.
    5. wsgi.py

---------------------

####  "core" Folder:
This is a folder or in django terms, an app, that just contains the front page of the website.

> A project can have multiple apps.

##### Files and Folders:
    1. migrations/
    2. static/ : Contains all the static files that are used within this app.
    3. templates/ : Contains all the html templates that are used in this application.
    4. __init__.py
    5. admin.py: This is where you register models you want to show in the django admin dashboard.
    6. apps.py
    7. forms.py
    8. models.py
    9. tests.py
    10. urls.py: contains the routing/url patterns for the views in this app
    11. views.py: contains view functions for this app

##### Images
###### Front Page without an authenticated user
![Front Page without an authenticated user](/screenshots/homepage-logged-out.jpg "Front Page when logged out.")

###### Front Page with an authenticated user
![Front Page with an authenticated user](/screenshots/homepage-logged-in.jpg "Front Page when logged in.")

-----------------------------

#### "account" Folder:
This contains the app that handles authentication and user management. Functions like signup, login, e.t.c.


##### Files and Folders:
> Most of the files and folders like **apps.py**, **tests.py**, remain the same across all the apps within a project.
> I would just highlight the files/folders that change or seem important to highlight.

    1. Forms.py: contains the signup form for the website. The default login form for django was used that is why there is no login form.

##### Images
###### Signup page
![Signup page](/screenshots/signup%20page.jpg "Signup page")

###### Login page
![Login page](/screenshots/login%20page.jpg "Login page")


----------------------------------

#### "room" Folder:
This app handles all the room management and contains the logic for real-time chat. It is the most important app in this project.

##### Files and Folders:
    1. consumers.py: This file contains the the functions that handles events and that happens between the client and the server. It contains functions that are triggered by events like say when a user joins/connects to a room. It is basically the view function for an ASGI app
    2. forms.py: Contains the form for creating and editing rooms.
    3. models.py: contains the ORM (Object Relational Mapping) models for the rooms.
    4. routing.py: this file is the analogous to the "urls.py" file in a wsgi app. It contains the route/url pattern to the consumer.
    5. views.py: contains all the view functions that are not asynchronous or do not run on ASGI terms.

##### Images
###### Public Rooms page
![Public Rooms page](/screenshots/public%20rooms.jpg "Public Rooms page")

###### Room page
![Room page](/screenshots/room.jpg "Room page")

###### Create Room page
![Create Room page](/screenshots/create%20rrom%20page.jpg "Create Room page")

###### Edit Room page
![Edit Room page](/screenshots/edit%20room.jpg "Edit Room page")


--------------------------

#### "staticfiles" Folder:
This is where django collects all the static files for the whole project.

--------------------------------------
#### Other Files

-----------------------------------------

##### manage.py
Used to manage and interact with the django project

--------------------------------------


##### requirements.txt
Contains all the python modules and dependencies used in this project.

--------------------------------------

##### Procfile
Configuration file for heroku.

--------------------------------------

##### .env
contains sensitive data and variables for the project


## Built With

* [Django](https://www.djangoproject.com/)
* [Tailwind CSS](https://tailwindcss.com/)
* [Postgres](https://www.postgresql.org/)
* [Redis](https://redis.io/)

Hosted on

* [Heroku](https://www.heroku.com/)


## Acknowledgements

* [CS50](https://cs50.harvard.edu/x/2022/)


# This was CS50x 🦆.
