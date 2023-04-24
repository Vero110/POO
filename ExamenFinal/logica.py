from tkinter import *
from tkinter import messagebox
import tkinter as tk
from logica import *

class Conversiones:
    arabigos = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50}

    def NumRomanos(self, numeroRomano):
        romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        op = 0
        for i in range(0, len(numeroRomano)):
            if (i == 0 or romanos[numeroRomano[i]] <= romanos[numeroRomano[i - 1]]):
                op += romanos[numeroRomano[i]]
            else:
                op += romanos[numeroRomano[i]] - 2 * romanos[numeroRomano[i - 1]]
        messagebox.showinfo("Nuestro numero Romano a Arabigo es:", op)
        

    def Arabigo(self, numeroArabigo):
        if (numeroArabigo == ""):
            messagebox.showerror ( "Ingrese un número")
        else:
            m = ["", "M", "MM", "MMM"]
            c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
            x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
            i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
  
            miles = m[numeroArabigo // 1000]
            centenas = c[(numeroArabigo % 1000) // 100]
            decimas = x[(numeroArabigo % 100) // 10]
            unidades = i[numeroArabigo % 10]
  
            numero = (miles + centenas + decimas + unidades)
            
            if (numeroArabigo <= 50):
                messagebox.showinfo("El número es: " + numero)
            else:
                messagebox.showerror( "Ingrese un número menor a 50")
        
