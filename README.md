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
```bash
$ python main.py PasswordTest
saisissez un mot de passe à tester : abc123

# Sortie :
L'entropie du mot de passe est :  15.509775004326936
La force du mot de passe est :  Very_weak
```

### 2. Génération de mot de passe (`PasswordGen`)
```bash
$ python main.py PasswordGen
Longueur du mot de passe : 12
Nombre de minuscules minimum : 4
Nombre de majuscules minimum : 2
Nombre de chiffres minimum : 2
Nombre de caractères spéciaux minimum : 1


# Sortie :
Le mot de passe est :  JZ!5d"hxvw9%
L'entropie du mot de passe est :  43.01955000865387
La force du mot de passe est :  Ok
```

### 3. Génération de passphrase (`PassphraseGen`)
```bash
$ python main.py PassphraseGen

# Sortie :
La passphrase est :  slurp petal museum dislike provided bloated
```