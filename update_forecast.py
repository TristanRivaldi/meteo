import requests
import json
import pandas as pd

# L'URL de l'API
url = 
"https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&hourly=temperature_2m,precipitation,windspeed_10m"

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
    daily_data.columns = ['Température Maximale (°C)', 'Température 
Minimale (°C)', 'Moyenne du Vent (km/h)', 'Précipitations (mm)']

    # Enregistrez les données agrégées dans un fichier JSON
    daily_data.to_json('weather_data.json', orient='index')
else:
    print("La requête vers l'API a échoué.")

