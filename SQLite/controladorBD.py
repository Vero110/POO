from tkinter import messagebox
import sqlite3 
import bcrypt 

class controladorBD:
    def __init__(self):
        pass 
    
    # Metodo para la creacion de conexiones 
    def conexionBD(self):
        
        try:
            conexion = sqlite3.connect("C:/Users/52442/Documents/GitHub/POO/SQLite/DBUsuarios.db")
            print("Conectado a la base de datos")
            
            return conexion 

        except sqlite3.OperationalError:
            print("No se conecto a la base de datos")
        
    #Metodo para guardar usuarios en la BD
    def guardarUsuario(self, nom, cor, con):
        
        #1. Importar una conexion 
        #Usamos una conexion 
        conx = self.conexionBD()
        
        #2. Validar parametros VACIOS
        #no dejamos avanzar para no meter cosas que no queremos en la BD
        if (nom == "" or cor == "" or con == ""): 
            messagebox.showwarning("Advertencia", "El Formulario esta Incompleto")
        else: 
            #3. Preparar el CURSOR, DATOS, QUERYSQL
            cursor = conx.cursor()
            datos = (nom, cor, con) 
            qrInsert = "insert into TBRegistrados(Nombre, Correo, Contraseña) values(?,?,?)"
            
            #4. Ejecutar insert y cerramos conexion 
            cursor.execute(qrInsert, datos)
            conx.commit() #Cambio en la base de datos
            conx.close
            messagebox.showinfo("Listo", "Usuario guardado")
    
   