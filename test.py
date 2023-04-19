# Import Meteostat library
from meteostat import *
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

geolocator = Nominatim(user_agent="my_app")
location = geolocator.geocode("Санкт-Петербург")



#today = datetime.now().date()
#tomorrow = today + timedelta(days=1)
current_date = datetime.now()
today = datetime(current_date.year, current_date.month, current_date.day)

tomorrow = today + timedelta(days=1)


locationP = Point(location.latitude, location.longitude)


# Получаем список станций поблизости с указанием daily_start
stations = Stations()
stations = stations.nearby(location.latitude, location.longitude)

# Получаем данные о погоде за последние 365 дней
data = Daily(locationP, today, tomorrow)
data = data.fetch()

# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()