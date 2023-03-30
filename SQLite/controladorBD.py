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
            conH = self.encriptarCon(con) #la contraseña encriptada guardamela en conH
            datos = (nom, cor, conH) 
            qrInsert = "insert into TBRegistrados(Nombre, Correo, Contraseña) values(?,?,?)"
            
            #4. Ejecutar insert y cerramos conexion 
            cursor.execute(qrInsert, datos)
            conx.commit() #Cambio en la base de datos
            conx.close
            messagebox.showinfo("Listo", "Usuario guardado")
    
       #Metodo para encriptar contraseñas
    def encriptarCon(self, con): 
        conPlana = con 
        conPlana = conPlana.encode() #convertimos con a bytes
        sal = bcrypt.gensalt() #algoritmo de aleatoridad
        conHa = bcrypt.hashpw(conPlana, sal) #crea la contraseña encriptada
        print (conHa)
        #enviamos la contraseña encryptada
        return conHa      
    
        #Metodo para buscar 1 usuario 
    def consultarUsuario(self, id):
        #1. Preparar una conexion 
        conx = self.conexionBD()
        #2. verificar si id contiene aldo 
        if (id == ""): 
            messagebox.showwarning("Cuidado", "Id vacio, escribe algo valido")
            conx.close()
        else:
            try:
                #3. preparar lo necesario (CURSOR Y EL QUERY)
                cursor=conx.cursor()
                selectQry = "select * from TBRegistrados where id = " + id
                
                #4. ejecutar y guardar la consulta
                cursor.execute(selectQry)
                rsUsuario = cursor.fetchall()
                conx.close()
                
                return rsUsuario
            
            except sqlite3.OperationalError:
                print("Error de consulta")
            
        