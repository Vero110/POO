import random

class EnigmaMachine:
    def __init__(self):
        self.rotors = [dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 26))) for _ in range(3)]
        self.reflector = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 26)))

    def encrypt(self, char):
        for rotor in self.rotors:
            char = rotor[char]
        char = self.reflector[char]
        for rotor in reversed(self.rotors):
            char = {v: k for k, v in rotor.items()}[char]
        return char

    def decrypt(self, char):
        for rotor in reversed(self.rotors):
            char = {v: k for k, v in rotor.items()}[char]
        char = {v: k for k, v in self.reflector.items()}[char]
        for rotor in self.rotors:
            char = rotor[char]
        return char

def encrypt_message(message, enigma):
    return ''.join([enigma.encrypt(char) for char in message])

def decrypt_message(encrypted_message, enigma):
    return ''.join([enigma.decrypt(char) for char in encrypted_message])

# Crear una instancia de EnigmaMachine para usar en todo el proceso
enigma = EnigmaMachine()

# Ejemplo de uso para encriptar
mensaje_original = "VERONICA"
mensaje_encriptado = encrypt_message(mensaje_original, enigma)

# Ejemplo de uso para desencriptar
mensaje_desencriptado = decrypt_message(mensaje_encriptado, enigma)

print("Mensaje original:", mensaje_original)
print("Mensaje encriptado:", mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)
