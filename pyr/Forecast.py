from urllib.request import urlopen
import xml.etree.ElementTree as ET

from . import Period
from .helpers import url_from_location, Location

FORECAST_TYPES = ['forecast', 'hour by hour']

class Forecast:
    def __init__(self, search, forecast_type = 'forecast'):
        assert forecast_type in FORECAST_TYPES, f'{forecast_type} not a supported forecast type.'
        self.search = search
        self._forecast_type = forecast_type        
        self.location = search

# ---------------------------------------------------------------------------
    
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, search):
        location = Location(search)

        self.url = url_from_location(location, forecast_type = self._forecast_type)
        with urlopen(self.url) as response:
            root = ET.parse(response).getroot()

        self._location = root[0][0].text
        self.country = root[0][2].text
        self.altitude = root[0][4].attrib['altitude']
        self.coordinates = (
            float(root[0][4].attrib['latitude']),
            float(root[0][4].attrib['longitude'])
        )

        self._forecast = []
        data = root.iter('time')
        next(data)
        for time in data:
            period = Period(time, self._location)
            self._forecast.append(period)

# ---------------------------------------------------------------------------

    @property
    def forecast_type(self):
        return self._forecast_type

    @forecast_type.setter
    def forecast_type(self, forecast_type):
        assert forecast_type in FORECAST_TYPES, f'{forecast_type} not a supported forecast type.'
        self._forecast_type = forecast_type
        self.location = self.search

# ---------------------------------------------------------------------------

    def __getitem__(self, index):
        return self._forecast[index]

    def __len__(self):
        return len(self._forecast)

    def __repr__(self):
        return self.location

    def __str__(self):
        if self.forecast_type == 'forecast':
            return f'Forecast for {self.location}'
        return f'Hour by hour forecast for {self.location}'