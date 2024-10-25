# python3 -m venv mon_environnement
# source mon_environnement/bin/activate
# deactivate
# pip freeze > requirements.txt
# pip install -r requirements.txt

import pycountry
import json
from math import radians, sin, cos, sqrt, atan2
from geopy.geocoders import Nominatim
from opencage.geocoder import OpenCageGeocode
import os
import random
import csv

from users import init_users, ajouter_utilisateur


def init():
    """
    Initialise et génère une structure de données contenant des informations sur les pays, les compagnies aériennes et les vols disponibles.

    Retourne un dictionnaire avec les éléments suivants :
        - "Pays": Une liste de tous les pays (chaîne de caractères) utilisant `pycountry`.
        - "reservation": Une liste contenant les champs pour une réservation individuelle, incluant :
            - "id_reservation": Identifiant unique pour une réservation (à définir ultérieurement).
            - "nombre_personne": Nombre de personnes associées à une réservation (à définir ultérieurement).
        - "Company": Un dictionnaire organisé par région (Europe, Amérique Latine), chaque région contenant une liste de compagnies aériennes, avec :
            - "name": Le nom de la compagnie aérienne (chaîne de caractères).
            - "vols": Une liste de vols disponibles pour chaque compagnie, où chaque vol comprend :
                - "numero_vol": Numéro du vol (chaîne de caractères, générée aléatoirement).
                - "places_disponibles": Nombre de places disponibles pour le vol (entier aléatoire entre 50 et 200).
                - "nombre_reservations": Nombre de réservations initialisées pour le vol (commence à 0).

    Retourne:
        dict : Un dictionnaire structuré contenant les informations sur les pays, les réservations, les compagnies aériennes, et les vols.
    """
    countries = [country.name for country in pycountry.countries]

    data = {
        "Pays": countries,
        "reservation": [{"id_reservation", "nombre_personne"}],
        "Company": {
            "Europe": [
                {
                    "name": "Air France",
                    "vols": [
                        {
                            "numero_vol": f"AF{random.randint(100, 999)}",
                            "places_disponibles": random.randint(50, 200),
                            "nombre_reservations": 0,
                        }
                        for _ in range(5)
                    ],
                },
                {
                    "name": "British Airways",
                    "vols": [
                        {
                            "numero_vol": f"BA{random.randint(100, 999)}",
                            "places_disponibles": random.randint(50, 200),
                            "nombre_reservations": 0,
                        }
                        for _ in range(5)
                    ],
                },
                {
                    "name": "Lufthansa",
                    "vols": [
                        {
                            "numero_vol": f"LH{random.randint(100, 999)}",
                            "places_disponibles": random.randint(50, 200),
                            "nombre_reservations": 0,
                        }
                        for _ in range(5)
                    ],
                },
                {
                    "name": "KLM Royal Dutch Airlines",
                    "vols": [
                        {
                            "numero_vol": f"KL{random.randint(100, 999)}",
                            "places_disponibles": random.randint(50, 200),
                            "nombre_reservations": 0,
                        }
                        for _ in range(5)
                    ],
                },
                {
                    "name": "Iberia",
                    "vols": [
                        {
                            "numero_vol": f"IB{random.randint(100, 999)}",
                            "places_disponibles": random.randint(50, 200),
                            "nombre_reservations": 0,
                        }
                        for _ in range(5)
                    ],
                },
            ],
            "Amérique Latine": [
                {
                    "name": "LATAM Airlines",
                    "vols": [
                        {
                            "numero_vol": f"LA{random.randint(100, 999)}",
                            "places_disponibles": random.randint(50, 200),
                            "nombre_reservations": 0,
                        }
                        for _ in range(5)
                    ],
                },
                {
                    "name": "Avianca",
                    "vols": [
                        {
                            "numero_vol": f"AV{random.randint(100, 999)}",
                            "places_disponibles": random.randint(50, 200),
                            "nombre_reservations": 0,
                        }
                        for _ in range(5)
                    ],
                },
                {
                    "name": "Aeroméxico",
                    "vols": [
                        {
                            "numero_vol": f"AM{random.randint(100, 999)}",
                            "places_disponibles": random.randint(50, 200),
                            "nombre_reservations": 0,
                        }
                        for _ in range(5)
                    ],
                },
                {
                    "name": "Copa Airlines",
                    "vols": [
                        {
                            "numero_vol": f"CM{random.randint(100, 999)}",
                            "places_disponibles": random.randint(50, 200),
                            "nombre_reservations": 0,
                        }
                        for _ in range(5)
                    ],
                },
                {
                    "name": "Gol Linhas Aéreas",
                    "vols": [
                        {
                            "numero_vol": f"G3{random.randint(100, 999)}",
                            "places_disponibles": random.randint(50, 200),
                            "nombre_reservations": 0,
                        }
                        for _ in range(5)
                    ],
                },
            ],
        },
    }
    return data


