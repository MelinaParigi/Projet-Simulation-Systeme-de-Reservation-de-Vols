import json
import random

def init_users():
    try:
        with open("users.json", "r") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return {"users": []}

def enregistrer_users(data):
    with open("users.json", "w") as fichier:
        json.dump(data, fichier, indent=4)

def ajouter_utilisateur(data, first_name, last_name, email, phone_number, reservation_id):
    # Vérifiez si l'utilisateur existe déjà
    for user in data["users"]:
        if user["email"] == email or user["phone_number"] == phone_number:
            # L'utilisateur existe déjà, ajoutons l'ID de réservation à son tableau
            if reservation_id not in user["reservation_id"]:  # Évite les doublons
                user["reservation_id"].append(reservation_id)
                print(f"L'utilisateur {first_name} {last_name} existe déjà. ID de réservation ajouté.")
            else:
                print(f"L'ID de réservation {reservation_id} existe déjà pour cet utilisateur.")
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
        "reservation_id": [reservation_id]  # Créer un tableau pour les IDs de réservation
    }
    data["users"].append(new_user)
    enregistrer_users(data)
    print(f"Nouvel utilisateur ajouté : {first_name} {last_name}.")

