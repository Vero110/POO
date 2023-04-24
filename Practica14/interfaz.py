from tkinter import *
from tkinter import messagebox
import random
from logica import *
            
class Formulario(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Caja Popular")
        self.geometry("300x300")
        self.caja = Caja()
        self.config(bg="gray")
        self.numero = StringVar()
        self.monto = StringVar()
        self.numero2 = StringVar()
        
        Label(self, text="No. Cuenta: ").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        Entry(self, textvariable=self.numero).grid(row=0, column=1, padx=5, pady=5)
        
        Label(self, text="Monto: ").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        Entry(self, textvariable=self.monto).grid(row=1, column=1, padx=5, pady=5)
        
        Label(self, text="No. Cuenta 2: ").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        Entry(self, textvariable=self.numero2).grid(row=2, column=1, padx=5, pady=5)
        
        Button(self, text="Consultar Saldo", command=self.consultar_saldo).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        Button(self, text="Ingresar Efectivo", command=self.ingresar_efectivo).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        Button(self, text="Retirar Efectivo", command=self.retirar_efectivo).grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        
        Button(self, text="Depositar a otra cuenta", command=self.depositar_a_otra_cuenta).grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        Button(self, text="Nueva Cuenta", command=self.nueva_cuenta).grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        
    def consultar_saldo(self):
        if self.numero.get() == "":
            messagebox.showerror("Error", "Debe llenar el campo No. Cuenta")
        else:
            saldo = self.caja.consultar_saldo(int(self.numero.get()))
            if saldo is None:
                messagebox.showerror("Error", "No existe la cuenta")
            else:
                messagebox.showinfo("Información", "El saldo de la cuenta es: {}".format(saldo))
            
    def ingresar_efectivo(self):
        if self.numero.get() == "" or self.monto.get() == "":
            messagebox.showerror("Error", "Debe llenar todos los campos")
        else:
            if self.caja.ingresar_efectivo(int(self.numero.get()), float(self.monto.get())):
                messagebox.showinfo("Información", "Efectivo ingresado con éxito")
            else:
                messagebox.showerror("Error", "No existe la cuenta")
                
    def retirar_efectivo(self):

        if self.numero.get() == "" or self.monto.get() == "":
            messagebox.showerror("Error", "Debe llenar todos los campos")
        else:
            if self.caja.retirar_efectivo(int(self.numero.get()), float(self.monto.get())):
                messagebox.showinfo("Información", "Efectivo retirado con éxito")
            else:
                messagebox.showerror("Error", "No existe la cuenta")
                
    def depositar_a_otra_cuenta(self):

        if self.numero.get() == "" or self.monto.get() == "" or self.numero2.get() == "":
            messagebox.showerror("Error", "Debe llenar todos los campos")
        else:
            if self.caja.depositar_a_otra_cuenta(int(self.numero.get()), float(self.monto.get()), int(self.numero2.get())):
                messagebox.showinfo("Información", "Efectivo depositado con éxito")
            else:
                messagebox.showerror("Error", "No existe la cuenta")
    
    def nueva_cuenta(self):
        NuevaCuenta(self)
    
    def ver_todas(self):
        cuentas = [str(cuenta) for cuenta in self.caja.cuentas]
        if len(cuentas) == 0:
            messagebox.showinfo("Información", "No hay cuentas registradas")
        else:
            messagebox.showinfo("Cuentas", "\n".join(cuentas))

app = Formulario()
app.mainloop()
