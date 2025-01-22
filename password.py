import math
import random
import string


class Password:
    def __init__(self, input_password):
        self.password = input_password
        self.entropy = Password.check_entropy(self)
        self.power = Password.check_password_strength(self)

    def get_password(self):
        print("Le mot de passe est : ", self.password)

    def check_entropy(self):
        char_set = set(self.password)
        char_set_size = len(char_set)
        password_size = len(self.password)
        entropy = math.log2(char_set_size ** password_size)
        return entropy
    
    def get_entropy(self):
        print("L'entropie du mot de passe est : ", self.entropy)

    
    def check_password_strength(self):
        if self.entropy < 28:
           return "Very_weak"
        elif 28 <= self.entropy < 36:
            return "Weak"
        elif 36 <= self.entropy < 60:
            return "Ok"
        elif 60 <= self.entropy < 128:
            return "Strong"
        elif self.entropy >= 128:
            return "Very_strong"
        else:
            raise ValueError("Mauvaise entropie")
        
    def get_password_strength(self):
        print("La force du mot de passe est : ", self.power)
        
    def generate_password(length, min_lowercase, min_uppercase, min_digits, min_special):
        # Liste contenant tous les caractères possibles
        all_characters = string.ascii_letters + string.digits + string.punctuation
        password_list = []
    
        # Ajout des caractères obligatoires
        password_list.extend(random.choices(string.ascii_lowercase, k=min_lowercase))
        password_list.extend(random.choices(string.ascii_uppercase, k=min_uppercase))
        password_list.extend(random.choices(string.digits, k=min_digits))
        password_list.extend(random.choices(string.punctuation, k=min_special))
    
        if len(password_list) > length:
            raise ValueError("La somme des caractères minimums dépasse la longueur totale")
    
        # Complétion avec des caractères aléatoires
        remaining_length = length - len(password_list)
        password_list.extend(random.choices(all_characters, k=remaining_length))
        random.shuffle(password_list)
        return "".join(password_list)