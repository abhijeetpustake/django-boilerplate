# Django Rest Boilerplate

A boilerplate for creating projects using DRF-Docker-Gunicorn with an option to have databas on Sqlite and Postgres hosted locally.

## Features
Boilerplate contains the following:
1. Custom throttliong class
2. Configurations for filter backends
3. Multiple settings file based on the environment
4. Logs configuration nbased on environments
  - For dev, uat and prod logs configured for AWS
  - For local logs configured for local storage
5. Database storage configurations for Sqlite and Postgres which can be toggled using env variable
6. Configurations for Gunicorn in docker compose file

## Installation

Follow the steps to run this:
1. First clone the repo
2. Run the following command to activate the shell
    ```bash
    pipenv shell
    ``` 
3. Install all the dependencies
    ```bash
    pipenv install
    ```
4. Add all the variables in .env file
5. Rename log groups in Settings files based on the environment. Currently this supports AWS and local
6. Rename your_project to name of your project
7. Once project is renamed replace the name of the old project with new one at the following places:
    - wsgi.py
    - manage.py
    - docker-compose.yml
8. To run the project first buuild the container and execute the following:
    - Build the container
      ```bash
      docker-compose build
      ```
    - Check if django is up and running by executing the following command
      ```bash  
      docker-compose up
      ```
    - To do the migrations run the following command
      ```bash
      docker-compose exec web python manage.py migrate
      ```