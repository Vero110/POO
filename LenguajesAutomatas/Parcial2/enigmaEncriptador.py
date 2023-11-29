import tkinter as tk
from tkinter import ttk

# Definición de la clase EnigmaMachine
class EnigmaMachine:
    def __init__(self, rotors, reflectors):
        self.rotors = rotors
        self.reflectors = reflectors

    # Método para encriptar un mensaje
    def encrypt(self, message, reflector_index):
        encrypted_message = ""
        reflector = self.reflectors[reflector_index]
        
        for char in message:
            encrypted_char = char
            # Encriptar con cada rotor
            for rotor in self.rotors:
                encrypted_char = rotor.encrypt(encrypted_char)
            # Reflejar
            encrypted_char = reflector.reflect(encrypted_char)
            # Encriptar en reversa con cada rotor
            for rotor in reversed(self.rotors):
                encrypted_char = rotor.encrypt(encrypted_char, reverse=True)
            encrypted_message += encrypted_char
        return encrypted_message

    # Método para desencriptar un mensaje
    def decrypt(self, message, reflector_index):
        return self.encrypt(message, reflector_index)

# Clase Rotor
class Rotor:
    def __init__(self, wiring):
        self.wiring = wiring

    # Método para encriptar un carácter
    def encrypt(self, char, reverse=False):
        if not reverse:
            return self.wiring[char]
        else:
            return next(key for key, value in self.wiring.items() if value == char)

# Clase Reflector
class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring

    # Método para reflejar un carácter
    def reflect(self, char):
        try:
            return self.wiring[char]
        except KeyError:
            # Manejo de excepción si la letra no está presente en el mapa de conexiones del reflector
            print(f"Error: La letra '{char}' no está presente en el mapa de conexiones del reflector.")
            return char

# Clase EnigmaGUI
class EnigmaGUI:
    def __init__(self, master):
        self.master = master
        master.title("Enigma Machine")

        # Preguntar número de reflectores
        reflector_count = tk.StringVar(value='2')
        reflector_label = ttk.Label(master, text="Número de reflectores:")
        reflector_label.grid(row=0, column=0, padx=10, pady=10)
        reflector_entry = ttk.Entry(master, textvariable=reflector_count)
        reflector_entry.grid(row=0, column=1, padx=10, pady=10)

        # Preguntar si se utilizarán los reflectores
        use_reflectors = tk.BooleanVar(value=True)
        reflectors_checkbox = ttk.Checkbutton(master, text="¿Utilizar reflectores?", variable=use_reflectors)
        reflectors_checkbox.grid(row=1, column=0, columnspan=2, pady=10)

        # Configuración inicial de rotores y reflectores
        self.rotor1 = Rotor({"A": "B", "B": "C", "C": "D", "D": "E", "E": "F", "F": "G", "G": "H", "H": "I", "I": "J", "J": "K", "K": "L", "L": "M", "M": "N", "N": "O", "O": "P", "P": "Q", "Q": "R", "R": "S", "S": "T", "T": "U", "U": "V", "V": "W", "W": "X", "X": "Y", "Y": "Z", "Z": "A"})
        self.rotor2 = Rotor({"A": "Z", "B": "Y", "C": "X", "D": "W", "E": "V", "F": "U", "G": "T", "H": "S", "I": "R", "J": "Q", "K": "P", "L": "O", "M": "N", "N": "M", "O": "L", "P": "K", "Q": "J", "R": "I", "S": "H", "T": "G", "U": "F", "V": "E", "W": "D", "X": "C", "Y": "B", "Z": "A"})

        # Configuración inicial de la máquina Enigma
        if use_reflectors.get():
            reflectors = [
                Reflector({"A": "Y", "B": "Z", "C": "X", "D": "W", "E": "V", "F": "U", "G": "T", "H": "S", "I": "R", "J": "Q", "K": "P", "L": "O", "M": "N", "N": "M", "O": "L", "P": "K", "Q": "J", "R": "I", "S": "H", "T": "G", "U": "F", "V": "E", "W": "D", "X": "C", "Y": "B", "Z": "A"}),
                # Agrega más reflectores si es necesario
            ]
            self.enigma = EnigmaMachine([self.rotor1, self.rotor2], reflectors)
        else:
            self.enigma = EnigmaMachine([self.rotor1, self.rotor2], [Reflector({})])

        # Etiqueta y cuadro de entrada
        self.label = ttk.Label(master, text="Palabra:")
        self.label.grid(row=2, column=0, padx=10, pady=10)
        self.entry = ttk.Entry(master)
        self.entry.grid(row=2, column=1, padx=10, pady=10)

        # Botones de encriptar y desencriptar
        self.encrypt_button = ttk.Button(master, text="Encriptar", command=self.encrypt_message)
        self.encrypt_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.decrypt_button = ttk.Button(master, text="Desencriptar", command=self.decrypt_message)
        self.decrypt_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Etiqueta para mostrar el resultado
        self.result_label = ttk.Label(master, text="")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)

    # Método para encriptar un mensaje y mostrar el resultado
    def encrypt_message(self):
        message = self.entry.get().upper()
        reflector_index = 0  # Utilizamos el primer reflector por defecto
        encrypted_message = self.enigma.encrypt(message, reflector_index)
        self.result_label.configure(text=f"Palabra encriptada: {encrypted_message}")

    # Método para desencriptar un mensaje y mostrar el resultado
    def decrypt_message(self):
        message = self.entry.get().upper()
        reflector_index = 0  # Utilizamos el primer reflector por defecto
        decrypted_message = self.enigma.decrypt(message, reflector_index)
        self.result_label.configure(text=f"Palabra desencriptada: {decrypted_message}")

# Función principal para ejecutar la aplicación
def main():
    root = tk.Tk()
    app = EnigmaGUI(root)
    root.mainloop()

# Verificar si el script está siendo ejecutado directamente
if __name__ == "__main__":
    main()
