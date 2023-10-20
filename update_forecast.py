import requests
import json
import pandas as pd
import os
import subprocess

# Lisez le jeton d'authentification depuis une variable d'environnement
github_token = os.environ.get("TOKEN")

# Configurez Git avec les informations d'identification
git_email = "rivaldi.tristan@orange.fr"
git_name = "TristanRivaldi"

os.system(f"git config --global user.email '{git_email}'")
os.system(f"git config --global user.name '{git_name}'")

# L'URL de l'API
url = "https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&hourly=temperature_2m,precipitation,windspeed_10m"

# Faites une requête vers l'API en incluant le jeton d'authentification dans les en-têtes
headers = {"Authorization": f"token {github_token}"}
response = requests.get(url, headers=headers)

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

    # Convertissez les horodatages Unix en millisecondes en dates (jours)
    daily_data.index = daily_data.index.map(lambda x: x.strftime('%Y-%m-%d'))

    # Enregistrez les données agrégées dans un fichier JSON
    daily_data.to_json('weather_data.json', orient='index')
    # Utilisez Git pour ajouter, confirmer et pousser les modifications
    os.system("git add weather_data.json")
    os.system("git commit -m 'Mise à jour des données météorologiques'")
    os.system("git push origin main")
else:
    print("La requête vers l'API a échoué.")
