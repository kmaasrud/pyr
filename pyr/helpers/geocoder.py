from urllib.request import urlopen
from urllib.parse import quote
import json
from pprint import pformat

GOOGLE_API_KEY = 'AIzaSyA272NouHuizItQDZUQ_vTkikUImEyL4dM'

GOOGLE_GEOCODER_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

class Location:
    def __init__(self, search = None, latlng = None):
        assert search or latlng, "Location object takes either 'search' or 'latlng' keyword arguments."
        if search:
            search = quote(search.replace(' ', '+'))
            url = f'{GOOGLE_GEOCODER_URL}?address={search}&key={GOOGLE_API_KEY}'
        elif latlng:
            url = f'{GOOGLE_GEOCODER_URL}?latlng={str(latlng[0])},{str(latlng[1])}&key={GOOGLE_API_KEY}'

        with urlopen(url) as request:
            response = json.load(request)['results'][0]

        for component in response['address_components']:
            setattr(self, component['types'][0], component['long_name'])

        self.formatted_address = response['formatted_address']
        self.lat = response['geometry']['location']['lat']
        self.lng = response['geometry']['location']['lng']
        self.coordinates = [self.lat, self.lng]

    def __repr__(self):
        return self.formatted_address

    def __str__(self):
        return pformat(vars(self))

if __name__ == "__main__":
    pass