# import the module
import python_weather
import asyncio
import os
import tkinter as tk
import ttkbootstrap as ttk
from ttkthemes import ThemedTk
from ttkbootstrap import *


# create a window and apply theme to window
window = ThemedTk(theme="lumen")
window.geometry("1200x700")

#create a frame
style = ttk.Style()
style.configure('TFrame', background='#FF0000')
daily_weather = ttk.Frame(window)


# Labels for weather

weather_label = ttk.Label(daily_weather, text="Weather")
temp_label = ttk.Label(window, text="Temperature")
wind_label = ttk.Label(window, text="Wind Speed")
humidity_label = ttk.Label(window, text="Humidity")
tip_label = ttk.Label(window, text="Tip", font=("Arial", 12, "italic"))





#place frames
daily_weather.grid(row=0, column=2)
print(1)

#place labels
weather_label.grid(row=0, column=0)
# temp_label.grid(row=1, column=0)
# wind_label.grid(row=2, column=0)
# humidity_label.grid(row=3, column=0)
# tip_label.grid(row=4, column=0)


#place window
window.mainloop()