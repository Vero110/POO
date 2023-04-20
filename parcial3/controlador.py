from tkinter import messagebox
import sqlite3
import tkinter
from typing import Self
import bcrypt
from ventana import * 

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
    
   
def ingresar_Cuenta (self): 
    varNoC = self.varNoC.get()
    saldo = self.VarSaldo.get()
    
def consultarUsuarios(self):
    # 1. usamos conexion 
        conx = self.conexionBD()
        cursor = conx.cursor()

        consultaQry = "SELECT * FROM TBCuentas"
        cursor.execute(consultaQry)
        rsConsulta = cursor.fetchall()

    # cerrar Conexion
        conx.close()

        return rsConsulta

       