# Calcul du prix de vols :
def distance_entre_pays(pays1, pays2):
    """
    Calcule la distance en kilomètres entre deux pays en utilisant leurs noms.

    La fonction utilise l'API OpenCage Geocode pour obtenir les coordonnées géographiques
    (latitude et longitude) des capitales des pays spécifiés, puis applique la formule de Haversine
    pour calculer la distance entre eux en kilomètres.

    Pour utiliser cette fonction, vous devez obtenir une clé API de l'API OpenCage Geocode.

    Étapes pour obtenir une clé API OpenCage:
    1. Allez sur https://opencagedata.com/ et créez un compte en cliquant sur “Sign Up”.
    2. Choisissez le plan gratuit ou un plan payant selon vos besoins.
    3. Une fois inscrit, allez dans votre tableau de bord et récupérez la clé API qui vous est attribuée.
    4. Remplacez la clé dans le code par la vôtre (ligne avec OpenCageGeocode("YOUR_API_KEY")).

    Paramètres:
    pays1 (str): Le nom du premier pays.
    pays2 (str): Le nom du second pays.

    Retourne:
    float: La distance en kilomètres entre les deux pays.
           Retourne None si les coordonnées d'un pays ne sont pas trouvées.
    """
    geocoder = OpenCageGeocode("b5072a154cba4479ba056f5b47d5bd7a")

    # Obtenir les coordonnées des deux pays
    result1 = geocoder.geocode(pays1)
    result2 = geocoder.geocode(pays2)

    if result1 and result2:
        lat1, lon1 = result1[0]["geometry"]["lat"], result1[0]["geometry"]["lng"]
        lat2, lon2 = result2[0]["geometry"]["lat"], result2[0]["geometry"]["lng"]

        # Calcul de la distance
        R = 6371  # Rayon de la Terre en km
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = (
            sin(dlat / 2) ** 2
            + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
        )
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c

        return distance
    else:
        print("Coordonnées non trouvées pour un ou les deux pays.")
        return None


# Calcul de la réservation
def calculate_flight_price(
    company_name,
    flight_number,
    pays_depart,
    pays_arriver,
    duration,
    travel_class,
    seat_selection=False,
):
    """
    Calcule le prix total d'un vol en fonction de la compagnie aérienne, de la distance, de la durée,
    de la classe de voyage et de la sélection de siège.

    La fonction utilise des tarifs de base spécifiques à chaque compagnie, des coefficients pour
    chaque classe de voyage, et des facteurs de coût basés sur la distance et la durée du vol.
    Une option pour ajouter des frais de sélection de siège est également incluse.

    Paramètres:
    company_name (str): Nom de la compagnie aérienne.
    flight_number (str): Numéro du vol.
    pays_depart (str): Pays de départ du vol.
    pays_arriver (str): Pays de destination du vol.
    duration (float): Durée estimée du vol en heures.
    travel_class (str): Classe de voyage, avec options "Economy", "Confort", ou "Business".
    seat_selection (bool, optionnel): Indique si une sélection de siège est effectuée.
                                      Par défaut à False.

    Retourne:
    float: Le prix total calculé du vol en euros.

    Méthode:
    1. Récupère la distance entre les pays de départ et d'arrivée à l'aide de `distance_entre_pays`.
    2. Applique un tarif de base pour la compagnie et ajoute un coût basé sur la distance et la durée.
    3. Multiplie le total par le coefficient de la classe de voyage (Economy, Confort, Business).
    4. Ajoute un frais supplémentaire pour la sélection de siège si `seat_selection` est True.

    Exemples de calcul:
        - Distance Factor: 0.1 €/km
        - Time Factor: 5 €/heure
        - Frais de sélection de siège: 20 € si sélectionné.
    """
    distance = distance_entre_pays(pays_depart, pays_arriver)
    # Tarifs de base pour chaque compagnie
    base_prices = {
        "Air France": 150,
        "British Airways": 180,
        "Lufthansa": 170,
        "KLM Royal Dutch Airlines": 160,
        "Iberia": 140,
        "LATAM Airlines": 130,
        "Avianca": 120,
        "Aeroméxico": 125,
        "Copa Airlines": 110,
        "Gol Linhas Aéreas": 100,
    }

    # Coefficients pour chaque classe de voyage
    class_factors = {"Economy": 1.0, "Confort": 1.2, "Business": 1.5}

    # Facteurs pour calculer le prix final
    distance_factor = 0.1  # Coût par kilomètre
    time_factor = 5  # Coût par heure
    seat_extra_fee = 20 if seat_selection else 0

    # Récupération du tarif de base de la compagnie
    base_price = base_prices.get(company_name, 150)

    # Calcul du prix final
    price = (
        base_price + (distance * distance_factor) + (duration * time_factor)
    ) * class_factors[travel_class] + seat_extra_fee

    # Détails du calcul
    print(f"Compagnie : {company_name}, Vol : {flight_number}")
    print(f"Distance : {distance} km, Durée : {duration} heures")
    print(
        f"Classe : {travel_class}, Sélection de siège : {'Oui' if seat_selection else 'Non'}"
    )
    print(f"Prix calculé : {price:.2f} €")

    return price


