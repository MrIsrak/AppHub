#import modules
import tkinter
import customtkinter
from geopy.geocoders import Nominatim
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily


#theme settings
customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#create CTk window
window = customtkinter.CTk()  # create CTk window like you do with the Tk window
window.geometry("1200x700")

#create frames
daily_weather = customtkinter.CTkFrame(master=window, width=300, height=700)


#text configuration
Wfont=customtkinter.CTkFont(family='Arial', size=24)
Wfont=('Arial', 36)

defoult = customtkinter.CTkFont(family='Calibri', size=14)
defoult=('Calibri', 14)

#create labels
main_text = customtkinter.CTkLabel(master=window, text="Weather",font=Wfont)
enter_your_city = customtkinter.CTkLabel(master=daily_weather, text="Enter your city",font=defoult)

#create entry
city_entry = customtkinter.CTkEntry(master=daily_weather, font=defoult)

#place entry
city_entry.place(in_=daily_weather,x=80,y=40)

#place frames in window
daily_weather.place(relx=0,rely=0)

#place labels in windows
main_text.place(x=579,y=0)
enter_your_city.place(x=105,y=10)




window.mainloop()