import tkinter as tk
import sqlite3
from tkinter import messagebox


# Conectar a la base de datos
conn = sqlite3.connect('Juan, Pedro')
c = conn.cursor()

# Crear la tabla de usuarios si no existe
c.execute('''CREATE TABLE IF NOT EXISTS usuarios 
             (username TEXT PRIMARY KEY, password TEXT, role TEXT)''')
conn.commit()

# Agregar algunos usuarios de ejemplo a la base de datos
c.execute("INSERT OR IGNORE INTO usuarios VALUES ('gerente', '123456', 'gerente')")
c.execute("INSERT OR IGNORE INTO usuarios VALUES ('cliente', 'abcdef', 'cliente')")
conn.commit()

# Crear la ventana de inicio de sesión
class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('Inicio de sesión')
        
        # Crear los campos de entrada de usuario y contraseña
        self.username_label = tk.Label(self, text='Nombre de usuario')
        self.username_entry = tk.Entry(self)
        
        self.password_label = tk.Label(self, text='Contraseña')
        self.password_entry = tk.Entry(self, show='*')
        
        # Agregar botón de inicio de sesión
        self.login_button = tk.Button(self, text='Iniciar sesión', command=self.login)
        
        # Colocar los widgets en la ventana
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()
        
    def login(self):
        # Obtener los valores de entrada del usuario y la contraseña
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Buscar al usuario en la base de datos
        c.execute("SELECT * FROM usuarios WHERE username = ?", (username,))
        user = c.fetchone()
        
        if user is None:
            # Si el usuario no existe, mostrar mensaje de error
            tk.messagebox.showerror('Error', 'El usuario no existe')
        elif user[1] != password:
            # Si la contraseña no coincide, mostrar mensaje de error
            tk.messagebox.showerror('Error', 'Contraseña incorrecta')
        elif user[2] == 'gerente':
            # Si el usuario es un gerente, abrir la ventana de gerente
            self.destroy()
            #GerenteWindow()
        elif user[2] == 'cliente':
            # Si el usuario es un cliente, abrir la ventana de cliente y bloquear la ventana de gerente
            self.destroy()
            ClienteWindow()
        
class ClienteWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('Ventana de cliente')
        
        # Deshabilitar la ventana de gerente para los clientes
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.close)
        
        # Crear los elementos de la ventana de cliente
        self.message_label = tk.Label(self, text='Bienvenido, cliente!')
        self.logout_button = tk.Button(self, text='Cerrar sesión', command=self.close)
        
        # Colocar los widgets en