def enregistrer(data):
    """
    Enregistre les données fournies dans un fichier JSON nommé 'data.json'.

    Cette fonction prend un dictionnaire ou une structure de données en Python
    et l'enregistre sous forme de fichier JSON avec une indentation de 4 espaces
    pour améliorer la lisibilité.

    Paramètres:
    data (dict): Les données à enregistrer, sous forme de dictionnaire ou d'autre structure JSON-serializable.

    Effets:
    Crée un fichier 'data.json' dans le répertoire courant, écrasant tout fichier du même nom existant.
    """
    with open("data.json", "w") as fichier:
        json.dump(data, fichier, indent=4)


# Fonction pour estimer la durée du vol
def estimate_flight_duration(pays_depart, pays_arriver):
    """
    Estime la durée d'un vol en heures entre deux pays en fonction de la distance qui les sépare.

    La fonction utilise `distance_entre_pays` pour calculer la distance en kilomètres entre
    les pays de départ et d'arrivée, puis divise cette distance par une vitesse moyenne de vol
    (900 km/h) pour obtenir une estimation de la durée du vol.

    Paramètres:
    pays_depart (str): Le nom du pays de départ.
    pays_arriver (str): Le nom du pays d'arrivée.

    Retourne:
    float: La durée estimée du vol en heures.
           Retourne None si la distance ne peut pas être calculée.
    """
    distance = distance_entre_pays(pays_depart, pays_arriver)
    if distance is None:
        return None

    vitesse_moyenne = 900  # Vitesse moyenne d'un vol en km/h
    duration = distance / vitesse_moyenne
    return duration



def save_to_csv(booking_data, filename='reservations.csv'):
    """
    Enregistre les informations de réservation dans un fichier CSV.

    Paramètres:
    booking_data (dict): Dictionnaire contenant les informations de réservation.
    filename (str): Le nom du fichier CSV dans lequel les données seront enregistrées.
    """
    fieldnames = ['id_reservation', 'first_name', 'last_name', 'email', 'phone_number', 'pays_depart', 'pays_arriver', 'classe', 'prix_total']
    
    # Vérifie si le fichier existe déjà pour écrire l'en-tête
    file_exists = False
    try:
        with open(filename, 'r'):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Écrire l'en-tête seulement si le fichier n'existe pas encore
        if not file_exists:
            writer.writeheader()

        writer.writerow(booking_data)



