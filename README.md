# Pyr

Pyr is a simple Python weather API, using data from [Yr](https://www.yr.no/). Get access to the forecast for 27 000 significant places all over the world, and easily use the data in your Python applications.

```python
>>> from pyr import Forecast
>>> fc = Forecast('Oslo')
>>> fc.coordinates
(59.9181752006436, 10.7544378094483)
>>> fc[0].temperature
'15'
>>> fc[10].from_time
datetime.datetime(2020, 5, 10, 2, 0)
>>> fc[10].description
'Cloudy'
```

## Installation

Instrall through pip

    pip install pyr

or clone this repository and install locally.

## Usage

Complete documentation is in progress...

## To do

- [ ] Realtime precipitation
- [ ] ASCII weather icons
- [ ] Weather graphs

---

Weather forecast from Yr, delivered by the Norwegian Meteorological Institute and NRK

I have no affiliation with Yr, NRK or The Norwegian Meteorological Institue.