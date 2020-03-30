from datetime import datetime

from .helpers import ISO_FORMAT

class Period:
    def __init__(self, element, location):
        self.location = location
        self.from_time = datetime.strptime(element.attrib['from'], ISO_FORMAT)
        self.to_time = datetime.strptime(element.attrib['to'], ISO_FORMAT)
        self.description = element[0].attrib['name']
        self.precipitation = element[1].attrib['value']
        self.precipitation_unit = 'mm'
        self.wind_deg = element[2].attrib['deg']
        self.wind_dir = element[2].attrib['code']
        self.wind_speed = element[3].attrib['mps']
        self.wind_name = element[3].attrib['name']
        self.temperature = element[4].attrib['value']
        self.pressure = element[5].attrib['value']

    def __repr__(self):
        return f'{self.from_time.strftime("%H:%M")}-{self.to_time.strftime("%H:%M")}'

    def __str__(self):
        return (
            f'Forecast for {self.location} from {self.from_time.strftime("%H:%M")} to {self.to_time.strftime("%H:%M")}'
            f'\n{self.to_time.strftime("%A %d %B %Y")}'
            f'\n{self.description}'
            f'\nTemperature: {self.temperature} °C'
            f'\nPrecipitation: {self.precipitation} {self.precipitation_unit}'
            f'\nWind: {self.wind_name} {self.wind_dir}'
            f'\nPressure: {self.pressure} hPa'
        )