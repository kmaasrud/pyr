from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from scipy.interpolate import make_interp_spline
import numpy as np

from datetime import datetime, timedelta

from pyr import Forecast

def graph(forecast):
    now = datetime.now()

    time = []
    temp = []
    for period in forecast.forecast:
        time_from_now = (period.from_time - now).days * 86400
        time_from_now += (period.from_time - now).seconds
        time_from_now /= 3600
        time.append(period.from_time)
        temp.append(float(period.temperature))

    # t = np.linspace(time[0], time[-1], 300)
    # smoothed = make_interp_spline(time, temp)
    # T = smoothed(t)

    fig, ax = plt.subplots()

    ax.plot(time, temp)

    ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
    fig.autofmt_xdate()

    ax.set_xlabel('Hours')
    ax.set_ylabel('Temperature (°C)')

    plt.show()

if __name__ == "__main__":
    forecast = Forecast('rotnes', forecast_type = 'hour')
    graph(forecast)