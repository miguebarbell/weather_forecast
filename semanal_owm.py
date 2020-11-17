#!/usr/bin/env python

import requests, json
from datetime import datetime


# extraer coodenadas de la ciudad
API_KEY = "1b247b59ad0620f5c2c38c0bfe145faf"
CITY = input("ciudad,pais\n")
# CITY = "santiago"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
URLC = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
response = requests.get(URLC)
x = response.json()
if x["cod"] == "404":
    print("ciudad no validada")
else:
    # coodenadas
    long = x["coord"]["lon"]
    lat = x["coord"]["lat"]
    pais = x["sys"]["country"]
    # extraer zona horaria
    base_url = "https://api.openweathermap.org/data/2.5/onecall?lat="
    URL = base_url + str(lat) + "&lon=" + str(long) + "&exclude=&units=metric&lang=es&appid=" + API_KEY
    response = requests.get(URL)
    x = response.json()
    print("\n\nCondiciones para " + CITY + " " + pais)
    print("Ubicación en Longitud " + str(long) + " Latitud " + str(lat))
    desc_actual = x["current"]['weather'][0]['description']
    temp_actual = str(x["current"]['temp'])
    feel_actual = str(x["current"]['feels_like'])
    uvi_actual = str(x["current"]['uvi'])
    print("Condiciones actuales \t:" + feel_actual + "°C " + desc_actual)
    # print(x["current"]["dt"])
    for i in range(3):
        dia = x["daily"][i+1]
        horas = (i+1)*24
        print("\nPRÓXIMAS " + str(horas) + " Horas\n" + str(dia['clouds']) + "% de nubosidad, se pronostica " + str(dia['weather'][0]['description']) + "\nprob. precip\t:" + str(dia['pop']*100) + "%")
        #  "%\nT° mañana\t" + str(dia['temp']['morn']) +
        #  "°C\nT° dia\t\t" + str(dia['temp']['day']) +
        #  "°C\nT° tarde\t" + str(dia['temp']['eve']) +
        #  "°C\nT° noche\t" + str(dia['temp']['night']) +
        #  "°C\nViento\t\t" + str(dia['wind_speed']) + " m/s dirección " + str(dia['wind_deg']) +
        #  "°\nVisibilidad\t" + str(dia['uvi']))
        print("T° Min\t\t:" + str(dia['temp']['min']) + "°C")
        print("T° Max\t\t:" + str(dia['temp']['max']) + "°C")
        print("Indice UV \t:" + str(dia['uvi']) + " uvi")
        print("Vientos\t\t:" + str(dia['wind_speed']) + " m/s dirección " + str(dia['wind_deg']) + "°")
        feel = dia['feels_like']
        min_term = min(dia['feels_like'], key = lambda k:dia['feels_like'][k]) 
        max_term = max(dia['feels_like'], key = lambda k:dia['feels_like'][k])
        print("Sensación térm\t:min " + str(feel[min_term]) + "°C max " + str(feel[max_term]) + "°C")
