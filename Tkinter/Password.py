from tkinter import * 
import tkinter as tk
from Logica import * 

axc = Logica()

def ejecutaVal():
    axc.validarContraseña(var1.get())

ventana = Tk()
ventana.title("password")
ventana.geometry("300x150")

seccion1 = Frame(ventana)
seccion1.pack(expand=True, fill='both')
titulo = Label (seccion1, text = "Generador de contraseñas", bg = "black", fg = "white",)

var1 = tk.StringVar()
labelContraseña = Label(seccion1, text = "contraseña: ").pack()
txtContraseña = Entry (seccion1, textvariable = var1, takefocus=True, command = ejecutaVal)
botonAcesso = Button (seccion1, text = "", bg = "green")
botonAcesso.pack()

ventana.mainloop()
