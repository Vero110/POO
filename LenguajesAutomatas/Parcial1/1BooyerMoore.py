import tkinter as tk
from tkinter import simpledialog, messagebox

def find_majority_element(elements):
    count = {}
    for element in elements:
        count[element] = count.get(element, 0) + 1
    for key, value in count.items():
        if value > len(elements) / 2:
            return key
    return None

def find_majority_element_button():
    data_input = input_entry.get()
    elements = data_input.split(',')
    
    if len(elements) != num_data:
        messagebox.showwarning("Error", "Ingresa " + str(num_data) + " elementos")
    else:
        result = find_majority_element(elements)
        
        if result is not None:
            result_label.config(text='El elemento mayoritario es: ' + str(result))
        else:
            result_label.config(text='El elemento mayoritario no existe')

# Crear la ventana principal
root = tk.Tk()
root.title("Mayoría de Elementos")

# Pregunta cuántos datos se desean ingresar
num_data = simpledialog.askinteger("Cantidad de Datos", "¿Cuántos datos desea ingresar?")


# Etiqueta para ingresar datos
input_label = tk.Label(root, text=f"Ingrese {num_data} elementos separados por comas:")
input_label.pack()

# Cuadro de entrada de datos
input_entry = tk.Entry(root)
input_entry.pack()

# Botón para encontrar el elemento mayoritario
find_button = tk.Button(root, text="Encontrar Elemento Mayoritario", command=find_majority_element_button)
find_button.pack()

# Etiqueta para mostrar el resultado
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
