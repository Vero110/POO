import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import sqlite3


class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} - {self.cantidad} disponibles"


class Tienda:
    def __init__(self):
        self.conexion = sqlite3.connect("tienda.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                precio REAL,
                cantidad INTEGER
            )
        """)
        self.conexion.commit()

    def agregar_producto(self, producto):
        self.cursor.execute("INSERT INTO productos (nombre, precio, cantidad) VALUES (?, ?, ?)",
                            (producto.nombre, producto.precio, producto.cantidad))
        self.conexion.commit()

    def eliminar_producto(self, producto):
        self.cursor.execute("DELETE FROM productos WHERE id = ?", (producto.id,))
        self.conexion.commit()


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        for item in self.items:
            if item[0].id == producto.id:
                item[1] += cantidad
                break
        else:
            self.items.append((producto, cantidad))

    def eliminar_producto(self, producto):
        for item in self.items:
            if item[0].id == producto.id:
                self.items.remove(item)
                break

    def costo_total(self):
        return sum(item[0].precio * item[1] for item in self.items)

    def generar_ticket(self, cursor):
        ticket = "------------------\nTICKET DE COMPRA\n------------------\n"
        for item in self.items:
            ticket += f"{item[0].nombre}: {item[1]} x ${item[0].precio:.2f} = ${item[0].precio * item[1]:.2f}\n"
            cursor.execute("UPDATE productos SET cantidad = cantidad - ? WHERE id = ?", (item[1], item[0].id))
        ticket += f"\nCosto total: ${self.costo_total():.2f}"
        return ticket


class TiendaGUI:
    def __init__(self, tienda, carrito):
        self.tienda = tienda
        self.carrito = carrito

        self.conexion = sqlite3.connect("tienda.db")
        self.cursor = self.conexion.cursor()

        self.ventana = tk.Tk()
        self.ventana.title

tienda = Tienda()
tienda.agregar_producto(Producto("Laptop", 15000, 10))
tienda.agregar_producto(Producto("Smartphone", 8000, 20))
tienda.agregar_producto(Producto("Tablet", 5000, 15))
tienda.agregar_producto(Producto("Impresora", 4000, 5))
carrito = Carrito()
tienda_gui = TiendaGUI(tienda, carrito)
