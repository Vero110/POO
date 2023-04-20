from tkinter import messagebox
import sqlite3
import tkinter
from typing import Self
import bcrypt

class controlador: 
    def _init_(self):
        pass

    # Metodo para crear conexiones
    def conexionBD(self):

        try:
            conexion = sqlite3.connect("C:/Users/52442/Documents/GitHub/POO/parcial3/BD_Banco.db")
            print("Conectado a la Base de Datos")
            return conexion
        except sqlite3.OperationalError:
            print("No se puede conectar")
    
    def ingresar(self,varCoN, varIDC, varSaldo):

        # usamos una conexion
        conx = self.conexionBD()

        if(varCoN=="" or varIDC=="" or varSaldo ==""):
            messagebox.showwarning("Formulario Incompleto")
        else:
            cursor = conx.cursor()
            qrInsert = "insert into TBCuentas(

       