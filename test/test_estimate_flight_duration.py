import sys
import os
import pytest
from unittest.mock import patch

"""
Tests pour la fonction estimate_flight_duration de vol.py.

Ces tests vérifient le bon fonctionnement de la fonction estimate_flight_duration,
qui estime la durée d'un vol en fonction de la distance entre deux pays et d'une 
vitesse moyenne. Les tests utilisent un patch pour simuler la distance entre les 
pays, permettant de contrôler les valeurs de retour de manière prédictive.
"""
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)
from vol import estimate_flight_duration


def test_estimate_flight_duration():
    """
    Teste estimate_flight_duration pour un cas standard avec une distance connue.

    - Simule une distance de 1000 km entre France et Espagne en utilisant un patch.
    - Vitesse moyenne : 900 km/h.
    - Durée attendue = distance / vitesse moyenne.

    Vérifie que la fonction retourne la durée correcte en heures pour un vol entre
    deux pays avec une distance simulée.
    """
    pays_depart = "France"
    pays_arriver = "Espagne"

    distance = 1000
    vitesse_moyenne = 900
    expected_duration = distance / vitesse_moyenne

    # Patch : remplace temporarement distance_entre_pays
    with patch("vol.distance_entre_pays", return_value=distance):
        result = estimate_flight_duration(pays_depart, pays_arriver)
        assert result == expected_duration


def test_estimate_flight_duration_none():
    """
    Teste estimate_flight_duration pour un cas où la distance est inconnue.

    - Simule une situation où distance_entre_pays retourne None (par exemple,
      si le pays de destination est incorrect ou non reconnu).
    - Vérifie que estimate_flight_duration retourne également None dans ce cas.

    Ce test garantit que la fonction gère correctement les situations où la distance
    ne peut pas être calculée.
    """
    pays_depart = "France"
    pays_arriver = "Nulle Part"

    with patch("vol.distance_entre_pays", return_value=None):
        result = estimate_flight_duration(pays_depart, pays_arriver)
        assert result is None


if __name__ == "__main__":
    pytest.main()
