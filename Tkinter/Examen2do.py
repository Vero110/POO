import tkinter as tk

# Definir la función para generar la matrícula
def generar_matricula():
    #Obtener los valores ingresados por el usuario
    nombre = nombre_entry.get()
    letra_apellidoP = apellidoP_entry.get()
    letra_apellidoM = apellidoM_entry.get()
    fecha_nacimiento = fecha_nacimiento_entry.get()
    año_curso = año_entry.get()
    carrera = carrera_entry.get()
    
    # Generar la matrícula
    letra_nombre = nombre[0]
    letra_apellidoP = letra_apellidoP[+1:]
    letra_apellidoM = letra_apellidoM[+1:]
    año_nacimiento = fecha_nacimiento[-4:]
    digitos_nacimiento = año_nacimiento[-2:]
    año_curso = año_curso [-2:]
    letra_carrera = carrera[+3:]
    
    matricula = letra_nombre + letra_apellidoP + letra_apellidoM + digitos_nacimiento + año_curso + letra_carrera
    
    # Actualizar la etiqueta de la matrícula
    matricula_label.config(text="Matrícula generada: " + matricula)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Matrículas")

# Crear etiquetas y campos de entrada
nombre_label = tk.Label(ventana, text="Nombre:")
nombre_label.grid(row=0, column=0)
nombre_entry = tk.Entry(ventana)
nombre_entry.grid(row=0, column=1)

apellidoP_label = tk.Label(ventana, text="ApellidoP:")
apellidoP_label.grid(row=1, column=0)
apellidoP_entry = tk.Entry(ventana)
apellidoP_entry.grid(row=1, column=1)

apellidoM_label = tk.Label(ventana, text="ApellidoM:")
apellidoM_label.grid(row=2, column=0)
apellidoM_entry = tk.Entry(ventana)
apellidoM_entry.grid(row=2, column=1)

fecha_nacimiento_label = tk.Label(ventana, text="Fecha de Nacimiento (dd-mm-yyyy):")
fecha_nacimiento_label.grid(row=3, column=0)
fecha_nacimiento_entry = tk.Entry(ventana)
fecha_nacimiento_entry.grid(row=3, column=1)

carrera_label = tk.Label(ventana, text="Carrera:")
carrera_label.grid(row=4, column=0)
carrera_entry = tk.Entry(ventana)
carrera_entry.grid(row=4, column=1)

año_label = tk.Label(ventana, text="Año en curso:")
año_label.grid(row=5, column=0)
año_entry = tk.Entry(ventana)
año_entry.grid(row=5, column=1)

# Crear el botón para generar la matrícula
generar_matricula_button = tk.Button(ventana, text="Generar Matrícula", command=generar_matricula)
generar_matricula_button.grid(row=6, column=0)

# Crear la etiqueta para mostrar la matrícula
matricula_label = tk.Label(ventana, text="")
matricula_label.grid(row=6, column=0, padx=10, pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
