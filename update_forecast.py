import os
import requests
import json
import pandas as pd
import subprocess

# Configurez Git avec les informations d'identification
git_email = "rivaldi.tristan@orange.fr"
git_name = "TristanRivaldi"

os.system(f"git config --global user.email '{git_email}'")
os.system(f"git config --global user.name '{git_name}'")

# L'URL de l'API
url = "https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&hourly=temperature_2m,precipitation,windspeed_10m"

# Faites une requête vers l'API
response = requests.get(url)

# Vérifiez si la requête a réussi
if response.status_code == 200:
    # Analysez la réponse JSON
    data = response.json()

    # Convertissez les données horaires en un DataFrame pandas
    df = pd.DataFrame(data['hourly'])

    # Convertissez la colonne 'time' en objet de date/heure
    df['time'] = pd.to_datetime(df['time'])

    # Extrayez la date (jour) à partir de la colonne 'time'
    df['date'] = df['time'].dt.date

    # Organiser les données en un format adapté pour le tableau HTML
    daily_data = {}
    for index, row in df.iterrows():
        date = row['date'].strftime('%Y-%m-%d')  # Convertir la date en str
        time = row['time'].strftime('%H:%M')
        temperature = f"{row['temperature_2m']} °C"
        windspeed = f"{row['windspeed_10m']} km/h"
        precipitation = f"{row['precipitation']} mm"

        if date not in daily_data:
            daily_data[date] = []

        daily_data[date].append({
            'time': time,
            'temperature': temperature,
            'windspeed': windspeed,
            'precipitation': precipitation
        })

    # Enregistrez les données dans weather_data.json
    with open('weather_data.json', 'w') as json_file:
        json.dump(daily_data, json_file)

    # Utilisez Git pour ajouter, confirmer et pousser les modifications
    os.system("git add weather_data.json")
    os.system("git commit -m 'Mise à jour des données météorologiques'")
    os.system("git push origin main")
else:
    print("La requête vers l'API a échoué.")

