import tkinter as tk
import requests

from geopy.distance import geodesic

def getDistance(canvas):
    city1 = textfield1.get()
    city2 = textfield2.get()
    api1 = "https://api.openweathermap.org/data/2.5/weather?q=" + city1 + "&appid=266686c4d633ee17a8b1c352e1319d11"
    api2 = "https://api.openweathermap.org/data/2.5/weather?q=" + city2 + "&appid=266686c4d633ee17a8b1c352e1319d11"
    json_data1 = requests.get(api1).json()
    json_data2 = requests.get(api2).json()
    latitude1 = json_data1['coord']['lat']
    longitude1 = json_data1['coord']['lon']
    latitude2 = json_data2['coord']['lat']
    longitude2 = json_data2['coord']['lon']

    # loading the latitude and longitude from two places
    first_place = (latitude1, longitude1)
    second_place = (latitude2, longitude2)
    distance = geodesic(first_place, second_place).km
    distance = "{:.1f}".format(distance)
    final_info = f"The Aerial(flight) distance between {city1} and {city2} is :"
    final_data = str(distance) + " km"
    label1.config(text= final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("AERIAL(FLIGHT) DISTANCE CALCULATOR")

f =("poppins", 14 ,"bold")
t =("poppins", 32 ,"bold")

textfield1 =tk.Entry(canvas,font=t)
textfield2 =tk.Entry(canvas,font=t)

textfield1.pack(pady = 20)
textfield2.pack(pady = 20)
textfield1.focus()
textfield2.focus()
textfield2.bind('<Return>',getDistance)

label1=tk.Label(canvas,font=f)
label1.pack()
label2 = tk.Label(canvas,font = t)
label2.pack()

canvas.mainloop()
