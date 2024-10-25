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


def enregistrer(data):
    with open("data.json", "w") as fichier:
        json.dump(data, fichier, indent=4)


if __name__ == "__main__":
    print()
    data = init()
    enregistrer(data)
