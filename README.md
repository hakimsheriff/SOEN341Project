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

* Ahmad Abunada (@Ahmad-ConU)
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

To install the dependencies required to run the application server, from with the pipenv shell:

	cd application
	
	pip install -r requirements.txt


## Starting the Application Server

### Django Server

To start the Django server, enter the our application directory with `cd application` and run:

    python manage.py runserver

The django server will run on http://localhost:8000/

#### Important notes
Before commiting anything to the project, make sure to into our application directory and run:
    
	pip freeze >  requirements.txt
	
## Architecture 

The following is a diagram of our application's architecture. It is of type "Model-View-Controller".

![Architecture Diagram](PigeonPostArchitecture.JPG?raw=true "Architecture Diagram")
	
## Testing

#### Unit Tests

To run our unit tests locally, run:

    python manage.py test
	
This will run the unit tests defined in our tests.py file.

#### Continous Integration Pipeline for Unit Tests

Our project uses Travis-CI as our hosted continuous integration service. Travis-CI builds and runs our unit tests for every branch and pull request. Our Travis-CI page be be found here: https://www.travis-ci.com/github/hakimsheriff/SOEN341Project

#### Acceptance Testing

Acceptance tests for our project are defined in the GitHub Issue for that particular story. We verify that all criteria is met before considering a feature to be done.