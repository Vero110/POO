from tkinter import *
from Pract13 import generadorContraseña
import tkinter as tk
import random


class PasswordGeneratorApp:
    def _init_(self):
        self._generator = generadorContraseña()
        self._root = tk.Tk()
        self._root.title("Generador de Contraseña")

        self._length_label = tk.Label(self._root, text="Cantidad de carcateres:")
        self._length_label.grid(row=0, column=0, padx=10, pady=10)

        self._length_var = tk.StringVar()
        self._length_var.set("8")
        self._length_entry = tk.Entry(self._root, textvariable=self._length_var)
        self._length_entry.grid(row=0, column=1)

        self._include_uppercase_var = tk.BooleanVar()
        self._include_uppercase_var.set(True)
        self._include_uppercase_checkbox = tk.Checkbutton(
            self._root,
            text="Include Uppercase",
            variable=self._include_uppercase_var
        )
        self._include_uppercase_checkbox.grid(row=1, column=0)

        self._include_special_characters_var = tk.BooleanVar()
        self._include_special_characters_var.set(True)
        self._include_special_characters_checkbox = tk.Checkbutton(
            self._root,
            text="Include Special Characters",
            variable=self._include_special_characters_var
        )
        self._include_special_characters_checkbox.grid(row=2, column=0)

        self._generate_button = tk.Button(self._root, text="Generando contraseña", command=self.generate_password)
        self._generate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self._password_label = tk.Label(self._root, text="Contraseña: ")
        self._password_label.grid(row=4, column=0, padx=10, pady=10)

        self._password_textbox = tk.Text(self._root, height=1)
        self._password_textbox.grid(row=4, column=1)

        self._root.mainloop()

    def generate_password(self):
        self._generator.set_length(int(self._length_var.get()))
        self._generator.include_uppercase(self._include_uppercase_var.get())
        self._generator.include_special_characters(
            self._include_special_characters_var.get()
        )
        password = self._generator.generate_password()
        self._password_textbox.delete(1.0, tk.END)
        self._password_textbox.insert(tk.END, password)
        tk.messagebox.showinfo("Contraseña generada", password)

if __name__ == "_main_":
    app = PasswordGeneratorApp()

            

        
        