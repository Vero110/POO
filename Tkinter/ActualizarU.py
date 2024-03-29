import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Tienda import InterfazTiendita
from logicaproyecto import Login, Resgistro

class Interfaz:


    def __init__(self, ventana):
        # Instanciamos un objeto ventana
        self.ventana = ventana
        self.ventana.title("Inicie sesion")
        self.ventana.geometry("600x400")
        self.ventana.config(bg='#A9F5BC')

        # Creamos un widget Notebook
        self.notebook = ttk.Notebook(self.ventana)
        self.notebook.pack(fill='both', expand=True)

        # Creamos la primera pestaña
        self.pagina1 = ttk.Frame(self.notebook)
        self.notebook.add(self.pagina1, text="Iniciar sesión")
        
        titulo1 = tk.Label(self.pagina1, text="Usuario:", font=("Helvetica",30), bg='#A9F5BC').pack(padx=20,pady=5)
        self.usuario = tk.Entry(self.pagina1, font=("Helvetica", 30), bg='#A9F5BC')
        self.usuario.pack(padx=20,pady=10)

        titulo2 = tk.Label(self.pagina1, text="Contraseña:", font=("Helvetica", 30), bg='#A9F5BC').pack(padx=20, pady=5)
        self.contraseña = tk.Entry(self.pagina1, show="*", font=("Helvetica", 30), bg='#A9F5BC')
        self.contraseña.pack(padx=20, pady=10, )

        self.Generar= tk.Button(self.pagina1, text="Ingresar", fg="white", bg='#1174B5', font=("Helvetica", 15), command=self.verificar)
        self.Generar.pack()

    def verificar(self):
        Usuario = self.usuario.get()
        Password = self.contraseña.get()
        if Usuario == "" or Password == "":
            mensaje = "Ingrese ambos campos"
        else:
            login = Login(Usuario, Password)
            if login.login():
                mensaje="Bienvenido"
                # muestra el mensaje en una ventana emergente
                messagebox.showinfo(title="Resultado", message=mensaje)
                # Cierra la ventana principal
                self.ventana.destroy()
                # Crea una instancia de InterfazTiendita
                tiendita = InterfazTiendita()
                # Llama al método mainloop de la ventana
                tiendita.root.mainloop()
            else:
                mensaje = "Revise sus datos e intente de nuevo."
                # muestra el mensaje de error en una ventana emergente
                messagebox.showerror(title="Resultado", message=mensaje)
ventana= tk.Tk()
interfaz_login=Interfaz(ventana)
ventana.mainloop()