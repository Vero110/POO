from tkinter import *
from tkinter import messagebox
import sqlite3
import tkinter as tk


import bcrypt

class Login:
    
    def __init__(self, usuario, contraseña):
            self.usuario = usuario
            self.contraseña = contraseña

    def login(self):
        try:
            conx = sqlite3.connect("C:/Users/52442/Documents/GitHub/POO/SQLite/DBUsuarios.db")
            cursor = conx.cursor()
            qrSelect = "SELECT * FROM Usuarios WHERE NombreUsu=? AND Contraseña=?"
            cursor.execute(qrSelect, (self.usuario, self.contraseña))
            resultado = cursor.fetchone()
            conx.close()

            if resultado:
                return True
            else:
                return False

        except sqlite3.OperationalError:
            print("Error de conexion a la BD")
            return False

class Resgistro:
    
    def __init__(self):
        pass
    
    # Metodo para intentar una conexión a la BD
    def conexionBD(self):
        try:
            conexion=sqlite3.connect("D:/documentos/GitHub/Proyecto_Integrador/TiendaQueveDoes.db")
            print("Conexion exitosa")
            return conexion            
        except sqlite3.OperationalError:
            print("Error de conexion a la BD")
        
    # Metodo para capturar datos del entry
    def guardarUsuarios(self, nom, cor, con):
        
        #1. usamos una conexión para registrar
        conx= self.conexionBD()
        
        #2. Checar que el entry contenga algo
        if(nom== " " or cor == "" or con == ""):
            messagebox.showwarning("Aguas", "Formulario incompleto")
        else:
            #3. Preparamos Cursor, Datos, QuerySQL
            cursor = conx.cursor()
            # Se manda a encriptar la contraseña y se agrega en el paquete de datos enviados a la BD
            datos=(nom, cor, con)
            qrInsert= "insert into Usuarios(NombreUsu, Puesto, Contraseña) values(?,?,?)"
            
            #4. Ejecutar Insert y cerramos conexion
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Usuario Guardado")
            
    def login(self):
        conx = sqlite3.connect("C:/Users/52442/Documents/GitHub/POO/SQLite/DBUsuarios.db")
        cursor = conx.cursor()
        # Obtener los valores de entrada del usuario y la contraseña
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Buscar al usuario en la base de datos
        conx.execute("SELECT * FROM usuarios WHERE username = ?", (username,))
        user = conx.fetchone()
        
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