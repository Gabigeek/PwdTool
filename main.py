from password import *
import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='Outil de gestion de mot de passe / passphrase',
        add_help=True)
    
    parser.add_argument('tool', type=str, help='Précisez l\'outil souhaité : passwordTest, passwordGen or passphraseTest')
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args()
    return args


args = get_args()
match args.tool:
    case 'passwordTest':
        pwd = input("saisissez un mot de passe à tester :")
        print("L'entropie du mot de passe est : ", Password.check_entropy(pwd))

    case 'passwordGen':
        print('passwordGen demandé')
    case 'passphraseTest':
        print('passphraseTest demandé')
    case _:
        print('Commande inconnue, merci de préciser l\'outil souhaité : passwordTest, passwordGen or passphraseTest')