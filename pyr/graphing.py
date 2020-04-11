from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt
plt.style.use('./helpers/kmaasrud.mplstyle')
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

    fig, ax = plt.subplots()

    for i in range(len(time) - 1):
        x = [time[i], time[i+1]]
        y = [temp[i], temp[i+1]]
        if y[0] > 0 or y[1] > 0:
            color = "red"
        else:
            color = "blue"
        ax.plot(x, y, color=color)

    ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
    fig.autofmt_xdate()

    ax.set_ylabel('°C')

    plt.show()

if __name__ == "__main__":
    forecast = Forecast('rotnes', forecast_type = 'hour')
    graph(forecast)