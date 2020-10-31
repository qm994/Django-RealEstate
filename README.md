# Django-RealEstate
A Django backend and React frontend: Real Estate Analysis Application

# TODO:

Configure the send email functionality and currently the send email not working in inquiry not working;
Containerized the app with docker;
Build the Portfolio page about myself;

OPTIONAL: Build scrapers for the app;


# 1. A few of python manage.py commands: notes here for memory purpose

## Migrate the changes to databse
(1) `python manage.py makemigrations` -> Migrate the models to the `migrations` folder
(2)`python manage.py migrate` -> Migrate the changes to database
 (Whenever we change the models `models.py`, we need to run both)
 
## Show the sql query used to create tables
 `python manage.py sqlmigrate listings 0001`
 
## How to update the static files?

Firstly add/edit the static files in the core app `realestate` then run  `python manage.py collectstatic` to migrate the changes to the core statics folder!

## start a new app
(1) `python manage.py startapp <app-name>`
(2) add the new app to the core app settings.py under the `INSTALLED_APPS`

# 2. Production Instance Summary

VPS: Droplet Ubuntu 20.04 1GB/1CPU, 25GB Disk, 1000GB Transfer;

When we set the `DEBUG=True`, the nginx will take care of the static files;





