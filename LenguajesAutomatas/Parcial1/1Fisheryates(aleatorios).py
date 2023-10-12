# numeros aleatorios 
import tkinter as tk
from tkinter import simpledialog
from random import randrange

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def shuffle(A):
    for i in range(len(A) - 1):
        j = randrange(i, len(A))
        swap(A, i, j)

def shuffle_numbers():
    num_data = simpledialog.askinteger("Cantidad de Números", "Cuántos números desea ingresar:")
    if num_data is not None:
        A = []

        for i in range(num_data):
            dato = simpledialog.askinteger("Ingresar Número", f"Ingrese el número {i + 1}:")
            if dato is not None:
                A.append(dato)

        shuffle(A)

        result_label.config(text="Lista barajada:\n" + ', '.join(map(str, A)))

# Crear la ventana principal
root = tk.Tk()
root.title("Barajar Números")

# Botón para barajar números
shuffle_button = tk.Button(root, text="Barajar Números", command=shuffle_numbers)
shuffle_button.pack()

# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
