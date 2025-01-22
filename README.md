# Gestionnaire de Mots de Passe et Passphrases

Un outil Python pour générer et évaluer des identifiants sécurisés.

----------------------------------------

## FONCTIONNALITÉS

- Évaluation de mot de passe : 
  * Calcule l'entropie
  * Détermine la force (Very_weak à Very_strong)

- Génération de mot de passe :
  * Personnalisation des critères :
    - Longueur totale
    - Nombre de minuscules/majuscules
    - Nombre de chiffres/caractères spéciaux

- Génération de passphrase :
  * 6 mots aléatoires
  * Basé sur la liste EFF (https://www.eff.org/dice)

----------------------------------------

## INSTALLATION

Prérequis :
- Python 3.x
- Modules nécessaires : requests

Commande d'installation :
pip install requests

----------------------------------------

## UTILISATION

### 1. Tester un mot de passe existant
Commande :
python main.py PasswordTest

Exemple :
> saisissez un mot de passe à tester : abc123
Le mot de passe est : abc123
Entropie : 15.51 | Force : Very_weak

### 2. Générer un mot de passe
Commande :
python main.py PasswordGen

Configuration type :
Longueur : 12
Minuscules : 4
Majuscules : 2
Chiffres : 2
Spéciaux : 1

Résultat exemple :
Mot de passe : JZ!5d"hxvw9%
Entropie : 43.02 | Force : Ok

### 3. Générer une passphrase
Commande :
python main.py PassphraseGen

Exemple de sortie :
slurp petal museum dislike provided bloated

----------------------------------------

## TESTS UNITAIRES

Lancer les tests :
python tests.py

Sortie attendue :
..
OK (2 tests passés)

Tests inclus :
- Vérification Very_weak (mot de passe "1234")
- Vérification Strong (mot de passe complexe)

----------------------------------------

## NOTES

- Les guillemets (") dans les mots de passe sont gérés automatiquement
- Les passphrases nécessitent une connexion Internet