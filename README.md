# Gestionnaire de Mots de Passe et Passphrases

Un outil Python pour générer et évaluer la sécurité des mots de passe et passphrases.

## Fonctionnalités

- **Évaluation de mot de passe** : Calcule l'entropie et la force d'un mot de passe existant.
- **Génération de mot de passe** : Crée un mot de passe sécurisé selon des critères personnalisables.
- **Génération de passphrase** : Génère une passphrase aléatoire à partir d'une liste de mots de l'EFF.

## Prérequis

- Python 3.x
- Modules Python : `requests`, `argparse`, `math`, `random`, `string`, `unittest`

Installez les dépendances avec :
```bash
pip install requests
```
## Exemples d'utilisation détaillés

### 1. Tester un mot de passe existant (`PasswordTest`)

**Exemple 1** - Mot de passe faible :  
```bash
$ python main.py PasswordTest
saisissez un mot de passe à tester : abc123

# Sortie :
Le mot de passe est : abc123
L'entropie du mot de passe est : 25.0
La force du mot de passe est : Weak