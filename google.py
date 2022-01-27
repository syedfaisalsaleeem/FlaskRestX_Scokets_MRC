import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ.get("apikey")

import googlemaps
import requests

def getaddress(lat,long):
    gmaps = googlemaps.Client(key=apikey)

    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((lat, long))
    return reverse_geocode_result


def getdistanceandtime(position1,position2):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&units=imperial&key={}".format(position1,position2,apikey)

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


