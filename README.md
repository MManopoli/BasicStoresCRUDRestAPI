# BasicStoresCRUDRestAPI
Augmented final code for Udemy Course: "REST APIs with Flask and Python":

    - Course code implements basic CRUD REST API for stores and items
    - REST API utilizes various Flask python packages, uWSGI, PostGreSQL and PGAdmin, and an nginx proxy
    - My modifications were to:
        - Stand up the whole system with Docker
        - Modify item creation to use store_name rather than an unknown store_id
      
      The course, by contrast has the student setup everything on a cloud server from scratch

# Course Link
https://www.udemy.com/course/rest-api-flask-and-python/

## Required Python packages

    Flask
    Flask-RESTful
    Flask-JWT
    Flask-SQLAlchemy
    uWSGI
    psycopg2

List can also be found here:

    ./requirements.txt

## Instructions to build and start all docker images

Setup the .env file

    copy or rename the sample.env file to just ".env"
    
    Set the following properties (no spaces may be between the "=" sign and the value)
    
    - Set the DB_USER and DB_PASSWORD:
    DB_USER=##USERNAME##
    DB_PASSWORD=##PASSWORD##
    
    - Set the DATABSE_URL using the DB_USER and DB_PASSWORD:
    DATABASE_URL=postgresql://##DB_USER##:##DB_PASSWORD##@fullstack-postgres:5432/fullstack_api
    
    - Set a random or intricate API_SECRET to some value (no spaces)
    API_SECRET=##JWT_SECRET_KEY##                            # Used for creating a JWT. Can be anything

    - Set a default email and password for logging into PostGreSQL Admin (PGADMIN)
    PGADMIN_DEFAULT_EMAIL=##username@email.com##
    PGADMIN_DEFAULT_PASSWORD=##PASSWORD##

Then execute:

    ./run-docker.sh

## Script to execute tests (after starting all docker images)

    ./run-tests.sh
