from tkinter import messagebox
import random
        
minus = "abcdefghijklmnñopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
base = minus + mayus + numeros 
long = int ( input ("ingrese la longitud deseada: "))

class Logica: 
    
    def _init_(base, long):
        if long == 8: 
            for _ in range (1):
                muestra = random.sample (base, long)
                password = "".join(muestra)
                print (password)
                
        