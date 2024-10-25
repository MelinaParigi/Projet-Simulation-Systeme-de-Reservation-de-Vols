# python3 -m venv mon_environnement
# source mon_environnement/bin/activate
# deactivate
# pip freeze > requirements.txt
# pip install -r requirements.txt
import pycountry
import json


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

def calculate_flight_price(data, company_name, flight_number, distance, duration, travel_class="Economy", seat_selection=False):
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
        "Gol Linhas Aéreas": 100
    }
    
    # Coefficients pour chaque classe de voyage
    class_factors = {
        "Economy": 1.0,
        "Confort": 1.2,
        "Business": 1.5
    }
    
    # Facteurs pour calculer le prix final
    distance_factor = 0.1  # Coût par kilomètre
    time_factor = 5  # Coût par heure
    seat_extra_fee = 20 if seat_selection else 0
    
    # Récupération du tarif de base de la compagnie
    base_price = base_prices.get(company_name, 150)
    
    # Calcul du prix final
    price = (base_price + (distance * distance_factor) + (duration * time_factor)) * class_factors[travel_class] + seat_extra_fee
    
    # Détails du calcul
    print(f"Compagnie : {company_name}, Vol : {flight_number}")
    print(f"Distance : {distance} km, Durée : {duration} heures")
    print(f"Classe : {travel_class}, Sélection de siège : {'Oui' if seat_selection else 'Non'}")
    print(f"Prix calculé : {price:.2f} €")
    
    return price

# Exemple 
# data = init()
# calculate_flight_price(data, "Air France", "AF123", 3000, 6, "Confort", True)


def enregistrer(data):
    with open("data.json", "w") as fichier:
        json.dump(data, fichier, indent=4)


# Fonction de réservation du vol
def book_flight(data):
    while True: 
        # Sélection du continent
        continents = list(data["Company"].keys())
        print("Sélectionnez le continent :")
        for i, continent in enumerate(continents, 1):
            print(f"{i}. {continent}")
        continent_choice = int(input("Entrez le numéro du continent : ")) - 1
        
        if continent_choice < 0 or continent_choice >= len(continents):
            print("Continent non disponible. Voulez-vous réessayer ? (oui/non)")
            if input().lower() != "oui":
                print("Réservation annulée.")
                return
            continue
        
        continent = continents[continent_choice]
        companies = data["Company"][continent]
        
        # Sélection de la compagnie
        print("\nCompagnies disponibles :")
        for i, company in enumerate(companies, 1):
            print(f"{i}. {company['name']}")
        company_choice = int(input("Entrez le numéro de la compagnie aérienne : ")) - 1
        
        if company_choice < 0 or company_choice >= len(companies):
            print("Compagnie non disponible. Voulez-vous réessayer ? (oui/non)")
            if input().lower() != "oui":
                print("Réservation annulée.")
                return
            continue
        
        compagnie = companies[company_choice]

        # Sélection du vol
        print("\nVols disponibles :")
        for i, vol in enumerate(compagnie["vols"], 1):
            print(f"{i}. Numéro de vol : {vol['numero_vol']}, Places disponibles : {vol['places_disponibles']}")
        vol_choice = int(input("Entrez le numéro du vol : ")) - 1
        
        if vol_choice < 0 or vol_choice >= len(compagnie["vols"]):
            print("Numéro de vol incorrect. Voulez-vous réessayer ? (oui/non)")
            if input().lower() != "oui":
                print("Réservation annulée.")
                return
            continue
        
        vol = compagnie["vols"][vol_choice]

        # Vérification des places disponibles
        nombre_places = int(input("\nCombien de places voulez-vous réserver ? "))
        if nombre_places > vol["places_disponibles"]:
            print("Désolé, il n'y a pas assez de places disponibles. Voulez-vous choisir un autre nombre ? (oui/non)")
            if input().lower() != "oui":
                print("Réservation annulée.")
                return
            continue

        # Sélection de la classe
        classes = ["Economy", "Confort", "Business"]
        print("\nSélectionnez la classe :")
        for i, cls in enumerate(classes, 1):
            print(f"{i}. {cls}")
        class_choice = int(input("Entrez le numéro de la classe : ")) - 1
        
        if class_choice < 0 or class_choice >= len(classes):
            print("Classe incorrect. Voulez-vous choisir une autre classe ? (oui/non)")
            if input().lower() != "oui":
                print("Réservation annulée.")
                return
            continue
        
        classe = classes[class_choice]
        
        # Autres informations
        distance = int(input("\nEntrez la distance du vol (en km) : "))
        duration = int(input("Entrez la durée du vol (en heures) : "))
        seat_selection = input("Voulez-vous sélectionner votre siège ? (oui/non) : ").strip().lower() == "oui"
        
        # Calcul et confirmation du prix
        prix_total = calculate_flight_price(data, compagnie["name"], vol["numero_vol"], distance, duration, classe, seat_selection)
        confirmation = input(f"\nLe prix total est de {prix_total:.2f} €. Confirmez-vous la réservation ? (oui/non) : ")
        
        if confirmation.lower() == "oui":
            vol["places_disponibles"] -= nombre_places
            enregistrer(data)
            print(f"\nRéservation confirmée pour {nombre_places} places sur le vol {vol['numero_vol']} avec {compagnie['name']}.")
            print(f"Prix total : {prix_total:.2f} €.")
        else:
            print("Réservation annulée.")



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
