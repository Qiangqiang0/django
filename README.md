# django

## Intro to dynamic webframe

web;send get; get response;
network sockets

Uniform Resouce Locator(URL)
protocal://host/document

python socket.socket  send the get to server
python socket.socket build the server

Basic idea of internet browser: request and response

## hello world

__init__.py

settings.py: 

3 function: routing, Views, models
parse to urls to choose which views to use.
Models.py tells how data are stored in databases.

virtual hosting:

## Html; CSS

CSS
1. color overwritten
    style ="color:red!important ;" 

2. image
     stye = ""

3. text, padding,border,margin


4. sizing the blocks


5. z index: overlap, whether it shows at the front or the background
 

## ngrok


## single table SQL 
SQLite, all in one file


## migrations

Object relational mapping

change models.py -> makemigrations -> migrate

```python

from django.db import mdoelse 
class User(models.Model):
    name = models.CharFields(max_length=128)

```

1. makemigrations: create a set migrations scripts

2. migrate: read make migrations and read into db

migrations:

    * from model to database
    * every time you migrate, you get new migrations
    * you can delete the file from migrations or delte the sqlite db and remigrate to get clean db


```python
from usermodel.models import User
u = User(names = "tom")
u.save()

```
# Web Server

1. Model-View-Controller(MVC)

    * Controller: the code for make decison and thinking
    * Viewer: CSS, HTML
    * model: peresistant data

    Django model: 

    * rougting: urls.py
    * Views: do controller tasks,views.py
    * Models: talk to the database


2. Views and templates

    * Django looks at the request URL and look aturls.py to select a view

    * three patterns for views (in urls.py)

    URL dispather (routing)

    1. route to predefined class
    2. route to a fucntion in views.py
    3. route to a class in views that has get() and post()

    cross-site scripting:
        solution: django.utils.html.escape


3. http status codes
    * 200: OK

    * 404: not found


# template

1. one or more applications in folders

2. render data + render template ==> render output

3. template tags/code

    * subsititution

        {{ zap }}: automatic escape

        {{zap|safe}}: not escape

   * Callling mode

        {% url 'cat-deatial' cat.id %}

        it has some function

    * logic
    {% if zap > 100 %}
    {% endif %}

    * blocks

    {% blocks %}

4. template inheritance

    * extends

    * block 


5. reverse urls
r
urlpatterns = [
    path("cats",views.catViews.as.view(),name = "cats"),
    path("cat/<int:pk_from_url>}",views.catViewDetial.as.view(),name = "cat"),
]
# Generic views


# forms 
1. get


2. post


3. refresh

set cookie, what, how?
