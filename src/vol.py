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


def init():
    countries = [country.name for country in pycountry.countries]
    import random

    data = {
        "Pays": countries,
        "reservation": [
            {
                "id_reservation",
                "nombre_personne"
            }
        ],
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
    data,
    company_name,
    flight_number,
    pays_depart,
    pays_arriver,
    duration,
    travel_class="Economy",
    seat_selection=False,
):
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


# Exemple
# data = init()
# calculate_flight_price(data, "Air France", "AF123", 3000, 6, "Confort", True)


def enregistrer(data):
    with open("data.json", "w") as fichier:
        json.dump(data, fichier, indent=4)


# Fonction pour estimer la durée du vol
def estimate_flight_duration(pays_depart, pays_arriver):
    distance = distance_entre_pays(pays_depart, pays_arriver)
    if distance is None:
        return None

    vitesse_moyenne = 900  # Vitesse moyenne d'un vol en km/h
    duration = distance / vitesse_moyenne
    return duration


def book_flight(data):
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
        data,
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
        data,
        compagnie["name"],
        vol["numero_vol"],
        pays_depart,
        pays_arriver,
        duration,
        classe,
        seat_selection=False,
    )

    id_reservation = f"{vol['numero_vol']}-{vol['nombre_reservations']}"

    # Confirmation de réservation
    confirmation = input(
        f"\nLe prix total est de {prix_total:.2f} €. Confirmez-vous la réservation ? (oui/non) : "
    )
    if confirmation.lower() == "oui":
        vol["places_disponibles"] -= nombre_places
        vol["nombre_reservations"] += nombre_places
        data["reservation"].append({
            "id_reservation": id_reservation,
            "nombre_personne": nombre_places
        })
        enregistrer(data)
        print(f"\nRéservation confirmée ! Numéro de réservation : {id_reservation}")
        print(
            f"{nombre_places} places réservées sur le vol {vol['numero_vol']} avec {compagnie['name']} à {prix_total:.2f} €."
        )
        print(f"\nRéservation confirmée ! Numéro de réservation : {id_reservation}")
        print(
            f"{nombre_places} places réservées sur le vol {vol['numero_vol']} avec {compagnie['name']} à {prix_total:.2f} €."
        )
    else:
        print("Réservation annulée.")


# Annulation réservation
def cancel_reservation(data):
    id_reservation = input("Veuillez entrer votre numéro de réservation (ex: AF403-0) : ")

    numero_vol = id_reservation.split('-')[0]

    correspondance_vol = False
    for continent, companies in data["Company"].items():
        for company in companies:
            for vol in company["vols"]:
                if vol["numero_vol"] == numero_vol:
                    correspondance_vol = True

                    confirmation = input(f"Vous êtes sûr de vouloir annuler votre réservation pour le vol {numero_vol} ? (oui/non) : ")
                    if confirmation.lower() == "oui":

                        for reservation in data["reservation"]:
                            if reservation["id_reservation"] == id_reservation:
                                nombre_personne = reservation["nombre_personne"]
                                vol["places_disponibles"] += nombre_personne

                                data["reservation"].remove(reservation)
                                enregistrer(data)
                                print(f"Réservation {id_reservation} annulée. {nombre_personne} place(s) libérée(s).")
                                return
                        print("Aucune réservation trouvée avec ce numéro de réservation.")
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
                print("Action non reconnue. Veuillez choisir parmi les actions disponibles.")

