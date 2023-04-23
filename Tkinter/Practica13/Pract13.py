from tkinter import *
from tkinter import messagebox
import random


class GeneraContraseña:
    def _init_(self, parent):
        self.parent = parent
        

        self.mayus = IntVar()
        self.esp = IntVar()
        self.contrasena = StringVar()
        self.long = StringVar(value="8")
        

        self.frame = Frame(parent)
        self.frame.pack()

        Label(self.frame, text="Longitud que desee : ").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        Spinbox(self.frame, from_=1, to=50, increment=1, textvariable=self.long).grid(row=0, column=1, padx=5, pady=5)
        Checkbutton(self.frame, text="Mayúsculas", variable=self.mayus).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        Checkbutton(self.frame, text="Caracteres especiales", variable=self.esp).grid(row=1, column=1, sticky="w", padx=5, pady=5)
        Button(self.frame, text="Generar", command=self.generar).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        Entry(self.frame, justify="center", textvariable=self.contrasena).grid(row=2, column=1, padx=5, pady=5)
        
    def generar(self):
        longitud = int(self.long.get())
        caracteres = "abcdefghijklmnopqrstuvwxyz"
        if self.mayus.get():
            caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.esp.get():
            caracteres += "!@#$%^&*()_+-={}|[]\\:\";'<>?,./"
        password = ""
        for i in range(longitud):
            password += random.choice(caracteres)
        self.contrasena.set(password)
    
class CopyContraseña:
    def _init_(self, parent, password):
        self.parent = parent
        self.password = password


        self.frame = Frame(parent)
        self.frame.pack()

        if password == "":
            messagebox.showerror("Error", "No hay nada que copiar")
            self.parent.destroy()
        else:
            parent.clipboard_clear()
            parent.clipboard_append(password)
            messagebox.showinfo("Copiado", "La contraseña ha sido guardada")
            self.parent.destroy()
            

    