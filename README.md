# Projet Météo Montpellier

Ce projet vise à fournir des informations météorologiques précises et actualisées pour la ville de Montpellier. En utilisant l'API Open-Meteo, les données sont collectées, traitées et présentées 
aux utilisateurs.

## Aperçu

L'application "Météo Montpellier" offre un moyen simple et efficace de suivre les conditions météorologiques quotidiennes et horaires pour Montpellier. Parmi ses principales fonctionnalités, on 
trouve :

- Affichage des températures maximales et minimales quotidiennes.
- Suivi des précipitations et de la vitesse moyenne du vent.
- Consultation des données météorologiques horaires pour chaque jour, permettant aux utilisateurs de planifier leurs activités en conséquence.

## Fonctionnalités et méthodologie

Le projet comporte plusieurs composants et fonctionnalités essentielles :

1. **Collecte de données :** Un script Python (`update_forecast.py`) est utilisé pour interroger l'API Open-Meteo et récupérer un large éventail de données météorologiques, notamment la température, 
les précipitations et la vitesse du vent.

2. **Traitement des données :** Les données horaires sont agrégées quotidiennement pour calculer la température maximale et minimale, la moyenne de la vitesse du vent et la somme des précipitations. 
Ces informations sont ensuite stockées dans un fichier JSON (`weather_data.json`): Une fois les données enregistrées, le script (`update_forecast.py`) utilise Git pour :

- Ajouter le fichier weather_data.json aux modifications suivantes (git add weather_data.json).
- Faire un commit avec le message "Mise à jour des données météorologiques" (git commit -m 'Mise à jour des données météorologiques').
- Pousser ces modifications vers la branche principale (git push origin main).

3. **Affichage :** Les données sont présentées aux utilisateurs sur une page web, cette page web est configurée dans le fichier `index.html` . Les informations sont organisées dans un tableau, avec des symboles 
visuels pour indiquer les conditions météorologiques (il y a un nuage (`nuage.svg`) avec de la pluie si des précipitations sont attendus dans la journées et un soleil (`soleil.svg`) si il n'y a pas de précipitation). Les images utilisées sont prises sur [freesvg.org](https://freesvg.org).

4. **Détails horaires :** Les utilisateurs ont la possibilité de consulter les détails horaires (pour certaines heures de la journée) des conditions météorologiques pour une journée sélectionnée en cliquant sur la ligne correspondante. Ils peuvent ainsi accéder à la température, le taux de précipitations et la vitesse du vent pour certaines heures. En cliquant deux fois de suite sur la même ligne, le tableau d'origine réapparaît. Dans la colonne Conditions météo l'image `lune.svg` apparait si il fait nuit et si il ne pleut pas et l'image `lune_n.svg` apparait si il fait nuit et qu'il y a des précipitations. Pour les autres heures de la journée, il y a l'image `soleil.svg` si il ne pleut pas et `nuage.svg` si il pleut.

5. **Mises à jour automatiques :** Le projet est conçu pour se mettre à jour automatiquement chaque jour à 6h30, grace au fichier `HULK.yml` qui est dans le dossier Workflow, ce fichier exécute le code `update_forecast.py` à 6h30 tous les jours. De plus le fichier `index.html` charge les données de `weather_data.json` lorsqu'on clique sur l'URL de l'application. L'application et donc mise à jour quotidiennement de manière automatique. 

## Application Web

Vous pouvez accéder à l'application "Météo Montpellier" en suivant ce lien : [Météo Montpellier](https://tristanrivaldi.github.io/meteo/)

## Contributeurs

- [Tristan Rivaldi](mailto:rivaldi.tristan@orange.fr)


