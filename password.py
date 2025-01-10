import math


class Password:
    def __init__(self, input_password):
        self.password = input_password
        entropy = Password.check_entropy(self.password)
        length = len(self.password)

    def check_entropy(password):
        char_set = set(password)
        char_set_size = len(char_set)
        password_size = len(password)
        entropy = math.log2(char_set_size ** password_size)
        return entropy