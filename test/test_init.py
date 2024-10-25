import sys
import os
import pycountry

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)
from vol import init

"""
Tests pour vérifier la structure de données générée par la fonction init.

Ces tests valident que la fonction init retourne une structure de données correcte,
comprenant les informations principales sur les pays, les réservations, et les compagnies 
aériennes par région. Le test vérifie la présence des clés et des types de données attendus 
ainsi que certaines contraintes sur les valeurs.
"""

# Remplacez 'your_module' par le nom du fichier contenant la fonction


def test_init_structure():
    """
    Teste la structure et la cohérence des données retournées par la fonction init.

    La fonction init est supposée retourner un dictionnaire contenant trois clés principales :
    - 'Pays' : une liste de noms de pays.
    - 'reservation' : une liste de structures de réservation avec des champs spécifiques.
    - 'Company' : un dictionnaire de compagnies aériennes, classées par région.

    Les vérifications incluent :
    1. Présence des clés principales ('Pays', 'reservation', 'Company').
    2. Type et contenu de 'Pays' (doit être une liste non vide).
    3. Structure de 'reservation' : doit être une liste contenant des dictionnaires avec les clés
       'id_reservation' et 'nombre_personne'.
    4. Structure de 'Company' : doit être un dictionnaire avec des clés de région (comme 'Europe',
       'Amérique Latine'), chacune associée à une liste de compagnies aériennes.
    5. Chaque compagnie doit contenir une clé 'name' et une liste 'vols', où chaque vol doit avoir
       les clés 'numero_vol', 'places_disponibles', et 'nombre_reservations'.
    6. Contraintes de valeurs :
       - 'places_disponibles' doit être un entier entre 50 et 200.
       - 'nombre_reservations' doit être initialisé à 0.

    Le test échoue si l'une des conditions ci-dessus n'est pas respectée.
    """
    # Appel de la fonction pour obtenir les données
    data = init()

    # Vérifie si les clés principales sont présentes
    assert "Pays" in data, "La clé 'Pays' doit être présente dans les données"
    assert (
        "reservation" in data
    ), "La clé 'reservation' doit être présente dans les données"
    assert "Company" in data, "La clé 'Company' doit être présente dans les données"

    # Vérifie que 'Pays' est une liste non vide
    assert isinstance(data["Pays"], list), "'Pays' doit être une liste"
    assert len(data["Pays"]) > 0, "'Pays' doit contenir des noms de pays"

    # Vérifie que 'reservation' est une liste et qu'elle contient la structure correcte
    assert isinstance(data["reservation"], list), "'reservation' doit être une liste"
    assert (
        len(data["reservation"]) > 0
    ), "'reservation' doit contenir au moins une structure"
    for reservation in data["reservation"]:
        assert (
            "id_reservation" in reservation
        ), "Chaque réservation doit avoir un 'id_reservation'"
        assert (
            "nombre_personne" in reservation
        ), "Chaque réservation doit avoir un 'nombre_personne'"

    # Vérifie la structure de 'Company'
    assert isinstance(data["Company"], dict), "'Company' doit être un dictionnaire"
    assert "Europe" in data["Company"], "'Europe' doit être une clé dans 'Company'"
    assert (
        "Amérique Latine" in data["Company"]
    ), "'Amérique Latine' doit être une clé dans 'Company'"

    # Vérifie la structure des compagnies dans 'Company'
    for region, companies in data["Company"].items():
        for company in companies:
            assert "name" in company, "Chaque compagnie doit avoir une clé 'name'"
            assert "vols" in company, "Chaque compagnie doit avoir une liste 'vols'"
            assert isinstance(company["vols"], list), "'vols' doit être une liste"

            # Vérifie chaque vol dans la liste des vols de la compagnie
            for vol in company["vols"]:
                assert "numero_vol" in vol, "Chaque vol doit avoir une clé 'numero_vol'"
                assert (
                    "places_disponibles" in vol
                ), "Chaque vol doit avoir une clé 'places_disponibles'"
                assert (
                    "nombre_reservations" in vol
                ), "Chaque vol doit avoir une clé 'nombre_reservations'"

                # Vérifie les valeurs de nombre de places et de réservations
                assert (
                    50 <= vol["places_disponibles"] <= 200
                ), "'places_disponibles' doit être entre 50 et 200"
                assert (
                    vol["nombre_reservations"] == 0
                ), "'nombre_reservations' doit être initialisé à 0"
