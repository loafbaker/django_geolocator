django_geolocator
=================

A django-based app for accessing and querying real-world geographic location

Run successfully in django 5.2.9 and Python 3, with supports from Bootstrap 3, Google Geocoding API, Google Map API, Foursquare Places API, GeoPy, and sqlite3

The Locu API service was shut down in January 2017 and is no longer supported.

## Steps to setup

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

# Start web service
python manage.py runserver
```

## API keys required to run the web service

Check out file `django_geolocator/apis.py` which is used to store the secret API key. You need to apply the valid API keys and put them in this file. Do not expose the secret keys to public.

```python
FOURSQUARE_API_KEY = "<your-own-foursquare-api-key>"
GOOGLE_GEOCODING_API_KEY = "<your-own-google-geocoding-api-key>"
```

Development records in Django 1.8.5 have been moved to `DEPRECATED.md`.
