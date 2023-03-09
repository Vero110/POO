from tkinter import Tk 
import tkinter as tk 

axc = Login
ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.geometry("200x100")
label_usuario = tk.Label(ventana, text="Correo electrónico:")
label_usuario.pack()
entry_usuario = tk.Entry(ventana) 
entry_usuario.pack()

label_contraseña = tk.Label(ventana, text="Contraseña:")
label_contraseña.pack()
entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.pack()

def verificar():
    axc

boton_login = tk.Button(ventana, text="Iniciar sesión", command = validacion())
boton_login.pack()

label_resultado = tk.Label(ventana, text="")
label_resultado.pack()
ventana.mainloop()

        


