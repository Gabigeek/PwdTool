import math


class Password:
    def __init__(self, input_password):
        self.password = input_password
        self.entropy = Password.check_entropy(self)
        self.power = Password.check_password_strength(self)

    def check_entropy(self):
        char_set = set(self.password)
        char_set_size = len(char_set)
        password_size = len(self.password)
        entropy = math.log2(char_set_size ** password_size)
        return entropy
    
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
            return "Entropie invalide"
