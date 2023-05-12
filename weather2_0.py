#import modules
import tkinter
import customtkinter
from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from geopy.geocoders import Nominatim
from meteostat import Stations
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from meteostat import Point, Daily

#showing the weather information
def get_weather(enter_your_city):

    canvas.get_tk_widget().configure(background='white')

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
    fig = Figure(figsize=(3.5, 3.5), dpi=92)

    

    x = y = range(1, 10)
    ax = fig.add_subplot(111)
    data.plot(y=['tavg', 'tmin', 'tmax'], ax=ax)
    
    # Embed the plot in the Tkinter window
    canvas.figure = fig
    canvas.draw()
    canvas.get_tk_widget().grid(in_=daily_weather, row=4, column=0, padx=6, pady=4)

def clear_graph():
    # Delete all elements on the canvas
    canvas.get_tk_widget().delete("all")
    # Update the canvas
    canvas.get_tk_widget().configure(background='#e0dcdc')
    canvas.draw()
    

#theme settings
customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#create CTk window
window = customtkinter.CTk()  # create CTk window like you do with the Tk window
window.geometry("1200x600")


#create rows and columns
window.columnconfigure(0, weight=1, minsize=200)
window.columnconfigure(1, weight=1, minsize=200)
window.columnconfigure(2, weight=1, minsize=200)
window.columnconfigure(3, weight=1, minsize=200)

window.rowconfigure(0, weight=1, minsize=100)
window.rowconfigure(1, weight=1, minsize=100)
window.rowconfigure(2, weight=1, minsize=100)
window.rowconfigure(3, weight=1, minsize=100)
window.rowconfigure(4, weight=1, minsize=100)



#text configuration
Wfont=customtkinter.CTkFont(family='Arial', size=24)
Wfont=('Arial', 36)

defoult = customtkinter.CTkFont(family='Calibri', size=14)
defoult=('Calibri', 14)

#create frames
daily_weather = customtkinter.CTkFrame(master=window, width=350, height=700)
daily_weather.grid(row=0, column=0, rowspan=5, padx=10, pady=10, sticky="nsw")  # занимает 5 строк, 1 колонку и прижимается к верхнему левому углу

daily_highlight = customtkinter.CTkFrame(master=window, width=830, height=450)
daily_highlight.grid(row=0, column=1, columnspan=3, rowspan=5, padx=10, pady=10, sticky="nsew")  # занимает 5 строк, 3 колонки и прижимается к верхнему правому углу


#create labels
#main_text = customtkinter.CTkLabel(master=daily_highlight, text="Weather", font=Wfont)
#main_text.grid(row=0, column=0, columnspan=4, pady=20, sticky="n")

enter_your_city = customtkinter.CTkLabel(master=daily_weather, text="Enter your city", font=defoult)
enter_your_city.grid(row=0, column=0, padx=10, pady=10)  

#create buttons
show_weather = customtkinter.CTkButton(master=daily_weather, text="Show the weather", command=lambda:get_weather(city_entry))
show_weather.grid(row=2, column=0, pady=10)  

clear_graph = customtkinter.CTkButton(master=daily_weather, text="Clear Graph", command=clear_graph)
clear_graph.grid(row=3, column=0, pady=10)  

#create entry
city_entry = customtkinter.CTkEntry(master=daily_weather, font=defoult)
city_entry.grid(row=1, column=0, pady=10)  

#create tabview
tabview = customtkinter.CTkTabview(master=daily_highlight)
tabview.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)



tabview.add("tab 1")  # add tab at the end
tabview.add("tab 2")  # add tab at the end
tabview.set("tab 1")  # set currently visible tab

#create canvas
canvas = FigureCanvasTkAgg(Figure(figsize=(3.5, 3.5), dpi=92), master=daily_weather)
canvas.draw()
canvas.get_tk_widget().grid(row=4, column=0, padx=6, pady=4)  

#configure grid rows and columns
daily_weather.columnconfigure(0, weight=1, minsize=200)
daily_weather.rowconfigure(4, weight=1, minsize=300, pad=0)

daily_highlight.columnconfigure(0, weight=1,minsize=830)
daily_highlight.rowconfigure(0, weight=1,minsize=450)


window.mainloop()