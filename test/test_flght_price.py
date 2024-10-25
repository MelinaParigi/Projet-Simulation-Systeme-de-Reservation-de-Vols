import sys
import os
import pycountry
import pytest

"""
Tests de la fonction calculate_flight_price dans divers scénarios de classes de voyage et de sélection de siège.

Ces tests vérifient la précision de calculate_flight_price en fonction des différents paramètres :
- Classe de voyage : Economy, Confort, Business.
- Sélection de siège : Avec ou sans sélection de siège.
- Durée du vol et distance entre les pays sont fixées pour assurer des comparaisons cohérentes.

Chaque test utilise pytest.approx pour autoriser une légère tolérance dans les valeurs calculées,
en raison de la nature des opérations en virgule flottante.
"""

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)
from vol import calculate_flight_price, estimate_flight_duration, distance_entre_pays


def test_calculate_flight_price_economy_no_seat_select():
    """
    Teste le calcul du prix pour un vol en classe Economy sans sélection de siège.

    - Compagnie: Air France
    - Classe: Economy
    - Sélection de siège: Non
    - Durée: 1 heure
    - Distance: 909.78 km (valeur fixe pour cohérence)

    Vérifie que le prix correspond au calcul attendu sans frais de sélection de siège.
    """
    company_name = "Air France"
    flight_number = "AF123"
    pays_depart = "France"
    pays_arriver = "Allemagne"
    duration = 1  # en heures
    travel_class = "Economy"
    seat_selection = False
    distance = 909.78

    prix = calculate_flight_price(
        company_name,
        flight_number,
        pays_depart,
        pays_arriver,
        duration,
        travel_class,
        seat_selection,
    )
    calcule_prix = (150 + (distance * 0.1) + (duration * 5)) * 1.0
    assert prix == pytest.approx(
        calcule_prix, rel=0.1
    ), f"Le prix calculé ({prix}) est incorrect pour un vol Economy sans sélection de siège"


def test_calculate_flight_price_economy_seat_select():
    """
    Teste le calcul du prix pour un vol en classe Economy avec sélection de siège.

    - Compagnie: Air France
    - Classe: Economy
    - Sélection de siège: Oui (ajout de 20€)
    - Durée: 1 heure
    - Distance: 909.78 km

    Vérifie que le prix correspond au calcul attendu avec frais de sélection de siège.
    """
    company_name = "Air France"
    flight_number = "AF123"
    pays_depart = "France"
    pays_arriver = "Allemagne"
    duration = 1  # en heures
    travel_class = "Economy"
    seat_selection = True
    distance = 909.78

    calcule_prix = (150 + (distance * 0.1) + (duration * 5)) * 1.0 + 20
    prix = calculate_flight_price(
        company_name,
        flight_number,
        pays_depart,
        pays_arriver,
        duration,
        travel_class,
        seat_selection,
    )
    assert prix == pytest.approx(
        calcule_prix, rel=0.1
    ), f"Le prix calculé ({prix}) est incorrect pour un vol Economy avec sélection de siège"


def test_calculate_flight_price_business_seat_select():
    """
    Teste le calcul du prix pour un vol en classe Business avec sélection de siège.

    - Compagnie: Air France
    - Classe: Business (coefficient 1.5)
    - Sélection de siège: Oui (ajout de 20€)
    - Durée: 1 heure
    - Distance: 909.78 km

    Vérifie que le prix correspond au calcul attendu avec frais de sélection de siège et le coefficient de Business.
    """
    company_name = "Air France"
    flight_number = "AF123"
    pays_depart = "France"
    pays_arriver = "Allemagne"
    duration = 1  # en heures
    travel_class = "Business"
    seat_selection = True
    distance = 909.78

    prix = calculate_flight_price(
        company_name,
        flight_number,
        pays_depart,
        pays_arriver,
        duration,
        travel_class,
        seat_selection,
    )
    calcule_prix = (150 + (distance * 0.1) + (duration * 5)) * 1.5 + 20
    assert prix == pytest.approx(
        calcule_prix, rel=0.1
    ), f"Le prix calculé ({prix}) est incorrect pour un vol Business avec sélection de siège"


def test_calculate_flight_price_business_no_seat_select():
    """
    Teste le calcul du prix pour un vol en classe Business sans sélection de siège.

    - Compagnie: Air France
    - Classe: Business (coefficient 1.5)
    - Sélection de siège: Non
    - Durée: 1 heure
    - Distance: 909.78 km

    Vérifie que le prix correspond au calcul attendu avec le coefficient de Business et sans frais de sélection de siège.
    """
    company_name = "Air France"
    flight_number = "AF123"
    pays_depart = "France"
    pays_arriver = "Allemagne"
    duration = 1  # en heures
    travel_class = "Business"
    seat_selection = False
    distance = 909.78

    prix = calculate_flight_price(
        company_name,
        flight_number,
        pays_depart,
        pays_arriver,
        duration,
        travel_class,
        seat_selection,
    )
    calcule_prix = (150 + (distance * 0.1) + (duration * 5)) * 1.5
    assert prix == pytest.approx(
        calcule_prix, rel=0.1
    ), f"Le prix calculé ({prix}) est incorrect pour un vol Business sans sélection de siège"


def test_calculate_flight_price_confort_seat_select():
    """
    Teste le calcul du prix pour un vol en classe Confort avec sélection de siège.

    - Compagnie: Air France
    - Classe: Confort (coefficient 1.2)
    - Sélection de siège: Oui (ajout de 20€)
    - Durée: 1 heure
    - Distance: 909.78 km

    Vérifie que le prix correspond au calcul attendu avec frais de sélection de siège et le coefficient de Confort.
    """
    company_name = "Air France"
    flight_number = "AF123"
    pays_depart = "France"
    pays_arriver = "Allemagne"
    duration = 1  # en heures
    travel_class = "Confort"
    seat_selection = True
    distance = 909.78

    prix = calculate_flight_price(
        company_name,
        flight_number,
        pays_depart,
        pays_arriver,
        duration,
        travel_class,
        seat_selection,
    )
    calcule_prix = (150 + (distance * 0.1) + (duration * 5)) * 1.2 + 20
    assert prix == pytest.approx(
        calcule_prix, rel=0.1
    ), f"Le prix calculé ({prix}) est incorrect pour un vol Confort avec sélection de siège"


def test_calculate_flight_price_confort_no_seat_select():
    """
    Teste le calcul du prix pour un vol en classe Confort sans sélection de siège.

    - Compagnie: Air France
    - Classe: Confort (coefficient 1.2)
    - Sélection de siège: Non
    - Durée: 1 heure
    - Distance: 909.78 km

    Vérifie que le prix correspond au calcul attendu avec le coefficient de Confort sans frais de sélection de siège.
    """
    company_name = "Air France"
    flight_number = "AF123"
    pays_depart = "France"
    pays_arriver = "Allemagne"
    duration = 1  # en heures
    travel_class = "Confort"
    seat_selection = False
    distance = 909.78

    prix = calculate_flight_price(
        company_name,
        flight_number,
        pays_depart,
        pays_arriver,
        duration,
        travel_class,
        seat_selection,
    )
    calcule_prix = (150 + (distance * 0.1) + (duration * 5)) * 1.2
    assert prix == pytest.approx(
        calcule_prix, rel=0.1
    ), f"Le prix calculé ({prix}) est incorrect pour un vol Confort sans sélection de siège"
