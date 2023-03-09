from Practica12 import * 
from tkinter import messagebox

class Logica():
    def __init__(self):
        pass
    
    def user(self, user, contraseña):
        user = "upq"
        contraseña = "upq123"
    
    def validacion(seft, usuario, contraseña):
        usuario = usuario.get()
        contraseña = contraseña.get()
        
        # Aquí iría la validación del usuario y contraseña
        if usuario == 'upq.com' and contraseña == 'upq123':
            messagebox.info("¡Bienvenido!")
        else:
            messagebox.ERROR("Por favor, revise sus datos")


        