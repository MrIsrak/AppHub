#import modules
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from geopy.geocoders import Nominatim
from meteostat import Stations
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from meteostat import Point, Daily


#showing the weather information
def get_weather(enter_your_city):
    #entering the city name
    user_text = enter_your_city.get()
    
    #initialazing the location data
    geolocator = Nominatim(user_agent="my_app")
    
    location = geolocator.geocode(user_text)

    # getting date
    current_date = datetime.now()
    today = datetime(current_date.year, current_date.month, current_date.day)
    tomorrow = today + timedelta(days=1)

    #geting location
    location_p = Point(location.latitude, location.longitude)

    # geting list of stations
    stations = Stations()
    stations = stations.nearby(location.latitude, location.longitude)

    # geting weather data
    data = Daily(location_p, today, tomorrow)
    data = data.fetch()

    # Plot line chart including average, minimum and maximum temperature
    fig = Figure(figsize=(3.5, 3), dpi=90)

    x = y = range(1, 10)
    ax = fig.add_subplot(111)
    data.plot(y=['tavg', 'tmin', 'tmax'], ax=ax)
    
    # Embed the plot in the Tkinter window
    canvas.figure = fig
    canvas.draw()
    canvas.get_tk_widget().place(in_=daily_weather, x=6, y=250, width=340, height=250)

def clear_graph():
    # Delete all elements on the canvas
    canvas.get_tk_widget().delete("all")
    # Update the canvas
    canvas.get_tk_widget().configure(background='lightgray')
    canvas.draw()
    