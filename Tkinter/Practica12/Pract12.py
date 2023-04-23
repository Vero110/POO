from tkinter import messagebox

class Usuario:
    def __init__(self):
        self.__email = "example@gmail.com"
        self.__password = "12345"

    def validacion(self, correo, contra):
        if (correo ==  "" and contra == ""):
            messagebox.showwarning = ("No hay datos")
            
        else:
            if (self.__email == correo and self.__password == contra):
                messagebox.showinfo ("Exito", "Los datos han sido ingresados correctamente")
            else: 
                messagebox.showerror("Advertencia","Los datos no coinciden")
            
