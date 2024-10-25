# python3 -m venv mon_environnement
# source mon_environnement/bin/activate
# deactivate
# pip freeze > requirements.txt
# pip install -r requirements.txt
import pycountry
import json
from math import radians, sin, cos, sqrt, atan2
from geopy.geocoders import Nominatim


def init():
    countries = [country.name for country in pycountry.countries]
    import random

    data = {
        "Pays": countries,  # Assurez-vous que 'countries' contient la liste des pays
        "Company": {
            "Europe": [
                {
                    "name": "Air France",
                    "vols": [
                        {
                            "numero_vol": f"AF{random.randint(100, 999)}",
                            "places_disponibles": random.randint(50, 200),
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
    """Calcule la distance en kilomètres entre les capitales de deux pays."""
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Obtenir les coordonnées des capitales des deux pays
    location1 = geolocator.geocode(pays1)
    location2 = geolocator.geocode(pays2)

    if location1 and location2:
        # Extraire les latitudes et longitudes
        lat1, lon1 = location1.latitude, location1.longitude
        lat2, lon2 = location2.latitude, location2.longitude

        # Formule de Haversine
        R = 6371  # Rayon de la Terre en kilomètres
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
        print("Impossible de trouver les coordonnées pour un ou les deux pays.")
        return None


# Exemple d'utilisation


def calculate_flight_price(
    data,
    company_name,
    flight_number,
    pays_depart,
    pays_arrivée,
    duration,
    travel_class="Economy",
    seat_selection=False,
):
    distance = distance_entre_pays(pays_depart, pays_arrivée)
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
data = init()
calculate_flight_price(data, "Air France", "AF123", 3000, 6, "Confort", True)


def enregistrer(data):
    with open("data.json", "w") as fichier:
        json.dump(data, fichier, indent=4)


if __name__ == "__main__":
    print()
    data = init()
    enregistrer(data)

    print("Bienvenu sur notre companie")
    action = input("que voulez vous faire:")
    match (action):
        case "réserver":
            pays_depart = input("entrez le pays de départ : ")
            destination = input("entrez votre destination : ")
            classe = input("selectionnez la classe du voyage : ")
            select_siege = input("voulez vous choisir votre siége: ")
