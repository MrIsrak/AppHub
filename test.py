# Import Meteostat library
from meteostat import *
from geopy.geocoders import Nominatim
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np


#Получаем локацию (Здесь строкой)
geolocator = Nominatim(user_agent="my_app")
location = geolocator.geocode("Санкт-Петербург")

#Получаем время
current_date = datetime.now()
today = datetime(current_date.year, current_date.month, current_date.day)

tomorrow = today + timedelta(days=1)

#Вводим координаты в переменную для погоды 
locationP = Point(location.latitude, location.longitude)


# Получаем список станций поблизости с указанием daily_start
stations = Stations()
stations = stations.Ф(location.latitude, location.longitude)

# Получаем данные о погоде 
data = Daily(locationP, today, tomorrow)
data = data.fetch()

# рисуем график
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()