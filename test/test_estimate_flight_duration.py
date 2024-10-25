import sys
import os
import pytest
from unittest.mock import patch

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)
from vol import estimate_flight_duration

def test_estimate_flight_duration():
    pays_depart = "France"
    pays_arriver = "Espagne"

    distance = 1000
    vitesse_moyenne = 900
    expected_duration = distance / vitesse_moyenne

    # Patch : remplace temporarement distance_entre_pays
    with patch('vol.distance_entre_pays', return_value=distance):
        result = estimate_flight_duration(pays_depart, pays_arriver)
        assert result == expected_duration

def test_estimate_flight_duration_none():
    pays_depart = "France"
    pays_arriver = "Nulle Part"

    with patch('vol.distance_entre_pays', return_value=None):
        result = estimate_flight_duration(pays_depart, pays_arriver)
        assert result is None

if __name__ == '__main__':
    pytest.main()