## Creating and activating virtualenv:
Python version 2.7 required

`python -m virtualenv env`
`.\env\Scripts\activate`


## Install the dependencies:
`pip install -r requirements.txt`


## Databases
By default the application is configured to use Sqlite3 database.

#### PostgreSQL
If you want to you PostrgeSQL uncomment its settings in file `/config/settigns.py`

#### Sqlite3
Enabled by default. To load initial data run the following command
`python manage.py loaddata tasks-source.json`


## Create an initial migration for models, and sync the database for the first time:
`python manage.py migrate`


## Run the server:
`python manage.py runserver`
