

---

# Simulateur de Réservation de Vols ✈️

Ce projet est un simulateur de réservation de vols permettant de choisir une destination, sélectionner une compagnie aérienne, déterminer une classe de voyage, choisir des sièges, et générer un billet avec tous les détails de vol et le calcul de prix.

## Fonctionnalités

- **Liste des Pays** : Sélection de la destination à partir d'une liste complète des pays du monde.
- **Liste des Vols et Compagnies** : Options de vols disponibles avec des compagnies aériennes variées.
- **Générateur de Prix** : Calcul automatique du prix en fonction de plusieurs critères :
  - Destination
  - Compagnie aérienne
  - Distance et durée du trajet
  - Classe de voyage (Business, Economy, Confort, etc.)
  - Sélection de siège spécifique
- **Billet d'Avion** : Impression d'un billet détaillé contenant toutes les informations essentielles de la réservation.

## Calcul du Prix du Billet 🎫

La formule pour calculer le prix du billet prend en compte plusieurs éléments clés :

1. **Base de Prix de la Compagnie** : Chaque compagnie a un tarif de base défini pour ses services. Par exemple, une compagnie haut de gamme peut avoir un tarif de base plus élevé.
2. **Distance entre Pays de Départ et d'Arrivée** : La distance entre l’aéroport de départ et l’aéroport de destination, en kilomètres.
3. **Durée du Trajet** : L'heure estimée du trajet peut influencer le prix (par exemple, un vol de nuit peut être plus coûteux).
4. **Classe de Voyage** : 
   - `Economy` : Prix standard.
   - `Confort` : Supplément de 20% sur le prix standard.
   - `Business` : Supplément de 50% sur le prix standard.
5. **Sélection de Siège** : La sélection d’un siège spécifique ajoute des frais supplémentaires (par exemple, un siège près de la fenêtre ou avec espace pour les jambes).

### Formule de Calcul du Prix

Voici la formule pour calculer le prix final :

\[
\text{Prix Final} = \left( \text{Tarif de Base Compagnie} + (\text{Distance} \times \text{Facteur Distance}) + (\text{Durée} \times \text{Facteur Temps}) \right) \times \text{Facteur Classe} + \text{Supplément Siège}
\]

#### Détails de la Formule

- **Tarif de Base Compagnie** : Prix de départ en fonction de la compagnie (par exemple, `150 €` pour une compagnie régulière).
- **Distance** : Distance entre les deux pays en kilomètres (par exemple, `3000 km`).
- **Facteur Distance** : Multiplicateur par kilomètre (par exemple, `0.1 €/km`).
- **Durée** : Heure du trajet en heures (par exemple, `6 heures`).
- **Facteur Temps** : Multiplicateur par heure de vol (par exemple, `5 €/heure`).
- **Facteur Classe** :
  - `Economy` : `1.0`
  - `Confort` : `1.2`
  - `Business` : `1.5`
- **Supplément Siège** : Frais supplémentaire si un siège spécifique est choisi (par exemple, `20 €` pour un siège avec espace supplémentaire).

### Exemple de Calcul

Pour un vol de `3000 km`, d'une durée de `6 heures`, avec la compagnie `Air Voyage` ayant un tarif de base de `150 €`, en classe `Confort`, et avec un siège spécifique :

\[
\text{Prix Final} = \left(150 + (3000 \times 0.1) + (6 \times 5)\right) \times 1.2 + 20
\]
\[
\text{Prix Final} = (150 + 300 + 30) \times 1.2 + 20 = 576 €
\]

## Format du Billet 🎟️

Le billet généré inclura les informations suivantes :

- **Pays de Départ** : (ex. France)
- **Pays d'Arrivée** : (ex. Japon)
- **Heure du Trajet** : (ex. 6 heures)
- **Classe de Voyage** : (Economy, Confort, Business)
- **Prix Total** : (calculé avec la formule ci-dessus)

### Exemple de Billet

```
===============================
          Billet de Vol         
===============================

Départ       : France
Destination  : Japon
Durée        : 6 heures
Classe       : Confort
Prix Total   : 576 €

===============================
Merci d'avoir choisi notre service !
===============================
```

---

