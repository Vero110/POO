import random
import string

class generadorContraseña:
    def __init__(self, length=8, include_uppercase=True, include_special_characters=True):
        self._length = length
        self._include_uppercase = include_uppercase
        self._include_special_characters = include_special_characters

    def set_length(self, length):
        self._length = length

    def include_uppercase(self, include_uppercase):
        self._include_uppercase = include_uppercase

    def include_special_characters(self, include_special_characters):
        self._include_special_characters = include_special_characters

    def generate_password(self):
        chars = string.ascii_lowercase
        if self._include_uppercase:
            chars += string.ascii_uppercase
        if self._include_special_characters:
            chars += string.punctuation

        password = "".join(random.choice(chars) for _ in range(self._length))
        return password
    



     








    

