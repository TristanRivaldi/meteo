import os
import requests
import json
import pandas as pd
import subprocess
from datetime import date

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

    # Agrégation des données par jour
    daily_data = df.groupby('date').agg({
        'temperature_2m': ['max', 'min'],
        'windspeed_10m': 'mean',
        'precipitation': 'sum'
    })

    # Renommez les colonnes pour plus de clarté
    daily_data.columns = ['Température Maximale (°C)', 'Température Minimale (°C)', 'Moyenne du Vent (km/h)', 'Précipitations (mm)']

    # Créez un dictionnaire pour stocker les données horaires par jour
    hourly_data = df.groupby('date').apply(lambda x: x[['time', 'temperature_2m', 'windspeed_10m', 'precipitation']].to_dict(orient='records')).to_dict()

    # Convertissez les dates en chaînes de caractères
    daily_data.index = daily_data.index.map(lambda x: x.strftime('%Y-%m-%d'))
    hourly_data = {date.strftime('%Y-%m-%d'): data for date, data in hourly_data.items()}

    # Enregistrez les données agrégées dans un fichier JSON
    data_to_save = {
        "daily_data": daily_data.to_dict(orient='index'),
        "hourly_data": hourly_data
    }

    with open('weather_data.json', 'w') as json_file:
        json.dump(data_to_save, json_file)

    # Utilisez Git pour ajouter, confirmer et pousser les modifications
    os.system("git add weather_data.json")
    os.system("git commit -m 'Mise à jour des données météorologiques'")
    os.system("git push origin main")
else:
    print("La requête vers l'API a échoué.")

