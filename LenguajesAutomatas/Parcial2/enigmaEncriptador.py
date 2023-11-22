import random

class EnigmaMachine:
    #Lista de rotores configurados aleatoriamente, reflector: Diccionario que representa el reflector configurado aleatoriamente.
    def __init__(self):
        #nicializa una instancia de la maq enigma con configuraciones aleatorias
        self.rotors = [dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 26))) for _ in range(3)]
        self.reflector = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 26)))

    def encrypt(self, char):
        #ifra un carácter utilizando los rotores y el reflector
        for rotor in reversed(self.rotors):
            char = rotor[char]
        char = self.reflector[char]
        for rotor in self.rotors:
            char = {v: k for k, v in rotor.items()}[char]
        return char

def encrypt_message(message):
    # mensaje utilizando una instancia de EnigmaMachine
    enigma = EnigmaMachine()
    return ''.join([enigma.encrypt(char) for char in message])

# Ejemplo de uso para encriptar
mensaje_original = "VERONICA"
mensaje_encriptado = encrypt_message(mensaje_original)

print("Mensaje original:", mensaje_original)
print("Mensaje encriptado:", mensaje_encriptado)
