import tkinter as tk
from interfaz import VentanaRegistro, VentanaPrincipal
from logica import Cuenta

def on_submit(num_cuenta, titular, edad, saldo):
    cuenta = Cuenta(num_cuenta, titular, edad, saldo)
    ventana_principal = VentanaPrincipal(cuenta)
    ventana_principal.mainloop()

ventana_registro = VentanaRegistro(on_submit, None)
ventana_registro.mainloop()
