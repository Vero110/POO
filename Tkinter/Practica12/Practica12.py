from Pract12 import *
from tkinter import * 
import tkinter as tk

axc = Usuario()

def ejecutaVal ():
    axc.validacion(var1.get(), var2.get())
    

ventana = Tk()
ventana.title("Práctica 12")
ventana.geometry("600x400")

seccion1 = Frame(ventana)
seccion1.pack(expand =True, fill ='both')

titulo = Label (seccion1, text =" Login ", bg = "black", fg = "white", font = ("Modern", 18)).pack()

var1 = tk.StringVar()
lblcorreo = Label (seccion1, text = "correo:").pack()
txtcorreo = Entry(seccion1, textvariable = var1, takefocus=True).pack()

var2 = tk.StringVar()
lblcorreo = Label (seccion1, text = "contraseña:").pack()
txtcorreo = Entry(seccion1, textvariable = var2, show="*").pack()

btnAcceso = Button(seccion1, text = "Acceder", bg="green", command=ejecutaVal)
btnAcceso.pack()

ventana.mainloop()