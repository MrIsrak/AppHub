#import modules
import tkinter
import customtkinter


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
    data.plot(y=['tavg', 'tmin', 'tmax'])

    plt.show()
    



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

#create labels
main_text = customtkinter.CTkLabel(master=window, text="Weather",font=Wfont)
enter_your_city = customtkinter.CTkLabel(master=daily_weather, text="Enter your city",font=defoult)

#create buttons
show_weather = customtkinter.CTkButton(master=daily_weather, text="Show the weather", command=lambda:get_weather(city_entry))


#create entry
city_entry = customtkinter.CTkEntry(master=daily_weather, font=defoult)

#place entry
city_entry.place(in_=daily_weather,x=80,y=40)

#place buttons in windows
show_weather.place(in_=daily_weather,x=80,y=80)

#place frames in window
daily_weather.place(relx=0,rely=0)




#place labels in windows
main_text.place(x=579,y=0)
enter_your_city.place(x=105,y=10)




window.mainloop()