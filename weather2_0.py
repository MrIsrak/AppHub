#import modules
import tkinter
import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



#showing the weather information
def get_weather(enter_your_city):
    #import modules
    from geopy.geocoders import Nominatim
    from meteostat import Stations
    from datetime import datetime, timedelta
    import matplotlib.pyplot as plt
    from meteostat import Point, Daily
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
    fig = Figure(figsize=(4, 3), dpi=90)
    #fig.get_tk_widget().configure(background=customtkinter.get_color('blue', 'background'))
    x = y = range(1, 10)
    ax = fig.add_subplot(111)
    data.plot(y=['tavg', 'tmin', 'tmax'], ax=ax)
    
    # Embed the plot in the Tkinter window
    canvas.figure = fig
    canvas.draw()
    canvas.get_tk_widget().place(in_=daily_weather,x=6, y=250)
    

def clear_graph():
    # Delete all elements on the canvas
    canvas.get_tk_widget().delete("all")
    # Update the canvas
    canvas.draw()
    


#theme settings
customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#create CTk window
window = customtkinter.CTk()  # create CTk window like you do with the Tk window
window.geometry("1200x700")

#text configuration
Wfont=customtkinter.CTkFont(family='Arial', size=24)
Wfont=('Arial', 36)

defoult = customtkinter.CTkFont(family='Calibri', size=14)
defoult=('Calibri', 14)


#create frames
daily_weather = customtkinter.CTkFrame(master=window, width=300, height=700)

daily_highlight = customtkinter.CTkFrame(master=window, width=880, height=450)

#create labels
main_text = customtkinter.CTkLabel(master=window, text="Weather",font=Wfont)
enter_your_city = customtkinter.CTkLabel(master=daily_weather, text="Enter your city",font=defoult)

#create buttons
show_weather = customtkinter.CTkButton(master=daily_weather, text="Show the weather", command=lambda:get_weather(city_entry))
clear_graph = customtkinter.CTkButton(master=daily_weather, text="Clear Graph", command=clear_graph)

#create entry
city_entry = customtkinter.CTkEntry(master=daily_weather, font=defoult)

#create canvas
canvas = FigureCanvasTkAgg(Figure(figsize=(4, 3), dpi=90), master=window)

#place entry
city_entry.place(in_=daily_weather,x=80,y=40)

#place buttons in windows
show_weather.place(in_=daily_weather,x=80,y=85)
clear_graph.place(in_=daily_weather,x=80,y=120)

#place frames in window
daily_weather.place(relx=0,rely=0)

daily_highlight.place(x=309,y=245)


#place labels in windows
main_text.place(x=579,y=0)
enter_your_city.place(x=105,y=10)




window.mainloop()