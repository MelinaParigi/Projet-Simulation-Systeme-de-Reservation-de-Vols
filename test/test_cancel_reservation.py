import sys
import os
import pytest
from unittest.mock import patch

"""
Tests pour la fonction cancel_reservation de vol.py.

Ces tests vérifient le bon fonctionnement de la fonction cancel_reservation,
qui permet d'annuler une réservation de vol et de mettre à jour les données 
de disponibilité des places. Les tests utilisent un patch pour simuler les 
entrées utilisateur, permettant de contrôler le comportement de la fonction 
et d'évaluer si les mises à jour des réservations et des places disponibles 
sont correctes.
"""
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)
from vol import cancel_reservation


def test_cancel_reservation():
    """
    Teste cancel_reservation pour un cas standard d'annulation.

    - Prépare un jeu de données avec une réservation existante.
    - Simule une entrée utilisateur confirmant l'annulation de la réservation.
    - Vérifie que la réservation a été supprimée de la liste des réservations 
      et que le nombre de places disponibles a été mis à jour.

    Ce test garantit que la fonction annule correctement une réservation.
    """
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

    # Patch de 'input' pour simuler les entrées utilisateur
    with patch('builtins.input', side_effect=user_inputs):  
        cancel_reservation(data)

        # Vérifie que la réservation a été supprimée
        assert len(data["reservation"]) == 0  
        # Vérifie que le nombre de places disponibles a été mis à jour
        assert data["Company"]["Europe"][0]["vols"][0]["places_disponibles"] == 102  


@pytest.mark.parametrize("user_inputs, expected_message", [ 
    (["AT123-1", "non"], "Annulation de réservation annulée."),  # Cas où l'utilisateur refuse l'annulation
    (["AT124-1", "oui"], "Numéro de vol introuvable."),  # Cas où le numéro de vol est incorrect
    (["AT123-2", "oui"], "Aucune réservation trouvée avec ce numéro de réservation.")  # Cas où l'ID réservation est incorrect
])
def test_cancel_reservation_edge_cases(user_inputs, expected_message):
    """
    Teste cancel_reservation pour des cas limites d'annulation.

    - Prépare un jeu de données avec une réservation existante.
    - Simule différents scénarios d'entrées utilisateur, y compris :
      - Annulation de l'annulation de la réservation.
      - Numéro de vol incorrect.
      - ID de réservation inexistant.
    - Vérifie que la réservation n'a pas été supprimée et que le nombre de 
      places disponibles reste inchangé dans chaque cas.

    """
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

    # Patch de 'input' pour simuler les entrées utilisateur
    with patch('builtins.input', side_effect=user_inputs):
        cancel_reservation(data)

        # Vérifie que la réservation n'a pas été supprimée
        assert len(data["reservation"]) == 1  
        # Vérifie que le nombre de places disponibles reste inchangé
        assert data["Company"]["Europe"][0]["vols"][0]["places_disponibles"] == 100


if __name__ == '__main__':
    pytest.main()
