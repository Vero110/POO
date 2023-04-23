import tkinter as tk
from logica import Cuenta
from tkinter import messagebox
class VentanaPrincipal(tk.Tk):
    def __init__(self, cuenta):
        tk.Tk.__init__(self)
        self.title("Cuenta")
        self.geometry("400x200")

        self.cuenta = cuenta

        # Crear los labels para mostrar la información de la cuenta
        tk.Label(self, text="No. Cuenta:").grid(row=0, column=0)
        tk.Label(self, text=self.cuenta.num_cuenta).grid(row=0, column=1)
        tk.Label(self, text="Titular:").grid(row=1, column=0)
        tk.Label(self, text=self.cuenta.titular).grid(row=1, column=1)
        tk.Label(self, text="Edad:").grid(row=2, column=0)
        tk.Label(self, text=self.cuenta.edad).grid(row=2, column=1)
        tk.Label(self, text="Saldo:").grid(row=3, column=0)
        self.saldo_label = tk.Label(self, text=self.cuenta.saldo)
        self.saldo_label.grid(row=3, column=1)

        # Crear los botones para las operaciones con la cuenta
        tk.Button(self, text="Consultar saldo", command=self.consultar_saldo).grid(row=4, column=0)
        tk.Button(self, text="Ingresar efectivo", command=self.ingresar_efectivo).grid(row=4, column=1)
        tk.Button(self, text="Retirar efectivo", command=self.retirar_efectivo).grid(row=5, column=0)
        tk.Button(self, text="Depositar a otra cuenta", command=self.depositar_a_otra_cuenta).grid(row=5, column=1)

    def consultar_saldo(self):
        tk.messagebox.showinfo("Saldo", f"El saldo actual es {self.cuenta.saldo}")

    def ingresar_efectivo(self):
        cantidad = float(tk.simpledialog.askstring("Ingreso de efectivo", "Ingresa la cantidad a ingresar"))
        if cantidad is not None:
            self.cuenta.ingresar(cantidad)
            self.saldo_label.config(text=self.cuenta.saldo)

    def retirar_efectivo(self):
        cantidad = float(tk.simpledialog.askstring("Retiro de efectivo", "Ingresa la cantidad a retirar"))
        if cantidad is not None:
            try:
                self.cuenta.retirar(cantidad)
                self.saldo_label.config(text=self.cuenta.saldo)
            except ValueError as e:
                tk.messagebox.showerror("Error", str(e))

    def depositar_a_otra_cuenta(self):
        num_cuenta_destino = input("Número de cuenta destino: ")
        cantidad = float(input("Cantidad a depositar: "))
        cuenta_destino = Cuenta(num_cuenta_destino, "Titular destino", 25, 0)
        resultado = self.cuenta.depositar_otra_cuenta(cuenta_destino, cantidad)
        if resultado == "Saldo insuficiente":
            print(resultado)
        else:
            self.actualizar_saldo()

class VentanaRegistro(tk.Tk):
    def __init__(self, on_submit, ventana_principal):
        tk.Tk.__init__(self)
        self.title("Registro de cuenta en caja popular")
        self.geometry("400x300")

        self.label_titulo = tk.Label(self, text="Registro de nueva cuenta")
        self.label_titulo.pack()

        self.frame_num_cuenta = tk.Frame(self)
        self.label_num_cuenta = tk.Label(self.frame_num_cuenta, text="Número de cuenta:")
        self.label_num_cuenta.pack(side=tk.LEFT)
        self.entry_num_cuenta = tk.Entry(self.frame_num_cuenta)
        self.entry_num_cuenta.pack(side=tk.LEFT)
        self.frame_num_cuenta.pack()

        self.frame_titular = tk.Frame(self)
        self.label_titular = tk.Label(self.frame_titular, text="Titular:")
        self.label_titular.pack(side=tk.LEFT)
        self.entry_titular = tk.Entry(self.frame_titular)
        self.entry_titular.pack(side=tk.LEFT)
        self.frame_titular.pack()

        self.frame_edad = tk.Frame(self)
        self.label_edad = tk.Label(self.frame_edad, text="Edad:")
        self.label_edad.pack(side=tk.LEFT)
        self.entry_edad = tk.Entry(self.frame_edad)
        self.entry_edad.pack(side=tk.LEFT)
        self.frame_edad.pack()
    

        
