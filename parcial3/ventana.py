from logging import root
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from controlador import controlador 

controlador = controlador ()

def ejecutaInsert():
    controlador.ingresar(varIDC.get(),varNoC.get(),varSaldo.get())







      
ventana = Tk()
ventana.title("Base de datos del banco")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestaña1 = ttk.Frame(panel)

# Ingresar dinero 
Label(pestaña1, text='Ingresar dinero', fg='blue', font=('Modern', 18)).pack()

varIDC = StringVar()
Label(pestaña1, text="ID cuenta ").pack()
Entry(pestaña1, textvariable=varIDC).pack()

varNoC = StringVar()
Label(pestaña1, text="Número de cuenta ").pack()
Entry(pestaña1, textvariable=varNoC).pack()

varSaldo = StringVar()
Label(pestaña1, text="Saldo ").pack()
Entry(pestaña1, textvariable=varSaldo).pack()

varIn = StringVar()
Label(pestaña1, text="Saldo a ingresar ").pack()
Entry(pestaña1, textvariable=varIn).pack()



btnGuardar = Button(pestaña1, text="", command=ejecutaInsert)
btnGuardar.pack()

ventana.mainloop()