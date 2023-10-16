import requests
import json

# L'URL de l'API
url = 
"https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&hourly=temperature_2m,precipitation,windspeed_10m"

# Faites une requête vers l'API
response = requests.get(url)

# Vérifiez si la requête a réussi
if response.status_code == 200:
    # Analysez la réponse JSON
    data = response.json()

    # Enregistrez les données directement dans le fichier JSON sur GitHub
    with open('weather_data.json', 'w') as json_file:
        json.dump(data, json_file)
else:
    print("La requête vers l'API a échoué.")

