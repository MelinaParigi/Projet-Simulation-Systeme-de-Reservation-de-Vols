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


def init():
    countries = [country.name for country in pycountry.countries]
    import random

    data = {
        "Pays": countries,
        "id_reservation": [],  # Assurez-vous que 'countries' contient la liste des pays
        "Company": {
            "Europe": [
                {
                    "name": "Air France",
                    "vols": [
                        {
                            "numero_vol": f"AF{random.randint(100, 999)}",
                            "places_disponibles": random.randint(50, 200),
                            "nombre_reservations": 0
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
                            "nombre_reservations": 0
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
                            "nombre_reservations": 0
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
                            "nombre_reservations": 0
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
                            "nombre_reservations": 0
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
                            "nombre_reservations": 0
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
                            "nombre_reservations": 0
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
                            "nombre_reservations": 0
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
                            "nombre_reservations": 0
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
                            "nombre_reservations": 0
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
                if input("Voulez-vous faire un autre choix ? (oui/non) : ").lower() != "oui":
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
            company_choice = int(input("Entrez le numéro de la compagnie aérienne : ")) - 1
            if 0 <= company_choice < len(companies):
                compagnie = companies[company_choice]
                break
            else:
                print("Compagnie non disponible.")
                if input("Voulez-vous faire un autre choix ? (oui/non) : ").lower() != "oui":
                    print("Réservation annulée.")
                    return
        except ValueError:
            print("Veuillez entrer un numéro valide.")
    
    # Étape 4 : Choix du vol
    while True:
        print("\nVols disponibles :")
        for i, vol in enumerate(compagnie["vols"], 1):
            print(f"{i}. Numéro de vol : {vol['numero_vol']}, Places disponibles : {vol['places_disponibles']}")
        
        try:
            vol_choice = int(input("Entrez le numéro du vol : ")) - 1
            if 0 <= vol_choice < len(compagnie["vols"]):
                vol = compagnie["vols"][vol_choice]
                break
            else:
                print("Numéro de vol incorrect.")
                if input("Voulez-vous faire un autre choix ? (oui/non) : ").lower() != "oui":
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
                if input("Voulez-vous choisir un autre nombre ? (oui/non) : ").lower() != "oui":
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
                if input("Voulez-vous choisir une autre classe ? (oui/non) : ").lower() != "oui":
                    print("Réservation annulée.")
                    return
        except ValueError:
            print("Veuillez entrer un numéro valide.")

    # Calcul du prix et numéro de réservation
    duration = estimate_flight_duration(pays_depart, pays_arriver)
    prix_total = calculate_flight_price(data, compagnie["name"], vol["numero_vol"], pays_depart, pays_arriver, duration, classe, seat_selection=False)
    
    id_reservation = f"{vol['numero_vol']}-{vol['nombre_reservations'] + 1}"

    # Confirmation de réservation
    confirmation = input(f"\nLe prix total est de {prix_total:.2f} €. Confirmez-vous la réservation ? (oui/non) : ")
    if confirmation.lower() == "oui":
        vol["places_disponibles"] -= nombre_places
        vol["nombre_reservations"] += 1
        enregistrer(data)
        print(f"\nRéservation confirmée ! Numéro de réservation : {id_reservation}")
        print(f"{nombre_places} places réservées sur le vol {vol['numero_vol']} avec {compagnie['name']} à {prix_total:.2f} €.")
    else:
        print("Réservation annulée.")

def cancel_reservation(data):
    # Étape 1 : Renseignement du numéro de vol et de réservation
    numero_vol = input("Entrez le numéro de vol pour annuler la réservation (ex: AF754) : ")
    id_reservation = input("Entrez le numéro de réservation complet (ex: AF754-1) : ")

    # Recherche de la compagnie et du vol correspondant
    for continent, companies in data["Company"].items():
        for compagnie in companies:
            for vol in compagnie["vols"]:
                # Vérifie si le numéro de vol correspond
                if vol["numero_vol"] == numero_vol:
                    # Étape 2 : Vérifie si la réservation existe
                    print("id_reservation", id_reservation)
                    if f"{numero_vol}-{vol['nombre_reservations']}" == id_reservation:
                        try:
                            # Demander le nombre de places pour cette réservation
                            nombre_places = int(input("Combien de places avez-vous réservé pour cette réservation ? "))

                            # Étape 3 : Libérer les sièges et décrémenter le compteur de réservations
                            vol["places_disponibles"] += nombre_places
                            vol["nombre_reservations"] -= 1  # Décrémenter le nombre de réservations

                            # Confirmation d'annulation
                            enregistrer(data)  # Enregistrement des données mises à jour
                            print(f"La réservation {id_reservation} a été annulée avec succès.")
                            return
                        except ValueError:
                            print("Le nombre de places entré est incorrect.")
                            return
                    else:
                        print("La réservation spécifiée n'existe pas ou a déjà été annulée.")
                        return

    # Si aucune correspondance n'a été trouvée
    print("Aucun vol ou réservation correspondante trouvée.")


if __name__ == "__main__":
    print()
    data = init()
    enregistrer(data)

    print("Bienvenu sur notre companie")
    action = input("que voulez vous faire:")
    match (action):
        case "réserver":
            book_flight(data)
            # pays_depart = input("entrez le pays de départ : ")
            # destination = input("entrez votre destination : ")
            # classe = input("selectionnez la classe du voyage : ")
        case "annuler":
            cancel_reservation(data)
        # case "modifer":
