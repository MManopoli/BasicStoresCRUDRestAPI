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

List can also be found in ./requirements.txt

## Script to build and start all docker images

    ./run-docker.sh

## Script to execute tests (after starting all docker images)

    ./run-tests.sh
