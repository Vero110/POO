import tkinter as tk
from tkinter import messagebox

class ProductosApp:
    def __init__(self):
        self.bebidas = []

        self.window = tk.Tk()
        self.window.title("Productos")

        # Crear elementos de la interfaz gráfica
        self.label_id = tk.Label(self.window, text="ID:")
        self.entry_id = tk.Entry(self.window)
        self.label_nombre = tk.Label(self.window, text="Nombre:")
        self.entry_nombre = tk.Entry(self.window)
        self.label_clasificacion = tk.Label(self.window, text="Clasificación:")
        self.entry_clasificacion = tk.Entry(self.window)
        self.label_marca = tk.Label(self.window, text="Marca:")
        self.entry_marca = tk.Entry(self.window)
        self.label_precio = tk.Label(self.window, text="Precio:")
        self.entry_precio = tk.Entry(self.window)
        self.button_agregar = tk.Button(self.window, text="Agregar", command=self.agregar_producto)
        self.button_eliminar = tk.Button(self.window, text="Eliminar", command=self.eliminar_producto)
        self.button_actualizar = tk.Button(self.window, text="Actualizar", command=self.actualizar_producto)
        self.button_mostrar = tk.Button(self.window, text="Mostrar todas", command=self.mostrar_producto)
        self.button_precio_promedio = tk.Button(self.window, text="Calcular precio promedio", command=self.calcular_precio_promedio)
        self.button_cantidad_marca = tk.Button(self.window, text="Cantidad por marca", command=self.contar_producto_por_marca)
        self.button_cantidad_clasificacion = tk.Button(self.window, text="Cantidad por clasificación", command=self.contar_producto_por_clasificacion)

        # Posicionar elementos en la ventana
        self.label_id.grid(row=0, column=0)
        self.entry_id.grid(row=0, column=1)
        self.label_nombre.grid(row=1, column=0)
        self.entry_nombre.grid(row=1, column=1)
        self.label_clasificacion.grid(row=2, column=0)
        self.entry_clasificacion.grid(row=2, column=1)
        self.label_marca.grid(row=3, column=0)
        self.entry_marca.grid(row=3, column=1)
        self.label_precio.grid(row=4, column=0)
        self.entry_precio.grid(row=4, column=1)
        self.button_agregar.grid(row=5, column=0)
        self.button_eliminar.grid(row=5, column=1)
        self.button_actualizar.grid(row=5, column=2)
        self.button_mostrar.grid(row=6, column=0)
        self.button_precio_promedio.grid(row=6, column=1)
        self.button_cantidad_marca.grid(row=6, column=2)
        self.button_cantidad_clasificacion.grid(row=7, column=0)

        self.window.mainloop()

    def agregar_producto(self):
        # Obtener los datos de los campos de entrada
        id = int(self.entry_id.get())
        nombre = self.entry_nombre.get()
        clasificacion = self.entry_clasificacion.get()
        marca = self.entry_marca.get()
        precio = float(self.entry_precio.get())

        # Agregar la bebida al almacén
        bebida = {'id': id, 'nombre': nombre, 'clasificacion': clasificacion, 'marca': marca, 'precio': precio}
        self.bebidas.append(bebida)

        # Limpiar los campos de entrada
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_clasificacion.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)

        messagebox.showinfo("Producto agregada", "El producto se agregó exitosamente al almacén.")

    def eliminar_producto(self):
        # Obtener el ID de la bebida a eliminar
        id = int(self.entry_id.get())

        for bebida in self.bebidas:
            if bebida['id'] == id:
                self.bebidas.remove(bebida)
                messagebox.showinfo("Eliminado", "Producto eliminada exitosamente.")
                return

        messagebox.showerror("Error", "No se encontró un producto con el ID especificado.")

    def actualizar_producto(self):
        # Obtener los datos actualizados de los campos de entrada
        id = int(self.entry_id.get())
        nombre = self.entry_nombre.get()
        clasificacion = self.entry_clasificacion.get()
        marca = self.entry_marca.get()
        precio = float(self.entry_precio.get())

        for bebida in self.bebidas:
            if bebida['id'] == id:
                bebida['nombre'] = nombre
                bebida['clasificacion'] = clasificacion
                bebida['marca'] = marca
                bebida['precio'] = precio
                messagebox.showinfo("Actualizado", "Producto actualizada exitosamente.")
                return

        messagebox.showerror("Error", "No se encontró un producto con el ID especificado.")

    def mostrar_producto(self):
        if self.bebidas:
            bebidas_str = ""
            for bebida in self.bebidas:
                bebidas_str += f"ID: {bebida['id']}, Nombre: {bebida['nombre']}, Clasificación: {bebida['clasificacion']}, Marca: {bebida['marca']}, Precio: {bebida['precio']}\n"
            messagebox.showinfo("Bebidas", bebidas_str)
        else:
            messagebox.showwarning("Advertencia", "No hay productos en el almacén.")

    def calcular_precio_promedio(self):
        if self.bebidas:
            total_precios = sum(bebida['precio'] for bebida in self.bebidas)
            promedio = total_precios / len(self.bebidas)
            messagebox.showinfo("Precio promedio", f"El precio promedio de las productos es: {promedio}")
        else:
            messagebox.showwarning("Advertencia", "No hay bebidas en el almacén.")

    def contar_producto_por_marca(self):
        marca = self.entry_marca.get()
        cantidad = sum(1 for bebida in self.bebidas if bebida['marca'] == marca)
        messagebox.showinfo("Cantidad por marca", f"La cantidad de productos de la marca {marca} es: {cantidad}")

    def contar_producto_por_clasificacion(self):
        clasificacion = self.entry_clasificacion.get()
        cantidad = sum(1 for bebida in self.bebidas if bebida['clasificacion'] == clasificacion)
        messagebox.showinfo("Cantidad por clasificación", f"La cantidad de productos de la clasificación {clasificacion} es: {cantidad}")

# Crear una instancia de la aplicación
app = ProductosApp()
