# Crowdsourcing Web App

## The Goal
* The goal of this part is to utilize image processing to present individual words or phrases and crowdsource them to the public
* This web app runs on a Python backend using the Django web framework and MongoDB

## Dependences
* MongoDB
* Django

## How to run the DEMO application
* Run mongod in a separate terminal
* To init the database with data, run :   ```python init_demo_data.py```
* ```python manage.py runserver```
* open ***127.0.0.1:8000/?id=1***  in your web browser for the demo app
* if deploying, you may need to run gunicorn and nginx with other commands for Django to work

## File System Overview
* SUNYdigsUpthePast
* app

## Issues to work on
* Figure out way to not brute force static links (Bug with Django static files)
* Integrate application with the rest of the data
   * Implement random id chosen after integrating the rest of the data 
* Make data loop once end is met 
