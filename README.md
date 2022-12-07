# Phone-Book
simple phonebook application that has contact names and their numbers

## DataBase & Schema DEsign 
 Draw Sql : https://drawsql.app/teams/development-9/diagrams/phone-book
 
## Request Response Cycle 
 - you can load direct in postman 
 
 - collection api docs included within collection
 
- Postman Collection : https://api.postman.com/collections/6749950-73a30316-c8fd-44c8-b696-4cebd88ffae1?access_key=PMAT-01GKPMA6649GT7AMA6Z1W0FFPY

## Operate Locally 

 - clone project fron githun `git clone {PROJECT_URL}`
 - cd into Phone-Book `cd Phone-Book`
 - run command `pipenv shell` to create python virtual enviroment 
 - run command `pipenv install` to install used libraries 
 - cd phone_book `cd phone_book`
 - run development server `python manage.py runserver 0.0.0.0:8000` you can change ip or port as your needs 
 
## Dockerization 
 
 - Dockerfile included and run up on python alpine 
 - build new docker image using docker file ` docker image build -t phonebook:1.0 . `
 - create docker container from docker image ` docker run -d --name book -p 8000:800 {IMAGE_ID}`
 - now you can consume urls from you localhost using port 8000
 
 
 ## Build Project 
 
 - project build with python Version 3.10 
 - Django 4.1 
 - Django Rest 3.14
 
 ## Prerequestes 
 
  -  machine with python 3.10 and pip package index 
  -  pipenv python library for manage virtual enviroments
  -  docker engine installed 
 
