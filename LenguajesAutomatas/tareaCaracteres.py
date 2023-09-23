import tkinter as tk
from tkinter import messagebox

def findMajorityLetter(word):
    if len(word) == 0:
        return None

    majority_letter = None
    count = 0

    for letter in word:
        if count == 0:
            majority_letter = letter
            count = 1
        elif letter == majority_letter:
            count += 1
        else:
            count -= 1

    if word.count(majority_letter) > len(word) / 2:
        return majority_letter
    else:
        return None

def find_majority_letter():
    word = word_entry.get()
    result = findMajorityLetter(word)

    if result:
        messagebox.showinfo("Resultado", f'La letra mayoritaria en la palabra "{word}" es: {result}')
    else:
        messagebox.showinfo("Resultado", f'No existe una letra mayoritaria en la palabra "{word}".')

# Configuración de la ventana principal
root = tk.Tk()
root.title("Encontrar Letra Mayoritaria")

# Etiqueta y entrada para la palabra
word_label = tk.Label(root, text="Ingrese una palabra:")
word_label.pack()
word_entry = tk.Entry(root)
word_entry.pack()

# Botón para encontrar la letra mayoritaria
find_button = tk.Button(root, text="Encontrar Letra Mayoritaria", command=find_majority_letter)
find_button.pack()

root.mainloop()
