from logging import root
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from controlador import controlador 

controlador = controlador ()

      
      
      
      
      
def cargarUsuarios():
    # 1. Obtener los datos de la tabla
    usuarios = controlador.consultarUsuarios()
    #Vista de arbol
    VCUENTA = ttk.Treeview(pestaña2, columns=("ID cuenta", "Actualizar", "Saldo"), show='headings')
  
    for usuario in usuarios:
        VCUENTA.insert("", END, values=(usuario[1], usuario[2], usuario[3]))

    VCUENTA.pack(fill=BOTH, expand=True)
    
    
    
    
    
ventana = Tk()
ventana.title("Base de datos del banco")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)


# Ingresar dinero 
Label= tk.Label( text='Numero de cuenta ', fg='blue', font=('Modern', 18))
Label.grid (row=0, column=0)

varNoC = tk.Entry()
varNoC.grid (row = 0, column = 1)

Label= tk.Label( text='Saldo', fg='blue', font=('Modern', 18))
Label.grid  (row=1, column=0)

VarSaldo = tk.Entry()
VarSaldo.grid (row = 1, column =1)

Label= tk.Button(pestaña1, text='Ingresar', command= ingresar_Cuenta)
Label.grid  (row=2, column=0)

Label= tk.Button(pestaña1, text='Actualizar', command= actualizar_Cuenta)
Label.grid  (row=2, column=1)

Label= tk.Button(pestaña1, text='Mostrar todas', command= mostrar)
Label.grid  (row=2, column=2)





ventana.mainloop()