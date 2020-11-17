#!/usr/bin/env python

import requests, json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = input("Ciudad? ")
#CITY = "Santiago"
API_KEY = "1b247b59ad0620f5c2c38c0bfe145faf"
URL = BASE_URL + "q=" + CITY + "&lang=es&appid=" + API_KEY
response = requests.get(URL)
x = response.json()
if x["cod"] != "404":

    #coordenadas
    c = x["coord"]
    long = c["lon"]
    lat = c["lat"]
    pais = x["sys"]["country"]
    print("Condiciones para " + str(CITY) + " " + str(pais))
    print("Ubicación en longitud " + str(long) + " Latitud " + str(lat))

    #general
    y = x["main"]
    temp = y["temp"]
    tempc = int(temp - 273.15)
    tem_min = int(y["temp_min"] - 273.15)
    tem_max = int(y["temp_max"] - 273.15)
    hum = y["humidity"]
    pres = y["pressure"]
    #clouds
    nube = x["clouds"]["all"]
    weather_descr = x["weather"][0]["description"]
    print(" Temperatura actual " + str(tem_min) + "°C - " + str(tem_max) + "°C" + "\n Presión atmosférica " + str(pres) + "hPa" + "\n Humedad " + str(hum) + "%" + "\n " + str(weather_descr) + " " + str(nube) + " % de nubosidad")

   #viento
    w = x["wind"]
    wspeed = w["speed"]
    wdirect = w["deg"]
    print(" Vientos de " + str(wspeed) + "KT desde los " + str(wdirect) + "°")
else:
    print("city not found")