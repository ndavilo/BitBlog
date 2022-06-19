# BitBlog
Blog created with django and python to allow registered user trade on cryptocurrencies 
Django-Heroku
Steps:
        1)	Create a folder
        2)	Open CMD
        3)	Create a virtual environment:
        a)	python3 -m venv name
        b)	source name/bin/activate
        4)	pip3 install Django
        5)	pip3 install Heroku
        6)	pip3 install gunicorn
        7)	pip3 install django-heroku
        8)	pip3 install Pillow
        9)	pip3 install python-decouple
        10)	django-admin startproject nameofproject
        11)	cd nameofproject
        12)	python3 manage.py startapp nameofapp
        13)	python3 manage.py makemigrations
        14)	python3 manage.py migrate
        15)	python3 manage.py createsuperuser
        a)	enter user name
        b)	enter user email
        c)	enter user passwords
        16)	pip freeze > requirements.txt
        17)	git init
        18)	git add
        19)	git commit -m “New Project”
        20)	open github
        a)	create new repository
        b)	copy name of repository
        21)	git remote add origin paste 19b
        22)	git push origin master (if you have push to master before it might not work | then git push origin main) 
        23)	open setting.py
        a)	add the following on top:
        i)	import os
        ii)	import django_heroku
        iii)	import dj_database_url
        iv)	from decouple import Config
        b)	add to MIDLEWARE:
        i)	‘whitenoise.middleware.WhiteNoiseMiddleware
        24)	touch Procfile 
        a)	open Procfile
        b)	web: gunicorn nameofyourapp.wsgi

How to change database from SQLite to Progress in Django:
  Command needed to backup database:
                    python manage.py dumpdata > datadump.json
  Go to settings.py:
                      DATABASES = {
                          'default': {
                              'ENGINE': 'django.db.backends.postgresql_psycopg2',
                              'NAME': 'name',                     
                              'USER': 'user',
                              'PASSWORD': 'password',
                              'HOST': 'localhost',
                              'PORT': '5432',      
                          }
                      }
                      db_from_env = dj_database_url.config(conn_max_age=600)
                      DATABASES['default'].update(db_from_env)
                      run migrations

Django Security Vulnerabilities:
                                  Session Modification
                                  Session Hijacking
                                  Cache Poisoning
                                  Arbitrary URLS generation
                                  CSRF: Unauthenticated Forged Requests
                                  CSRF Via Forged AJAX Requests
                                  Directory Traversal
                                  DoS 
                                  IPAddressField, FilePathField, GenericIPAddressField attack
