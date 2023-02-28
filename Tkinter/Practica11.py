from tkinter import Tk, Frame, Button 

#1. Crear ventana. Instanciamos un objeto Ventana
ventana = Tk() 
ventana.title("Practica 11:3 Frames")
ventana.geometry("600x400")

#2. Definir secciones de la ventana
seccion1 = Frame(ventana, bg = "#ccccff")
seccion1.pack(expand=True, fill = 'both')

seccion2 = Frame(ventana, bg = "pink") 
seccion2.pack(expand=True, fill = 'both')

seccion3 = Frame (ventana, bg = "gray")
seccion3.pack(expand=True, fill = 'both')

#3. Botones
botonAzul = Button(seccion1, text = "boton azul", fg = "red") 
botonAzul.place(x = 60, y = 60)

botonMorado = Button(seccion2, text = "boton morado", fg = "#0099ff") 
botonMorado.grid(row = 0, column = 0 )

botonNegro = Button(seccion2, text = "boton negro", fg = "black", bg = "#239023") 
botonNegro.grid(row = 1, column = 0)

botonRosa = Button(seccion3, text = "boton rosa", fg = "#00e600")
botonRosa.pack()

#Main de ejecucion de la ventana 
ventana.mainloop()