def book_flight(data):
    """
    Permet à un utilisateur de réserver un vol en suivant un processus interactif.

    Cette fonction guide l'utilisateur à travers les étapes de réservation d'un vol :
        1. Sélection du pays de départ et du pays d'arrivée.
        2. Choix du continent, de la compagnie aérienne et du vol.
        3. Sélection du nombre de places et de la classe de voyage.
        4. Calcul du prix total et confirmation de la réservation.

    Une fois la réservation confirmée, les informations de réservation sont enregistrées
    et un billet de vol est généré avec les détails du vol.

    Paramètres:
    data (dict): Dictionnaire contenant les données des pays, des compagnies aériennes et des vols disponibles.

    Retourne:
    None
    """
    # Étape 1 : Pays de départ et d'arrivée
    pays_depart = input("De quel pays voulez-vous partir ? ")
    pays_arriver = input("Vers quel pays voulez-vous arriver ? ")

    # Étape 2 : Choix du continent
    while True:
        continents = list(data["Company"].keys())
        print("Sélectionnez le continent :")
        for i, continent in enumerate(continents, 1):
            print(f"{i}. {continent}")

        try:
            continent_choice = int(input("Entrez le numéro du continent : ")) - 1
            if 0 <= continent_choice < len(continents):
                continent = continents[continent_choice]
                break
            else:
                print("Continent non disponible.")
                if (
                    input("Voulez-vous faire un autre choix ? (oui/non) : ").lower()
                    != "oui"
                ):
                    print("Réservation annulée.")
                    return
        except ValueError:
            print("Veuillez entrer un numéro valide.")

    # Étape 3 : Choix de la compagnie
    while True:
        companies = data["Company"][continent]
        print("\nCompagnies disponibles :")
        for i, company in enumerate(companies, 1):
            print(f"{i}. {company['name']}")

        try:
            company_choice = (
                int(input("Entrez le numéro de la compagnie aérienne : ")) - 1
            )
            if 0 <= company_choice < len(companies):
                compagnie = companies[company_choice]
                break
            else:
                print("Compagnie non disponible.")
                if (
                    input("Voulez-vous faire un autre choix ? (oui/non) : ").lower()
                    != "oui"
                ):
                    print("Réservation annulée.")
                    return
        except ValueError:
            print("Veuillez entrer un numéro valide.")

    # Étape 4 : Choix du vol
    while True:
        print("\nVols disponibles :")
        for i, vol in enumerate(compagnie["vols"], 1):
            print(
                f"{i}. Numéro de vol : {vol['numero_vol']}, Places disponibles : {vol['places_disponibles']}"
            )

        try:
            vol_choice = int(input("Entrez le numéro du vol : ")) - 1
            if 0 <= vol_choice < len(compagnie["vols"]):
                vol = compagnie["vols"][vol_choice]
                break
            else:
                print("Numéro de vol incorrect.")
                if (
                    input("Voulez-vous faire un autre choix ? (oui/non) : ").lower()
                    != "oui"
                ):
                    print("Réservation annulée.")
                    return
        except ValueError:
            print("Veuillez entrer un numéro valide.")

    # Étape 5 : Nombre de places
    while True:
        try:
            nombre_places = int(input("\nCombien de places voulez-vous réserver ? "))
            if nombre_places <= vol["places_disponibles"]:
                break
            else:
                print("Désolé, il n'y a pas assez de places disponibles.")
                if (
                    input("Voulez-vous choisir un autre nombre ? (oui/non) : ").lower()
                    != "oui"
                ):
                    print("Réservation annulée.")
                    return
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    # Étape 6 : Sélection de la classe
    classes = ["Economy", "Confort", "Business"]
    while True:
        print("\nSélectionnez la classe :")
        for i, cls in enumerate(classes, 1):
            print(f"{i}. {cls}")

        try:
            class_choice = int(input("Entrez le numéro de la classe : ")) - 1
            if 0 <= class_choice < len(classes):
                classe = classes[class_choice]
                break
            else:
                print("Classe incorrecte.")
                if (
                    input("Voulez-vous choisir une autre classe ? (oui/non) : ").lower()
                    != "oui"
                ):
                    print("Réservation annulée.")
                    return
        except ValueError:
            print("Veuillez entrer un numéro valide.")

    # Calcul du prix et numéro de réservation
    duration = estimate_flight_duration(pays_depart, pays_arriver)
    prix_total = calculate_flight_price(
        compagnie["name"],
        vol["numero_vol"],
        pays_depart,
        pays_arriver,
        duration,
        classe,
        seat_selection=False,
    )

    id_reservation = f"{vol['numero_vol']}-{vol['nombre_reservations'] + 1}"
    prix_total = calculate_flight_price(
        compagnie["name"],
        vol["numero_vol"],
        pays_depart,
        pays_arriver,
        duration,
        classe,
        seat_selection=False,
    )

    id_reservation = f"{vol['numero_vol']}-{vol['nombre_reservations']}"

    # Information users
    first_name = input("Entrez votre prénom : ")
    last_name = input("Entrez votre nom : ")
    email = input("Entrez votre email : ")
    phone_number = input("Entrez votre numéro de téléphone : ")

    users_data = init_users()

    # Confirmation de réservation
    confirmation = input(
        f"\nLe prix total est de {prix_total:.2f} €. Confirmez-vous la réservation ? (oui/non) : "
    )
    if confirmation.lower() == "oui":
        vol["places_disponibles"] -= nombre_places
        vol["nombre_reservations"] += nombre_places
        data["reservation"].append(
            {"id_reservation": id_reservation, "nombre_personne": nombre_places}
        )

        
        booking_data = {
            'id_reservation': id_reservation,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone_number': phone_number,
            'pays_depart': pays_depart,
            'pays_arriver': pays_arriver,
            'classe': classe,
            'prix_total': prix_total
        }

        # Enregistrer les informations de réservation dans le fichier CSV
        save_to_csv(booking_data)
        enregistrer(data)
        ajouter_utilisateur(
            users_data, first_name, last_name, email, phone_number, id_reservation
        )

        print(f"\nRéservation confirmée ! Numéro de réservation : {id_reservation}")
        print(
            f"""
    ===============================
            Billet de Vol         
    ===============================

    Départ       : {pays_depart}
    Destination  : {pays_arriver}
    Durée        : {int(duration)} heures
    Classe       : {classe}
    Prix Total   : {int(prix_total)} €

    ===============================
    Merci d'avoir choisi notre service !
    ===============================
    """
        )

    else:
        print("Réservation annulée.")


