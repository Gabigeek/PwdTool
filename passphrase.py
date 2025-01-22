import requests
import random

class Passphrase:
    def __init__(self):

        #Récupération de la liste et parsing
        url = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"
        response = requests.get(url, timeout=2)
        if response.status_code != 200:
            err_msg = "Error while grabbing EFF password list"
            print(err_msg)
        words = response.text.splitlines()
        word_dict = {}
        for l in words:
            split_line = l.split("\t")
            key = split_line[0]
            value = split_line[1]
            word_dict[key] = value

        #Tirage et génération de la passphrase
        self.wordlist= []
        for i in range(6):

            dice_roll = []
            for i in range(5):
                dice_roll.append(random.randrange(1,6))
        
            dice_result = ''.join(map(str, dice_roll))
            self.wordlist.append(word_dict[dice_result])
        
        
        