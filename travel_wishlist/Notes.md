# Lab 10 / Travel Wishlist Django Webapp

## Get set up... 
1. Get venv set up, then `pip install django`
2. Start the project `django-admin startproject <project_name>`
3. Move into new project directory `cd <project_name>`
4. Test basic set up with `python manage.py runserver`
   - Open here: (http://127.0.0.1:8000)[http://127.0.0.1:8000] (or displayed dev server address)
5. Create an app: `python manage.py startapp <app_name>` (one of potentially many, each is a single part of the website)
6. Create classes in the new app directory's `models.py` file (`<app_name>.models.py`)
   - `from django.db import models`
         `class <class_name>(models.Model):`
               each attribute must be a models.<db_field_type>(field attribute)
                example:
   ```
   class Place(models.Model):
       name = models.CharField(max_length =200)
       visited = models.BooleanField(default=False)
   ``` 
7. Run `python manage.py makemigrations` to create migrations (instructions for django to create tables from models)
8. Then run `python manage.py migrate` to create the tables 

## Admin stuff... 
1. go to <app_name>.admin.py
2. import data types you want to look at `from .models import <class_name>`
3. register it with `admin.site.register(<class_name>)`
4. run `python manage.py createsuperuser`
   - set a username (necessary), email (optional), password (necessary, can be crappy unless on a live server)
5. Login at (http://127.0.0.1:8000/admin)[http://127.0.0.1:8000/admin]


## Creating a page... 
### Creating a form for users to create new objects
This example page should have a form and and a list of objects with a false value (places unvisited)
We need...
- URL (route)
  - under the orignal **project** directory (*not the app directory*) enter the `urls.py` file
  - import `from django.urls import include`
  - add new line in `urlpatterns` list
    - `path('',include('<app_name>.urls)` (this lets the app handle everything other than the predefined `path('admin/', admin.site.urls)` path)
  - Create <app_name>.urls in the app directory. 
    - import...
      - `from django.urls import path`
      - `from . import views`
    - define paths to views 
```
urlpatterns = [
    path('', views.place_list, name = 'place_list')  # Note that name = same as new view function we make shortly
]
```

- View (code fetching list of places not visited from db, creates response with the data)
    - move to `<app_name>.views.py`
    - create a function 
```
def place_list(request):  # must have 1 arg: request
    return render(request, '<app_name>/<template_name>.html')
```

- Template (HTML template containing the form and placeholder for list of objects [places])
  - create the Templates subdirectory under the app directory (`<app_name>.templates`)
  - create another subdirectory inside the new templates directory, this one matching the app name (always or just for this example?)
    - (`<app_name>.templates.<app_name>`)
  - create a template html file in this directory
    - (`<app_name>.templates.<app_name>.<template_name>`)  # using 