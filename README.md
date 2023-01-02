# Diplomantky.cz (rev. 2)
This is a repository for upgraded version of diplomantky.cz webpage.
Revision 2 of diplomantky should bring improved design and an administrative interface.

## Development

### Run locally with SQLite3
```
DEVELOPMENT_MODE=True DEBUG=True python3 manage.py runserver
```

### Run loally with remote DB
You will need a DB_URL string containing all the needed info for the configuration of DB.
This can be found on DigitalOcean at: `Project->Apps->Database->Connection_Details->Connection_String`.

1. create virtual environment, if not already created: `python3 -m venv .venv`
2. activate the environment: `source .venv/bin/activate`
3. install requirements if needed: `pip3 install -r requirements.txt`
4. finally run locally with remote DB on DigitalOcean:
```
DATABASE_URL=<DB_URL> DEVELOPMENT_MODE=True DEBUG=True python3 manage.py runserver
```


