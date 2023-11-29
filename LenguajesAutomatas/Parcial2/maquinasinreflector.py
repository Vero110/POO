import string
import random

class EnigmaMachine:
    def __init__(self, rotor_positions):
        self.rotors = [list(string.ascii_uppercase), list(string.ascii_uppercase)]
        self.rotor_positions = rotor_positions

    def set_rotor_positions(self, positions):
        for i in range(len(positions)):
            self.rotor_positions[i] = positions[i]

    def rotate_rotors(self):
        for i in range(len(self.rotors) - 1, 0, -1):
            if i == len(self.rotors) - 1:
                self.rotors[i] = self.rotors[i][1:] + [self.rotors[i][0]]
            else:
                if self.rotors[i + 1][0] == self.rotors[i][25]:
                    self.rotors[i] = self.rotors[i][1:] + [self.rotors[i][0]]
                else:
                    break

    def encrypt_letter(self, letter):
        for i in range(len(self.rotors)):
            letter = self.rotors[i][(ord(letter) - ord('A') + self.rotor_positions[i]) % 26]
        return letter

    def encrypt_message(self, message):
        encrypted_message = ''
        for char in message:
            if char.isalpha():
                encrypted_message += self.encrypt_letter(char.upper())
                self.rotate_rotors()
            else:
                encrypted_message += char
        return encrypted_message

# Ejemplo de uso
rotor_positions = [0, 0]
enigma = EnigmaMachine(rotor_positions)

mensaje = "HELLO"
mensaje_cifrado = enigma.encrypt_message(mensaje)
print(f"Mensaje original: {mensaje}")
print(f"Mensaje cifrado: {mensaje_cifrado}")
