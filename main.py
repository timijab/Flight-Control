import pyautogui as py
import webbrowser
import time
import requests
import geopy
import tkinter as tk
from tkinter import Toplevel
from geopy.geocoders import Nominatim
import customtkinter


customtkinter.get_appearance_mode()
main = customtkinter.CTk()
main.geometry("700x700")
main.title("Flight control system")
main.grid_rowconfigure(0, weight=1)
main.grid_columnconfigure(0, weight=1)

box = customtkinter.CTkFrame(master=main, width=500, height=200, corner_radius=10, border_color="#0B2447",
                             border_width=2)
box.grid(row=0, column=0)

label = customtkinter.CTkLabel(master=box, text_color="black", text="Please enter present location here.")
label.grid(row=0, column=0, pady=10, padx=50)

entry_location_1 = customtkinter.CTkEntry(master=box, width=200, height=50, text_color='black')
entry_location_1.grid(row=1, column=0, padx=50, pady=50)

label_2 = customtkinter.CTkLabel(master=box, text_color="black", text="Please enter destination here.")
label_2.grid(row=0, column=1, pady=10, padx=50)

entry_location_2 = customtkinter.CTkEntry(master=box, width=200, height=50, text_color='black')
entry_location_2.grid(row=1, column=1, padx=50, pady=50)

API_KEY = "YOUR API KEY"

def weather_condition():
    """ Provides weather conditions for flight"""
    geolocator = Nominatim(user_agent='MyApp')
    location = geolocator.geocode(entry_location_1.get())
    lat = location.latitude
    lon = location.longitude
    present = customtkinter.CTkFrame(master=main, width=250, height=200, corner_radius=10, border_color="#0B2447",
                             border_width=2)
    present.grid(row=1, column=0)
    present_location = customtkinter.CTkLabel(master=present, font=("Helvetica", 20, "bold"), text=f'Current Location \n Latitude: {lat}\n\nLongitude: {lon}')
    present_location.grid(row=0, column=0, padx=20, pady=30)

    #  second location
    geolocation = Nominatim(user_agent='MyApp')
    location_1 = geolocation.geocode(entry_location_2.get())
    lat_1 = location_1.latitude
    lon_1 = location_1.longitude
    present_location = customtkinter.CTkLabel(master=present,font=("Helvetica", 20, "bold"), text=f' Locked destination Coordinate \n Latitude: {lat_1}\n\nLongitude: {lon_1}')
    present_location.grid(row=0, column=1)

#     flight details
    def weather_info():
        result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
        new_com = result.json()
        # important parts we need
        main_condition = new_com['weather']
        description = new_com['weather']
        temperature = new_com['main']
        feels_like = new_com['main']
        minimum_temperature = new_com['main']
        maximum_temperature = new_com['main']

        wind = new_com['wind']
        clouds = new_com['clouds']
        # pop graphics interface
        pop = Toplevel()
        pop.title("Flight weather Condition")
        pop.geometry("400x500")
        pop.config(bg='white')
        information = customtkinter.CTkLabel(master=pop, font=("Helvetica", 13, "bold"), text=f"Flight condition: {main_condition}\n\n Description: "
                                                              f"{description}\n\n Temperature: {temperature}Celsuis "
                                                              f"\n{feels_like}\n\n Minimum Temperature: "
                                                              f"{minimum_temperature}"
                                                              f"\n\n Wind: {wind}"
                                                              f"\n\n Cloud conditions: {clouds}")
        information.grid(row=0, column=0)

    def initiate_flight():
        """Flight simulator geo-fs"""
        webbrowser.open("https://www.geo-fs.com/")
        time.sleep(10)
        py.click(700, 100)
        # In simulator; use (+) and (-) to set throttle.
        # Mouse is stick: pull mouse down in stick to take-off.
        # C change direction.
        # G- release landing gear and space as landing gear.
        #
        # Taxiing
        # time to hold on to key
        start = time.time()
        while time.time() - start < 100:
            py.hold("9")
        # Takeoff
        py.drag(0, 12, duration=1.5)

    flight_detail_button = customtkinter.CTkButton(master=main, text='Flight Details', border_width=3,
                                                border_color='#b2beb5',
                                                text_color="#0B2447", fg_color='white', height=30, width=200,
                                                hover_color='#b2beb5', command=weather_info)
    flight_detail_button.grid(row=3, columnspan=1, pady=20, padx=10)

    flight_button = customtkinter.CTkButton(master=main, text='Start Flight', border_width=3,
                                                   border_color='#b2beb5',
                                                   text_color="#0B2447", fg_color='white', height=30, width=200,
                                                   hover_color='#b2beb5', command=initiate_flight)
    flight_button.grid(row=4, columnspan=1, pady=20, padx=10)


button_location_1 = customtkinter.CTkButton(master=box, text='Lock in Location', border_width=3, border_color='#b2beb5',
                                            text_color="#0B2447", fg_color='white', height=30, width=200,
                                            hover_color='#b2beb5', command=weather_condition)
button_location_1.grid(rowspan=2, columnspan=1, pady=20, padx=10)






main.mainloop()
