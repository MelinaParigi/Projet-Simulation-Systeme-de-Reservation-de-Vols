import sys
import os
import pycountry
import pytest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)
from vol import calculate_flight_price, estimate_flight_duration, distance_entre_pays


def test_calculate_flight_price_economy_no_seat_select():
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
