from tkinter import messagebox
import sqlite3
import tkinter
from typing import Self
import bcrypt

class controladorBD:

    def _init_(self):
        pass

    # Metodo para crear conexiones
    def conexionBD(self):

        try:
            conexion = sqlite3.connect("C:/Users/52442/Documents/GitHub/POO/SQLite/DBUsuarios.db")
            print("Conectado a la Base de Datos")
            return conexion
        except sqlite3.OperationalError:
            print("No se puede conectar")

    #Metodo para guardar usuarios
    def guardarUsuario(self,nom,cor,con):

        # usamos una conexion
        conx = self.conexionBD()

        # validar parametros que esten vacios
        if(nom=="" or cor=="" or con ==""):
            messagebox.showwarning("Formulario Incompleto")
        else:
        #preparamos el cursor Y EL QUERY
            cursor = conx.cursor()
            conH = self.encriptarCon(con)
            datos = (nom,cor,conH)
            qrInsert = "insert into TBRegistrados(nombre,correo,contraseña) values(?,?,?)"

        #ejecutar Insert y cerramos conexion
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Exito","Usuario Guardado")

    def encriptarCon(self,con):
        conPlana = con
        conPlana = conPlana.encode() #convertimos con a bytes
        sal = bcrypt.gensalt()
        conHa = bcrypt.hashpw(conPlana,sal)
        print(conHa)

        return conHa

     # Metodo para buscar un usuario
    def consultarUsuario(self,id):
        #1. Preparar una conexion
        conx = self.conexionBD()

        if(id == ""):
            messagebox.showwarning("Advertencia","El ID esta vacío")
            conx.close()
        else:
            try:
    
                cursor = conx.cursor()
                selecQuery = "select * from TBRegistrados where id="+id

                cursor.execute(selecQuery)
                rsUsuario = cursor.fetchall()
                conx.close()

                return rsUsuario

            except sqlite3.OperationalError:
                print("Error de consulta")


    def consultarUsuarios(self):
    # 1. usamos conexion 
        conx = self.conexionBD()
        cursor = conx.cursor()

        consultaQry = "SELECT * FROM TBRegistrados"
        cursor.execute(consultaQry)
        rsConsulta = cursor.fetchall()

    # cerrar Conexion
        conx.close()

        return rsConsulta

        # Método para actualizar un usuario
    def actualizarUsuario(self, id, nom, cor, con):
        # 1. Preparar una conexión
        conx = self.conexionBD()

        # 2. Verificar si el ID está vacío
        if(id == ""):
            messagebox.showwarning(" ","El ID esta vacio")
            conx.close()
        else:
            try:
                # 3. Preparar cursor y query
                cursor = conx.cursor()

                # 4. Encriptar la contraseña si es necesario
                if con != "":
                    con = self.encriptarCon(con)

                # 5. Actualizar los datos del usuario
                actualizaQry = f"UPDATE TBRegistrados SET nombre=?, correo=?, contraseña=? WHERE id={id}"
                Obj = (nom, cor, con)
                cursor.execute(actualizaQry, Obj)

                # 6. Guardar los cambios y cerrar la conexión
                conx.commit()
                conx.close()

                messagebox.showinfo(" ", "El usuario se ha actualizado")
            except sqlite3.OperationalError:
                print("No se puede actualizar el usuario")

    def eliminarUsuario(self, id):
            # 1. Preparar una conexión
            cons = self.conexionBD()

            # 2. Verificar si el ID está vacío
            if(id == ""):
                messagebox.showwarning(" ","No podemos seguir porque el ID esta vacio")
                cons.close()
            else:
                try:
                    # 3. Preparar cursor y query
                    cursor = cons.cursor()

                    # 4. Eliminar el usuario
                    delQuery = f"DELETE FROM TBRegistrados WHERE id={id}"
                    cursor.execute(delQuery)

                    # 5. Guardar los cambios y cerrar la conexión
                    cons.commit()
                    cons.close()

                    messagebox.showinfo("" , "El usuario ha sido eliminado exitosamente")
                except sqlite3.OperationalError:
                    print("No se puede eliminar el usuario")