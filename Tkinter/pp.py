import tkinter as tk
from tkinter import ttk, messagebox

class AlmacendeBebidas:
    def __init__(self):
        self.bebidas = []
        
        self.ventana = tk.Tk()
        self.ventana.title("Almacenamiento de Bebidas")

        self.Control = ttk.Notebook(self.ventana)

        self.pag1 = ttk.Frame(self.Control)
        self.Control.add(self.pag1, text="Alta de Bebidas")
        
        self.pag2 = ttk.Frame(self.Control)
        self.Control.add(self.pag2, text="Baja de Bebidas")
        
        self.pag3 = ttk.Frame(self.Control)
        self.Control.add(self.pag3, text="Actualización de Bebidas")
        
        self.pag4 = ttk.Frame(self.Control)
        self.Control.add(self.pag4, text="Consulta de Bebidas")
        
        # Configurar pestaña Agregar
        self.etiID = tk.Label(self.pag1, text="ID:")
        self.entrID = tk.Entry(self.pag1)
        
        self.etiNombre = tk.Label(self.pag1, text="Nombre:")
        self.entrNombre = tk.Entry(self.pag1)
        
        self.etiClasif = tk.Label(self.pag1, text="Clasificación:")
        self.entrClasif = tk.Entry(self.pag1)
        
        self.etiMarca = tk.Label(self.pag1, text="Marca:")
        self.entrMarca = tk.Entry(self.pag1)
        
        self.etiPrecio = tk.Label(self.pag1, text="Precio:")
        self.entrPrecio = tk.Entry(self.pag1)
        
        self.agregar = tk.Button(self.pag1, text="Agregar", command=self.Alta_Bebidas)
        self.calcularpormarca = tk.Button(self.pag1, text="Cantidad por marca", command=self.Cantidad_Marcas)
        self.calcularporclasificacion = tk.Button(self.pag1, text="Cantidad por clasificación", command=self.Cantidad_Clasificacion)

        self.etiID.grid(row=1, column=1)
        self.entrID.grid(row=1, column=2)
        self.etiNombre.grid(row=2, column=1)
        self.entrNombre.grid(row=2, column=2)
        self.etiClasif.grid(row=3, column=1)
        self.entrClasif.grid(row=3, column=2)
        self.etiMarca.grid(row=4, column=1)
        self.entrMarca.grid(row=4, column=2)
        self.etiPrecio.grid(row=5, column=1)
        self.entrPrecio.grid(row=5, column=2)
        self.agregar.grid(row=6, column=1)
        self.calcularpormarca.grid(row=6, column=2)
        self.calcularporclasificacion.grid(row=7, column=1, columnspan=3)

        # Configurar pestaña Eliminar
        self.bajalID = tk.Label(self.pag2, text="ID:")
        self.bajaeID = tk.Entry(self.pag2)
        self.baja = tk.Button(self.pag2, text="Eliminar", command=self.Baja_Bebida)

        self.bajalID.grid(row=1, column=1)
        self.bajaeID.grid(row=1, column=2)
        self.baja.grid(row=2, column=1)

        # Configurar pestaña Actualizar
        self.IDactL = tk.Label(self.pag3, text="ID:")
        self.IDeactE = tk.Entry(self.pag3)
        self.NombreAcL = tk.Label(self.pag3, text="Nombre:")
        self.NombreAcE = tk.Entry(self.pag3)
        self.ClasificacionAcL = tk.Label(self.pag3, text="Clasificación:")
        self.ClasificacionAcE = tk.Entry(self.pag3)
        self.MarcaAcL = tk.Label(self.pag3, text="Marca:")
        self.MarcaAcE = tk.Entry(self.pag3)
        self.PrecioAcL = tk.Label(self.pag3, text="Precio:")
        self.PrecioAcE = tk.Entry(self.pag3)
        self.Actualizar = tk.Button(self.pag3, text="Actualizar", command=self.Actualizar_Bebida)

        self.IDactL.grid(row=1, column=1)
        self.IDeactE.grid(row=1, column=2)
        self.NombreAcL.grid(row=2, column=1)
        self.NombreAcE.grid(row=2, column=2)
        self.ClasificacionAcL.grid(row=3, column=1)
        self.ClasificacionAcE.grid(row=3, column=2)
        self.MarcaAcL.grid(row=4, column=1)
        self.MarcaAcE.grid(row=4, column=2)
        self.PrecioAcL.grid(row=5, column=1)
        self.PrecioAcE.grid(row=5, column=2)
        self.Actualizar.grid(row=6, column=1)

        # Configurar pestaña Mostrar
        self.mostrar = tk.Button(self.pag4, text="Mostrar todas", command=self.Mostrar_Bebidas)
        self.preciopromedio = tk.Button(self.pag4, text="Calcular precio promedio", command=self.Precio_Promedio)

        self.mostrar.pack()
        self.preciopromedio.pack()

        self.Control.pack()
        self.ventana.mainloop()

    def Alta_Bebidas(self):
        id = int(self.entrID.get())
        nombre = self.entrID.get()
        clasificacion = self.entrClasif.get()
        marca = self.entrMarca.get()
        precio = float(self.entrPrecio.get())

        bebida = {'id': id, 'nombre': nombre, 'clasificacion': clasificacion, 'marca': marca, 'precio': precio}
        self.bebidas.append(bebida)

        self.entrID.delete(0, tk.END)
        self.entrNombre.delete(0, tk.END)
        self.entrClasif.delete(0, tk.END)
        self.entrMarca.delete(0, tk.END)
        self.entrPrecio.delete(0, tk.END)

        messagebox.showinfo("Bebida agregada", "La bebida se agregó correctamente")

    def Baja_Bebida(self):
        id = int(self.bajaeID.get())

        for bebida in self.bebidas:
            if bebida['id'] == id:
                self.bebidas.remove(bebida)
                messagebox.showinfo("Eliminado", "La bebida ya se elimino")
                return

    def Actualizar_Bebida(self):
        id = int(self.IDeactE.get())
        nombre = self.NombreAcE.get()
        clasificacion = self.ClasificacionAcE.get()
        marca = self.MarcaAcE.get()
        precio = float(self.PrecioAcE.get())

        for bebida in self.bebidas:
            if bebida['id'] == id:
                bebida['nombre'] = nombre
                bebida['clasificacion'] = clasificacion
                bebida['marca'] = marca
                bebida['precio'] = precio
                messagebox.showinfo("Actualizado", "Los campos se actualizaron correctamente")
                return

        messagebox.showerror("Error", "No se encontró ninguna bebida con ese ID")

    def Mostrar_Bebidas(self):
        if self.bebidas:
            bebidas_str = ""
            for bebida in self.bebidas:
                bebidas_str += f"ID: {bebida['id']}, Nombre: {bebida['nombre']}, Clasificación: {bebida['clasificacion']}, Marca: {bebida['marca']}, Precio: {bebida['precio']}\n"
            messagebox.showinfo("Bebidas", bebidas_str)
        else:
            messagebox.showwarning("Advertencia", "No hay bebidas")

    def Precio_Promedio(self):
        if self.bebidas:
            precioTotal = sum(bebida['precio'] for bebida in self.bebidas)
            promedio = precioTotal / len(self.bebidas)
            messagebox.showinfo("Precio promedio", f"El precio promedio de las bebidas es: {promedio}")

    def Cantidad_Marcas(self):
        marca = self.entrMarca.get()
        cantidad = sum(1 for bebida in self.bebidas if bebida['marca'] == marca)
        messagebox.showinfo("Cantidad por marca", f"La cantidad de bebidas de la marca {marca} es: {cantidad}")

    def Cantidad_Clasificacion(self):
        clasificacion = self.entrClasif.get()
        cantidad = sum(1 for bebida in self.bebidas if bebida['clasificacion'] == clasificacion)
        messagebox.showinfo("Cantidad por clasificación", f"La cantidad de bebidas de la clasificación {clasificacion} es: {cantidad}")

app = AlmacendeBebidas()

