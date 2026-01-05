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

Check out file `django_geolocator/apis.py` which is used to stored the secret API key. You need to apply the valid API keys and put them in this file. Do not expose the secret keys to public.

```python
FOURSQUARE_API_KEY = "<your-own-foursquare-api-key>"
GOOGLE_GEOCODING_API_KEY = "<your-own-google-geocoding-api-key>"
```

## Deprecated minor versions for Django 1.8.5

Ver.1   [Start Project, Setup Settings, and Static](../../tree/d4aaafd8953cd07859ddbf9bb1517b6958fc862a)

Ver.2   [Locu Search](../../tree/b8179c09e0b343a776cec7033b78bb9b9bcdfa36)

Ver.3   [Foursquare Search](../../tree/7190932c4acc7c0f8d2bebe7ddb2c91a56e3708d)

Ver.4   [Setup Location App & Url](../../tree/c3696c0e1aff32dc9a874f7e026eb1a88ea1d398)

Ver.5   [Implement Bootstrap](../../tree/e92fef1641b525dbf99c0ef17f17a0b585113b88)

Ver.6   [Location Details with Locu & Setup Google Maps](../../tree/7e7db2f3cee82dd8775a85a50f15862e727b9179)

Ver.7   [Location Details with Foursquare](../../tree/b4c8075c9b2ef91d64ebf795848cc385312433fa)

Ver.8   [Get User's Location](../../tree/305327b4c4dd948c4cff703d27fdfa2b443f718a)

Ver.9   [User Location in Views](../../tree/3327de2f4b69a56196f3bbff21a61f91bbf38597)