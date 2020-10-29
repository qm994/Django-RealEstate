# Django-RealEstate
A Django backend and React frontend: Real Estate Analysis Application


# Planning:
(1)First version of app will use the fake data then after the version1 will be expecting to have the data scraped from Trulia site history data as the source.


# A few of python manage.py commands: notes here for memory purpose

## 1)Migrate the models to the `migrations` folder
 `python manage.py makemigrations`
 
## 2)Migrate the changes to databse
 `python manage.py migrate`
 
## 3)Show the sql query used to create tables
 `python manage.py sqlmigrate listings 0001`
 
## How to update the static files?

Firstly add/edit the static files in the core app `realestate` then run  `python manage.py collectstatic` to migrate the changes to the core statics folder!

## start a new app
python manage.py startapp <app-name>
