import sys
import os
import pytest
from unittest.mock import patch

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from vol import cancel_reservation

def test_cancel_reservation():
    data = {
        "reservation": [
            {
                "id_reservation": "AT123-1",
                "nombre_personne": 2,
            }
        ],
        "Company": {
            "Europe": [
                {
                    "name": "Air Test",
                    "vols": [
                        {
                            "numero_vol": "AT123",
                            "places_disponibles": 100,
                            "nombre_reservations": 1,
                        }
                    ],
                }
            ]
        }
    }

    user_inputs = [
        "AT123-1",
        "oui"      # Confirmation d'annulation
    ]

    # Patch de 'input' et 'print'
    with patch('builtins.input', side_effect=user_inputs):  #Pour simuler ce que les utilisateurs auraient mis dans les inputs
        cancel_reservation(data)

        
        assert len(data["reservation"]) == 0  # La réservation a été supprimée
        assert data["Company"]["Europe"][0]["vols"][0]["places_disponibles"] == 102  # Places libérées

# Pour simuler les appels de la fonction input et les remplacer par d'autres : 

@pytest.mark.parametrize("user_inputs, expected_message", [ 
    (["AT123-1", "non"], "Annulation de réservation annulée."),  # Cas où l'utilisateur refuse l'annulation
    (["AT124-1", "oui"], "Numéro de vol introuvable."),  # Cas où le numéro de vol est incorrect
    (["AT123-2", "oui"], "Aucune réservation trouvée avec ce numéro de réservation.")  # Cas où l'ID réservation est incorrect
])
def test_cancel_reservation_edge_cases(user_inputs, expected_message):
    data = {
        "reservation": [
            {
                "id_reservation": "AT123-1",
                "nombre_personne": 2,
            }
        ],
        "Company": {
            "Europe": [
                {
                    "name": "Air Test",
                    "vols": [
                        {
                            "numero_vol": "AT123",
                            "places_disponibles": 100,
                            "nombre_reservations": 1,
                        }
                    ],
                }
            ]
        }
    }

    # Patch de 'input' et 'print'
    with patch('builtins.input', side_effect=user_inputs):
        cancel_reservation(data)

        assert len(data["reservation"]) == 1  # La réservation n'a pas été supprimée
        assert data["Company"]["Europe"][0]["vols"][0]["places_disponibles"] == 100


if __name__ == '__main__':
    pytest.main()