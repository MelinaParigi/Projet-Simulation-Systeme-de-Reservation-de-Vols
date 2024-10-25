import sys
import os
import pytest
from unittest.mock import patch

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)
from vol import book_flight

"""
Tests pour la fonction book_flight de vol.py.

Ces tests vérifient le bon fonctionnement de la fonction book_flight,
qui permet à un utilisateur de réserver un vol. Les tests simulent les
entrées de l'utilisateur pour chaque étape du processus de réservation
et vérifient que les données sont mises à jour.
"""


def test_book_flight_success():
    """
    Teste book_flight pour une réservation réussie.

    - Simule les entrées utilisateur pour réserver un vol.
    - Vérifie que la réservation est ajoutée et que le nombre
      de places disponibles est mis à jour.
    """

    data = {
        "reservation": [],
        "Company": {
            "Europe": [
                {
                    "name": "Air Test",
                    "vols": [
                        {
                            "numero_vol": "AT123",
                            "places_disponibles": 100,
                            "nombre_reservations": 0,
                        }
                    ],
                }
            ]
        }
    }

    user_inputs = [
        "France",    # Pays de départ
        "Espagne",   # Pays d'arrivée
        "1",         # Choix du continent (Europe)
        "1",         # Choix de la compagnie (Air Test)
        "1",         # Choix du vol (AT123)
        "1",         # Nombre de places
        "1",         # Choix de la classe (Economy)
        "John",      # Prénom
        "Doe",       # Nom
        "john.doe@example.com",  # Email
        "0123456789",  # Numéro de téléphone
        "oui"        # Confirmation de réservation
    ]

    with patch('builtins.input', side_effect=user_inputs):
        book_flight(data)

        # Vérifications
        assert len(data["reservation"]) == 1  # Une réservation ajoutée
        assert data["reservation"][0]["nombre_personne"] == 1  # Nombre de personnes
        assert data["Company"]["Europe"][0]["vols"][0]["places_disponibles"] == 99  # Places
        assert data["Company"]["Europe"][0]["vols"][0]["nombre_reservations"] == 1  # Réservations

def test_book_flight_cancelled():
    """
    Teste book_flight pour un cas où l'utilisateur annule la réservation à la fin.

    - Simule les entrées utilisateur pour annuler la réservation.
    - Vérifie que la réservation n'est pas ajoutée.
    """
    # Données de test
    data = {
        "reservation": [],
        "Company": {
            "Europe": [
                {
                    "name": "Air Test",
                    "vols": [
                        {
                            "numero_vol": "AT123",
                            "places_disponibles": 100,
                            "nombre_reservations": 0,
                        }
                    ],
                }
            ]
        }
    }

    user_inputs = [
        "France",    # Pays de départ
        "Espagne",   # Pays d'arrivée
        "1",         # Choix du continent (Europe)
        "1",         # Choix de la compagnie (Air Test)
        "1",         # Choix du vol (AT123)
        "1",         # Nombre de places
        "1",         # Choix de la classe (Economy)
        "John",      # Prénom
        "Doe",       # Nom
        "john.doe@example.com",  # Email
        "0123456789",  # Numéro de téléphone
        "non"        # Confirmation de réservation
    ]

    with patch('builtins.input', side_effect=user_inputs):
        book_flight(data)

        # Vérifications
        assert len(data["reservation"]) == 0  # Aucune réservation ajoutée
        assert data["Company"]["Europe"][0]["vols"][0]["places_disponibles"] == 100  # Places
        assert data["Company"]["Europe"][0]["vols"][0]["nombre_reservations"] == 0  # Réservations

if __name__ == '__main__':
    pytest.main()