# Annulation réservation
def cancel_reservation(data):
    """
    Permet à un utilisateur d'annuler une réservation existante en utilisant un numéro de réservation.

    La fonction recherche le vol associé au numéro de réservation fourni par l'utilisateur,
    vérifie la confirmation de l'annulation et, si elle est confirmée, libère les places réservées
    et met à jour les données en conséquence.

    Si aucune réservation ne correspond au numéro fourni, un message d'erreur est affiché.

    Paramètres:
    data (dict): Dictionnaire contenant les informations de réservation et les détails des vols.

    Retourne:
    None
    """
    id_reservation = input(
        "Veuillez entrer votre numéro de réservation (ex: AF403-0) : "
    )

    numero_vol = id_reservation.split("-")[0]

    correspondance_vol = False
    for continent, companies in data["Company"].items():
        for company in companies:
            for vol in company["vols"]:
                if vol["numero_vol"] == numero_vol:
                    correspondance_vol = True

                    confirmation = input(
                        f"Vous êtes sûr de vouloir annuler votre réservation pour le vol {numero_vol} ? (oui/non) : "
                    )
                    if confirmation.lower() == "oui":

                        for reservation in data["reservation"]:
                            if reservation["id_reservation"] == id_reservation:
                                nombre_personne = reservation["nombre_personne"]
                                vol["places_disponibles"] += nombre_personne

                                data["reservation"].remove(reservation)
                                enregistrer(data)
                                print(
                                    f"Réservation {id_reservation} annulée. {nombre_personne} place(s) libérée(s)."
                                )
                                return
                        print(
                            "Aucune réservation trouvée avec ce numéro de réservation."
                        )
                    else:
                        print("Annulation de réservation annulée.")
                    return

    if not correspondance_vol:
        print("Numéro de vol introuvable.")


def charger_donnees():
    # Vérifiez si le fichier existe
    if os.path.exists("data.json"):
        # Charger les données existantes
        with open("data.json", "r") as fichier:
            return json.load(fichier)
    else:
        # Si le fichier n'existe pas, créez les données initiales et les sauvegardez dans le fichier JSON
        data = init()
        enregistrer(data)
        return data


if __name__ == "__main__":
    """
    Programme principal pour la gestion des réservations de vols.

    Ce programme permet à l'utilisateur de :
        1. Réserver un vol.
        2. Annuler une réservation existante.
        3. Quitter le programme.

    Le programme charge les données nécessaires, puis affiche un menu interactif
    permettant à l'utilisateur de choisir une action. Chaque action est associée
    à une fonction spécifique pour gérer les réservations et les annulations.

    Actions:
    - "1" : Lance la fonction `book_flight(data)` pour réserver un vol.
    - "2" : Lance la fonction `cancel_reservation(data)` pour annuler une réservation.
    - "3" : Quitte le programme.
    """
    data = charger_donnees()
    print("Bienvenue sur notre compagnie")
    while True:
        print("\nActions disponibles :")
        print("1. Réserver un vol")
        print("2. Annuler une réservation")
        print("3. Quitter")

        action = input("Que voulez-vous faire (tapez le numéro correspondant) : ")

        match action:
            case "1":
                book_flight(data)
            case "2":
                cancel_reservation(data)
            case "3":
                print("Merci pour votre visite ! À bientôt")
                break
            case _:
                print(
                    "Action non reconnue. Veuillez choisir parmi les actions disponibles."
                )
