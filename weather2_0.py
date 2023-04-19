import tkinter
import customtkinter
import python_weather
import asyncio
import os

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

#create labels
main_text = customtkinter.CTkLabel(master=window, text="Weather",font=Wfont)

#place frames in window
daily_weather.place(relx=0,rely=0)
main_text.place(x=579,y=0)


window.mainloop()