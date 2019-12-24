# 🔥 FireLocs

A project to be used during our 2020 NCSS Masterclass.

## Getting started

Create a `virtualenv` in which to install the project dependencies.

    virtualenv -p python3.7 venv

Install the dependencies with `pip`.

    venv/bin/pip install -r requirements.txt

Create your database.

    venv/bin/python manage.py migrate

Populate your database.

    venv/bin/python manage.py import_fires http://www.rfs.nsw.gov.au/feeds/majorIncidents.xml

Start the development server.

    venv/bin/python manage.py runserver

Launch your browser and visit http://localhost:8000/ and http://localhost:8000/json/ to interact with the system.
