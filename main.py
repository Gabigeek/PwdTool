from password import *
import argparse
import sys

def get_args():
    parser = argparse.ArgumentParser(
        prog='ProgramName',
        description='Outil de gestion de mot de passe / passphrase',
        add_help=True)
    
    parser.add_argument('tool', type=str, help='Précisez l\'outil souhaité : PasswordTest, PasswordGen or PassphraseTest')
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args()
    return args


args = get_args()
#debug
#args.tool = 'passwordTest'

match args.tool:
    case 'PasswordTest':
        pwd = Password(input("saisissez un mot de passe à tester : "))
        pwd.get_entropy()
        pwd.get_password_strength()

    case 'PasswordGen':
        length = int(input("Longueur du mot de passe : "))
        min_lowercase = int(input("Nombre de minuscules minimum : "))
        min_uppercase = int(input("Nombre de majuscules minimum : "))
        min_digits = int(input("Nombre de chiffres minimum : "))
        min_special = int(input("Nombre de caractères spéciaux minimum : "))
        gen_pwd = Password(Password.generate_password(length, min_lowercase, min_uppercase, min_digits, min_special))
        gen_pwd.get_password()
        gen_pwd.get_entropy()
        gen_pwd.get_password_strength()
        
    case 'PassphraseTest':
        print('passphraseTest demandé')
    case _:
        print('Commande inconnue, merci de préciser l\'outil souhaité : PasswordTest, PasswordGen or PassphraseTest')