import tkinter as tk

def validar_login():
    correo = entry_correo.get()
    contrasena = entry_contrasena.get()
    
    if correo == 'upq.com' and contrasena == 'upq123':
        label_resultado.config(text="¡Bienvenido!")
    else:
        label_resultado.config(text="Por favor, revise sus datos")

# Crear la ventana de inicio de sesión
ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.geometry("200x100")


# Crear los campos de entrada para correo y contraseña
label_correo = tk.Label(ventana, text="Correo electrónico:", bg = "#ccccff")
label_correo.pack()
entry_correo = tk.Entry(ventana, bg="pink")
entry_correo.pack()

label_contrasena = tk.Label(ventana, text="Contraseña:", bg = "blue")
label_contrasena.pack()
entry_contrasena = tk.Entry(ventana, show="*", bg = "yellow")
entry_contrasena.pack()

# Crear el botón de inicio de sesión
boton_login = tk.Button(ventana, text="Iniciar sesión", command=validar_login)
boton_login.pack()

# Crear la etiqueta para mostrar el resultado de la validación
label_resultado = tk.Label(ventana, text="", bg = "green")
label_resultado.pack()

# Iniciar la ventana
ventana.mainloop()