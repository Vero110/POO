import tkinter as tk
from tkinter import Entry, Label, Tk, TkVersion
productos = {
    "Coca-cola 600ML $16": 16,
    "Sabritas $20": 20,
    "Garrafon de Agua $50": 50,
    "Pan Bimbo $45": 45,
    "Tortillas $22": 22,
    "Fabuloso $30": 30,
    "Cloro $20": 20,
    "Cepillo de dientes $17": 17,
    "Leche $26": 26,
    "Mazapan $7": 7
}
total = 0
carrito = []
def comprar_producto():
    producto = listbox.get(tk.ACTIVE)
    carrito.append(producto)
    precio = productos[producto]
    global total
    total += precio
    actualizar_total()
def eliminar_producto():
    producto = listbox.get(tk.ACTIVE)
    carrito.append(producto)
    precio = productos[producto]
    global total
    total += precio
    actualizar_total()
def agregar_producto():
    producto = listbox.get(tk.ACTIVE)
    carrito.append(producto)
    precio = productos[producto]
    global total
    total += precio
    actualizar_total()
def actualizar_total():
    total_label.config(text="Total: $" + str(total))
root = tk.Tk()
root.title("Bienvenido a la tiendita")
root.geometry("800x500")
listbox = tk.Listbox(root)
for producto in productos:
    listbox.insert(tk.END, producto)
listbox.pack()
agregar_button = tk.Button(root, text="Agregar al carrito", command=agregar_producto)
agregar_button.pack()
eliminar_button = tk.Button(root, text="Eliminar producto del carrito", command=eliminar_producto)
eliminar_button.pack()
total_label = tk.Label(root, text="Total: $0")
total_label.pack()
comprar_button = tk.Button(root, text="Comprar", command=comprar_producto)
comprar_button.pack()
label = Label(root, text="Agregue su ubicación de favor:",fg="black")
label.pack()
ubicacion = Entry(root)
ubicacion.pack()
root.mainloop()