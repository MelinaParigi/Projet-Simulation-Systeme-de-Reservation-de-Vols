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

## Installation
### Prérequis
- Python 3.x
- Bibliothèques nécessaires : voir `requirements.txt`

### Installation

Clonez ce projet et installez les dépendances avec les commandes suivantes :

```
git clone <url-du-repo>
cd <nom-du-repo>
pip install -r requirements.txt
```

## Utilisation

Lancez l’application avec la commande suivante :

```
python vol.py
```

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

**Prix Final** = (Tarif de Base Compagnie + (Distance × Facteur Distance) + (Durée × Facteur Temps)) × Facteur Classe + Supplément Siège

#### Détails de la Formule

- **Tarif de Base Compagnie** : Dépend de la compagnie choisie (par exemple, 150 € pour une compagnie standard).
- **Distance** : Distance entre l’aéroport de départ et l’aéroport de destination en kilomètres.
- **Facteur Distance** : Multiplicateur par kilomètre (par exemple, 0.1 €/km).
- **Durée** : Durée du trajet en heures.
- **Facteur Temps** : Multiplicateur par heure de vol (par exemple, 5 €/heure).
- **Facteur Classe** :
  - Economy : 1.0
  - Confort : 1.2
  - Business : 1.5
- **Supplément Siège** : Frais supplémentaire pour un siège spécifique (par exemple, 20 €).

### Exemple de Calcul

**Exemple de Calcul du Prix du Billet :**

Pour un vol de **3000 km**, d'une durée de **6 heures**, avec la compagnie **Air Voyage** ayant un tarif de base de **150 €**, en classe **Confort**, et avec un siège spécifique, le calcul serait :

1. **Tarif de Base Compagnie** : 150 €
2. **Distance** : 3000 km, avec un facteur de 0.1 €/km, soit :
   - 3000 km × 0.1 €/km = 300 €
3. **Durée** : 6 heures, avec un facteur de 5 €/heure, soit :
   - 6 heures × 5 €/heure = 30 €
4. **Facteur Classe** pour la classe **Confort** : 1.2
5. **Supplément Siège** : 20 €

En appliquant la formule complète :

**Prix Final** = (Tarif de Base Compagnie + (Distance × Facteur Distance) + (Durée × Facteur Temps)) × Facteur Classe + Supplément Siège

Ce qui donne :

**Prix Final** = (150 + 300 + 30) × 1.2 + 20

**Prix Final** = 480 × 1.2 + 20

**Prix Final** = 576 €

---

Ainsi, le prix total pour ce vol serait **576 €**.

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

### Instructions Utilisateur

1. **Choisissez votre destination** : Sélectionnez un pays dans la liste des destinations disponibles.
2. **Sélectionnez la compagnie aérienne et le vol** : Choisissez parmi les options de compagnies disponibles pour cette destination.
3. **Choisissez la classe de voyage** : Sélectionnez votre classe (Economy, Confort, Business).
4. **Sélectionnez votre siège** : Option pour choisir un siège spécifique avec des frais supplémentaires.
5. **Confirmez votre réservation** : Génération du billet avec tous les détails et le prix final.

### Exemple de scénario

Pour un vol de **3000 km**, d'une durée de **6 heures**, avec la compagnie **Air Voyage**, en classe **Confort**, et avec un siège spécifique, le calcul serait le suivant :

1. **Tarif de Base Compagnie** : 150 €
2. **Distance** : 3000 km avec un facteur de 0.1 €/km, soit :
   - 3000 km × 0.1 €/km = 300 €
3. **Durée** : 6 heures avec un facteur de 5 €/heure, soit :
   - 6 heures × 5 €/heure = 30 €
4. **Facteur Classe** pour la classe **Confort** : 1.2
5. **Supplément Siège** : 20 €

La formule complète devient :

**Prix Final** = (150 + 300 + 30) × 1.2 + 20

**Prix Final** = 576 €

Ainsi, le prix total pour ce vol serait de **576 €**.

## Contributions

Les contributions sont les bienvenues ! Veuillez suivre ces étapes pour contribuer :

1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`).
3. Commitez vos changements (`git commit -m 'Add some AmazingFeature'`).
4. Pushez vers la branche (`git push origin feature/AmazingFeature`).
5. Ouvrez une Pull Request.

## Auteurs et Crédits

- **Auteur** : Amine CHABANE, Mélina
- **Remerciements** : La prof, w3school, youtube.

---
