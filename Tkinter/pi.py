import tkinter as tk

class TiendaGUI:
    def _init_(self):
        self.productos = []

        self.ventana = tk.Tk()
        self.ventana.title("Tienda")

        # Crear los widgets
        self.lbl_nombre = tk.Label(self.ventana, text="Nombre:")
        self.lbl_precio = tk.Label(self.ventana, text="Precio:")
        self.lbl_stock = tk.Label(self.ventana, text="Stock:")
        self.lbl_mensaje = tk.Label(self.ventana, text="")
        self.ent_nombre = tk.Entry(self.ventana)
        self.ent_precio = tk.Entry(self.ventana)
        self.ent_stock = tk.Entry(self.ventana)
        self.btn_agregar = tk.Button(self.ventana, text="Agregar", command=self.agregar_producto)
        self.btn_eliminar = tk.Button(self.ventana, text="Eliminar", command=self.eliminar_producto)
        self.lst_productos = tk.Listbox(self.ventana)
        
        # Ubicar los widgets en la ventana
        self.lbl_nombre.grid(row=0, column=0)
        self.lbl_precio.grid(row=1, column=0)
        self.lbl_stock.grid(row=2, column=0)
        self.ent_nombre.grid(row=0, column=1)
        self.ent_precio.grid(row=1, column=1)
        self.ent_stock.grid(row=2, column=1)
        self.btn_agregar.grid(row=3, column=0)
        self.btn_eliminar.grid(row=3, column=1)
        self.lst_productos.grid(row=4, column=0, columnspan=2)

    def agregar_producto(self):
        nombre = self.ent_nombre.get()
        precio = float(self.ent_precio.get())
        stock = int(self.ent_stock.get())
        producto = (nombre, precio, stock)
        self.productos.append(producto)
        self.actualizar_lista()
        self.lbl_mensaje.config(text="Producto agregado.")

    def eliminar_producto(self):
        seleccion = self.lst_productos.curselection()
        if seleccion:
            index = seleccion[0]
            self.productos.pop(index)
            self.actualizar_lista()
            self.lbl_mensaje.config(text="Producto eliminado.")
        else:
            self.lbl_mensaje.config(text="Por favor seleccione un producto.")

    def actualizar_lista(self):
        self.lst_productos.delete(0, tk.END)
        for nombre, precio, stock in self.productos:
            texto = f"{nombre} - ${precio:.2f} - {stock} unidades"
            self.lst_productos.insert(tk.END, texto)

    def iniciar(self):
        self.actualizar_lista()
        self.ventana.mainloop()

if _name_ == "_main_":
    tienda = TiendaGUI()
    tienda.iniciar()