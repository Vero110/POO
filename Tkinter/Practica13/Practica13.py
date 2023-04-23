from tkinter import *
from tkinter import messagebox
from Pract13 import GeneraContraseña, CopyContraseña


class gen:
    def _init_(self, master):
        self.master = master
        self.master.title("Generador de contraseñas")
        self.master.resizable(0,0)
        self.master.iconbitmap("icon.ico")
        
        self.generador = GeneraContraseña(self.master)
        Button(self.generador.frame, text="Copiar", command=self.copiar).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        Button(self.generador.frame, text="Salir", command=self.salir).grid(row=3, column=1, sticky="w", padx=5, pady=5)
    
    def copiar(self):
        password = self.generador.contrasena.get()
        CopyContraseña(Toplevel(self.master), password)
    
    def salir(self):
        valor = messagebox.askquestion("Salir", " ")
        if valor == "yes":
            self.master.destroy()
    
if __name__ == "_main_": 
    root = Tk()
    app = gen(root)
    root.mainloop() 

            

        
        