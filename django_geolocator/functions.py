import requests

from geopy import geocoders

from .apis import *


def find_city_lat_lng(lat, lng):
    g = geocoders.GoogleV3(api_key = GOOGLE_GEOCODING_API_KEY)
    find = "%s %s" % (lat, lng)
    location = g.geocode(find)
    address = location.raw['address_components']
    city_names = [component['long_name'] 
                 for component in address 
                 if 'locality' in component['types']]
    return city_names[0]


# OBSOLETE
def locu_search(query):
    api = LOCU_API

    url = 'https://api.locu.com/v1_0/venue/search/?'

    local = query

    locality = local.replace(' ', '%20')

    new_url = url + 'api_key=' + api + '&locality=' + locality

    resp = requests.get(new_url)

    resp.raise_for_status()

    results = resp.json()

    locations = [[abc['name'], abc['id']] for abc in results['objects']]

    return locations


# OBSOLETE
def locu_details(locu_id):
    api = LOCU_API

    url = 'https://api.locu.com/v1_0/venue/'

    new_url = url + locu_id + '/?api_key=' + api

    resp = requests.get(new_url)

    resp.raise_for_status()

    results = resp.json()

    for abc in results['objects']:
        details = [abc['lat'], abc['long']]   # Assume only one object returned

    return details



def find_place(query):
    g = geocoders.GoogleV3(api_key = GOOGLE_GEOCODING_API_KEY)
    try:
        place, (lat, lng) = g.geocode(query)
        return place, lat, lng
    except:
        return "", -1, -1


def foursquare_search(query):
    place, lat, lng = find_place(query)

    if place == "" and lat == -1 and lng == -1:
        return []

    url = 'https://places-api.foursquare.com/places/search'

    headers = {
        "X-Places-Api-Version": "2025-06-17",
        "Accept": "application/json",
        "Authorization": f"Bearer {FOURSQUARE_API_KEY}",
    }

    data = {
        "ll": str(lat) + "," + str(lng),
        "radius": 5000,
    }

    resp = requests.get(url, headers=headers, data=data)

    resp.raise_for_status()

    results = resp.json()

    locations = [[abc['name'], abc['fsq_place_id']] for abc in results['results']]

    # for abc in results['results']:
    #     print(abc['name'])
    #     try:
    #         print(f"phone   = {abc['tel']}")
    #     except Exception:
    #         pass
    #     try:
    #         print(f"twitter = {abc['social_media']['twitter']}")
    #     except Exception:
    #         pass
    #     try:
    #         print(f"city    = {abc['location']['locality']}")
    #     except Exception:
    #         pass

    return locations


def foursquare_details(fsq_place_id):
    url = f"https://places-api.foursquare.com/places/{fsq_place_id}"

    headers = {
        "X-Places-Api-Version": "2025-06-17",
        "Authorization": f"Bearer {FOURSQUARE_API_KEY}",
    }

    resp = requests.get(url, headers=headers)

    resp.raise_for_status()

    results = resp.json()

    details = [results['latitude'], results['longitude']]

    return details