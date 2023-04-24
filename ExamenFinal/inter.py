from tkinter import *
from tkinter import messagebox
import tkinter as tk
from logica import *

logica = Conversiones()

def Interfaz():
    logica.NumRomanos(varR.get())


ventana = Tk()
ventana.title ("Convertidor")
ventana.geometry ("300x300")

etiqueta = Frame(ventana, bg = "pink")
etiqueta.pack(expand= True, fill = 'both')

varR = tk.StringVar()
Rom = tk.Label(etiqueta, text="Numero Romano:").pack()
Roman = tk.Entry(etiqueta, width=25, textvariable=varR).pack()

btnConversion = Button(etiqueta, text = "Convertir", bg = "gray", command= Interfaz).pack()

def Inter():
    logica.Arabigo(int(varA.get()))

varA = tk.StringVar()
Ara = tk.Label(etiqueta, text="Numero Arabigo:").pack()
Arab = tk.Entry(etiqueta, width=25, textvariable=varA).pack()

btnConversion = Button(etiqueta, text = "Convertir", bg = "gray", command= Inter).pack()


ventana.mainloop()