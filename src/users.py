import json
import random


def init_users():
    """
    Initialise et charge les données des utilisateurs depuis le fichier 'users.json'.

    Si le fichier 'users.json' existe, la fonction lit et renvoie son contenu sous
    forme de dictionnaire. Si le fichier est introuvable, elle retourne un dictionnaire
    vide avec une clé 'users' contenant une liste vide.

    Retourne:
        dict: Dictionnaire des utilisateurs, initialisé avec une liste vide sous la clé 'users'
              si le fichier n'est pas trouvé.
    """
    try:
        with open("users.json", "r") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return {"users": []}


def enregistrer_users(data):
    """
    Enregistre les données des utilisateurs dans le fichier 'users.json'.

    Prend un dictionnaire contenant les informations des utilisateurs, puis le
    sauvegarde en format JSON dans 'users.json' avec une indentation de 4 espaces
    pour la lisibilité.

    Paramètres:
        data (dict): Dictionnaire contenant les informations des utilisateurs à enregistrer.
    """
    with open("users.json", "w") as fichier:
        json.dump(data, fichier, indent=4)


def ajouter_utilisateur(
    data, first_name, last_name, email, phone_number, reservation_id
):
    """
    Ajoute un utilisateur ou met à jour ses réservations dans le dictionnaire des utilisateurs.

    - Si un utilisateur avec le même email ou numéro de téléphone existe déjà, l'ID de réservation
      fourni est ajouté à son tableau de réservations, sauf s'il est déjà présent.
    - Si l'utilisateur n'existe pas, un nouvel utilisateur est créé avec un ID utilisateur unique,
      et ses informations sont ajoutées au dictionnaire.

    Paramètres:
        data (dict): Dictionnaire des utilisateurs existants.
        first_name (str): Prénom de l'utilisateur.
        last_name (str): Nom de l'utilisateur.
        email (str): Adresse email de l'utilisateur.
        phone_number (str): Numéro de téléphone de l'utilisateur.
        reservation_id (str): ID de réservation à associer à l'utilisateur.

    Effets:
        Met à jour 'data' avec un nouvel utilisateur ou ajoute une réservation
        à un utilisateur existant, puis enregistre les modifications dans 'users.json'.
    """
    # Vérifiez si l'utilisateur existe déjà
    for user in data["users"]:
        if user["email"] == email or user["phone_number"] == phone_number:
            # L'utilisateur existe déjà, ajoutons l'ID de réservation à son tableau
            if reservation_id not in user["reservation_id"]:  # Évite les doublons
                user["reservation_id"].append(reservation_id)
                print(
                    f"L'utilisateur {first_name} {last_name} existe déjà. ID de réservation ajouté."
                )
            else:
                print(
                    f"L'ID de réservation {reservation_id} existe déjà pour cet utilisateur."
                )
            enregistrer_users(data)
            return

    # Si l'utilisateur n'existe pas, créons un nouvel utilisateur
    user_id = f"{first_name.lower()}{last_name.lower()}{random.randint(1000, 9999)}"  # Un ID utilisateur unique
    new_user = {
        "id_user": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": phone_number,
        "reservation_id": [
            reservation_id
        ],  # Créer un tableau pour les IDs de réservation
    }
    data["users"].append(new_user)
    enregistrer_users(data)
    print(f"Nouvel utilisateur ajouté : {first_name} {last_name}.")
