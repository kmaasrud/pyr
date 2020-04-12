from urllib.request import urlopen
from urllib.parse import quote, urlsplit
from math import sqrt
import csv

HOUR_BY_HOUR_STRINGS = [
    'hour by hour', 'hourbyhour', 'hour_by_hour', 'hourly', 'hour', 'per hour', 'forecast_hour_by_hour',
    'forecast hour by hour'
]

REGULAR_FORECAST_STRINGS = [
    'forecast', 'forecasts', 'regular', 'regular forecast'
]

SOURCES = ['http://fil.nrk.no/yr/viktigestader/noreg.txt', 'http://fil.nrk.no/yr/viktigestader/verda.txt']

def coords(place):
    return [float(place['Lat']), float(place['Lon'])]

def fetch_places(src):
    places = []
    with urlopen(src) as response:
        txt = response.read().decode()[:-2]

    reader = csv.reader(txt.split('\n'), delimiter = '\t')
    headers = next(reader)
    
    for line in reader:
        places.append(
            {header: val for header, val in zip(headers, line)}
        )

    return places

# TODO: Are there quicker ways?
def find_closest(location, list_of_locations):
    coords_to_match = [location.lat, location.lng]
    current_distance = 90
    for place in list_of_locations:
        new_distance = sqrt((float(place['Lat']) - location.lat)**2 + (float(place['Lon']) - location.lng)**2)
        if new_distance < current_distance:
            current_distance = new_distance
            closest = place

    return closest

def decode(forecast_type):
    if forecast_type.lower() in HOUR_BY_HOUR_STRINGS:
        return 'forecast_hour_by_hour'
    elif forecast_type.lower() in REGULAR_FORECAST_STRINGS:
        return 'forecast'
    else:
        raise AssertionError('Forecast type not supported')

def url_from_location(location, forecast_type = 'forecast'):
    if location.country == 'Norway':
        src = SOURCES[0]
        places = fetch_places(src)
        result = find_closest(location, places)
        result = result['Engelsk']
    else:
        src = SOURCES[1]
        places = fetch_places(src)
        result = find_closest(location, places)
        result = result['Lenke til engelsk-XML']

    result = quote(result.split('www.yr.no')[1])
    result = 'http://www.yr.no' + result
    result = result.replace('forecast', decode(forecast_type))

    return result

if __name__ == "__main__":
    pass