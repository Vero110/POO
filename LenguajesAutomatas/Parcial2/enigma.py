import tkinter as tk
from tkinter import ttk

#definición de la clase de la maq enigma
class EnigmaMachine:
    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector

    # metodo para encriptar un mensaje
    def encrypt(self, message):
        encrypted_message = ""
        for char in message:
            encrypted_char = char
            # Encriptar 
            for rotor in self.rotors:
                encrypted_char = rotor.encrypt(encrypted_char)
            # Reflejar
            encrypted_char = self.reflector.reflect(encrypted_char)
            # Encriptar en reversa con cada rotor
            for rotor in reversed(self.rotors):
                encrypted_char = rotor.encrypt(encrypted_char, reverse=True)
            encrypted_message += encrypted_char
        return encrypted_message

    # Método para desencriptar un mensaje 
    def decrypt(self, message):
        return self.encrypt(message)  

# Definición de la clase Rotor que representa un rotor en la máquina Enigma
class Rotor:
    def __init__(self, wiring):
        self.wiring = wiring

    # Metodo para encriptar un carácter
    def encrypt(self, char, reverse=False):
        if not reverse:
            return self.wiring[char]
        else:
            return next(key for key, value in self.wiring.items() if value == char)

#clase reflector que representa el reflector en la máquina Enigma
class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring

    # Método para reflejar un carácter
    def reflect(self, char):
        return self.wiring[char]

# Definición de la clase EnigmaGUI que representa la interfaz gráfica de la máquina Enigma
class EnigmaGUI:
    def __init__(self, master):
        self.master = master
        master.title("Enigma Machine")

        # Etiqueta y cuadro de entrada
        self.label = ttk.Label(master, text="Mensaje:")
        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.entry = ttk.Entry(master)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        # Botones de encriptar y desencriptar
        self.encrypt_button = ttk.Button(master, text="Encriptar", command=self.encrypt_message)
        self.encrypt_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.decrypt_button = ttk.Button(master, text="Desencriptar", command=self.decrypt_message)
        self.decrypt_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Etiqueta para mostrar el resultado
        self.result_label = ttk.Label(master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

        # Configuración inicial de rotores y reflector
        self.rotor1 = Rotor({"A": "B", "B": "C", "C": "D", "D": "E", "E": "F", "F": "G", "G": "H", "H": "I", "I": "J", "J": "K", "K": "L", "L": "M", "M": "N", "N": "O", "O": "P", "P": "Q", "Q": "R", "R": "S", "S": "T", "T": "U", "U": "V", "V": "W", "W": "X", "X": "Y", "Y": "Z", "Z": "A"})
        self.rotor2 = Rotor({"A": "Z", "B": "Y", "C": "X", "D": "W", "E": "V", "F": "U", "G": "T", "H": "S", "I": "R", "J": "Q", "K": "P", "L": "O", "M": "N", "N": "M", "O": "L", "P": "K", "Q": "J", "R": "I", "S": "H", "T": "G", "U": "F", "V": "E", "W": "D", "X": "C", "Y": "B", "Z": "A"})
        self.reflector = Reflector({"A": "Y", "B": "Z", "C": "X", "D": "W", "E": "V", "F": "U", "G": "T", "H": "S", "I": "R", "J": "Q", "K": "P", "L": "O", "M": "N", "N": "M", "O": "L", "P": "K", "Q": "J", "R": "I", "S": "H", "T": "G", "U": "F", "V": "E", "W": "D", "X": "C", "Y": "B", "Z": "A"})

        # Configuración inicial de la máquina Enigma
        self.enigma = EnigmaMachine([self.rotor1, self.rotor2], self.reflector)

    # Método para encriptar un mensaje y mostrar el resultado
    def encrypt_message(self):
        message = self.entry.get().upper()
        encrypted_message = self.enigma.encrypt(message)
        self.result_label.configure(text=f"Mensaje encriptado: {encrypted_message}")

    # Método para desencriptar un mensaje y mostrar el resultado
    def decrypt_message(self):
        message = self.entry.get().upper()
        decrypted_message = self.enigma.decrypt(message)
        self.result_label.configure(text=f"Mensaje desencriptado: {decrypted_message}")

# Función principal para ejecutar la aplicación
def main():
    root = tk.Tk()
    app = EnigmaGUI(root)
    root.mainloop()

# Verificar si el script está siendo ejecutado directamente
if __name__ == "__main__":
    main()
