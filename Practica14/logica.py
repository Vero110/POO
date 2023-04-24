from tkinter import *
from tkinter import messagebox
import random

class Cuenta:
    def __init__(self, numero, titular, edad, saldo):
        self.numero = numero
        self.titular = titular
        self.edad = edad
        self.saldo = saldo
        
    def __str__(self):
        return "No. Cuenta: {}, Titular: {}, Edad: {}, Saldo: {}".format(
            self.numero, self.titular, self.edad, self.saldo)
    
    def __repr__(self):
        return "Cuenta({}, {}, {}, {})".format(
            self.numero, self.titular, self.edad, self.saldo)
    
    def __eq__(self, other):
        if isinstance(other, Cuenta):
            return self.numero == other.numero
        else:
            return False
        
    def __ne__(self, other):
        return not self.__eq__(other)

class Caja:
    def __init__(self):
        self.cuentas = []
        
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        
    def consultar_saldo(self, numero):
        for cuenta in self.cuentas:
            if cuenta.numero == numero:
                return cuenta.saldo
        return None
        
    def ingresar_efectivo(self, numero, monto):
        for cuenta in self.cuentas:
            if cuenta.numero == numero:
                cuenta.saldo += monto
                return True
        return False
        
    def retirar_efectivo(self, numero, monto):
        for cuenta in self.cuentas:
            if cuenta.numero == numero:
                if cuenta.saldo >= monto:
                    cuenta.saldo -= monto
                    return True
                else:
                    return False
        return False
        
    def depositar_a_otra_cuenta(self, numero, monto, numero2):
        for cuenta in self.cuentas:
            if cuenta.numero == numero:
                if cuenta.saldo >= monto:
                    cuenta.saldo -= monto
                    for cuenta2 in self.cuentas:
                        if cuenta2.numero == numero2:
                            cuenta2.saldo += monto
                            return True
                else:
                    return False
        return False

class NuevaCuenta(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.title("Nueva Cuenta")
        self.grab_set()
        self.config(bg="#ffccff")
        self.numero = random.randint(1000, 9999)
        self.titular = StringVar()
        self.edad = StringVar()
        
        Label(self, text="No. Cuenta: {}".format(self.numero)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        Label(self, text="Titular: ").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        
        Entry(self, textvariable=self.titular).grid(row=1, column=1, padx=5, pady=5)
        Label(self, text="Edad: ").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        
        Entry(self, textvariable=self.edad).grid(row=2, column=1, padx=5, pady=5)

        Button(self, text="Crear", command=self.crear).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
    def crear(self):
        if self.titular.get() == "" or self.edad.get() == "":
            messagebox.showerror(" ", "Debe llenar todos los campos")
        else:
            self.parent.caja.agregar_cuenta(Cuenta(self.numero, self.titular.get(), int(self.edad.get()), 0))
            messagebox.showinfo(" ", "Cuenta creada con éxito")
            self.destroy()
