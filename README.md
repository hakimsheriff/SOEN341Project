# Pigeon Post - A SOEN341Project

## Objective

Develop an instagram-like social media platform.

## Project Description

This project will consist of a web application designed to mimmick certain features from the popular social media app "Instagram." This will include features such as posting pictures and will allow users to interact with posted pictures in various ways, such as commenting or "liking". 

## Core Features

* Posting a picture (with a text description)
* Leaving comments to posted pictures
* Following a user
* Liking a post

## Team Members

* Hakim Sheriff (@hakimsheriff)
* Aseel Meeran Babu Hussain (@AseelAce) 
* Lucas Silva (@Lucas-ConU)
* Waleed Iqbal (@WaleedIqbal99)
* Yasser Edebbab (@timotei1)
* Fatima El Fouladi (@seaiam)

## Technologies

* Python
* Django
* Bootstrap

## Dependecy Installation Instructions

First, you must install Python from https://www.python.org/downloads/. 
The version that has been tested is 3.9.1.

We will use pip to install dependencies.

To install pip, download https://bootstrap.pypa.io/get-pip.py and run

    python get-pip.py

It is recomended to run this server with Pipenv. To install and start Pipenv:

    pip install pipenv

    pipenv shell

To install the dependencies required to run the backend server, from with the pipenv shell:

	cd backend
	
	pip install -r requirements.txt


## Starting the Application Server

#### Backend

To start the Django backend, enter the backend directory with `cd backend` and run:

    python manage.py runserver

The django server will run on http://localhost:8000/

### Important notes
Before commiting anything the the project , make sure to go to the backend and run:
    pip freeze >  requirements.txt

