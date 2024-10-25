from opencage.geocoder import OpenCageGeocode
from math import radians, sin, cos, sqrt, atan2


def distance_entre_pays(pays1, pays2, api_key):
    geocoder = OpenCageGeocode(api_key)

    # Obtenir les coordonnées des deux pays
    result1 = geocoder.geocode(pays1)
    result2 = geocoder.geocode(pays2)

    if result1 and result2:
        lat1, lon1 = result1[0]["geometry"]["lat"], result1[0]["geometry"]["lng"]
        lat2, lon2 = result2[0]["geometry"]["lat"], result2[0]["geometry"]["lng"]

        # Calcul de la distance
        R = 6371  # Rayon de la Terre en km
        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)
        a = (
            sin(dlat / 2) ** 2
            + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
        )
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c

        return distance
    else:
        print("Coordonnées non trouvées pour un ou les deux pays.")
        return None


# Utilisation de la fonction avec votre clé API
api_key = "b5072a154cba4479ba056f5b47d5bd7a"
pays1 = "Canada"
pays2 = "Japon"
distance = distance_entre_pays(pays1, pays2, api_key)
if distance:
    print(f"La distance entre {pays1} et {pays2} est d'environ {distance:.2f} km.")
