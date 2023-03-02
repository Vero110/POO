from tkinter import Tk, Frame, Button, messagebox

#4. Funcion de mensajes para el botón
def mostrarMensaje():
    messagebox.showinfo("Aviso","Este mensaje es para avisar algo")
    messagebox.showerror("Es un mensaje de error:","todo fallo con exito")
    print (messagebox.askquestion("Pregunta:", "El jugó con tu corazón?"))
    print (messagebox.askokcancel("Pregunta:", "El jugó con tu corazón?"))
    print (messagebox.askretrycancel("Pregunta:", "El jugó con tu corazón?"))
    print (messagebox.askyesnocancel("Pregunta:", "El jugó con tu corazón?"))
    print (messagebox.askyesno("Pregunta:", "El jugó con tu corazón?"))

#5. Funcion para agregar botones
def agregarBoton():
    botonRosa.config(text="+", bg = "white", fg = "pink")
    botonNuevo = Button(seccion3, text ="Boton nuevo")
    botonNuevo.pack()

    

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
botonAzul = Button(seccion1, text = "boton azul", fg = "red", command = mostrarMensaje) 
botonAzul.place(x = 60, y = 60)

botonMorado = Button(seccion2, text = "boton morado", fg = "#0099ff") 
botonMorado.grid(row = 0, column = 0 )

botonNegro = Button(seccion2, text = "boton negro", fg = "black", bg = "#239023") 
botonNegro.grid(row = 1, column = 0)

botonRosa = Button(seccion3, text = "boton rosa", fg = "#00e600", command = agregarBoton)
botonRosa.pack()



#Main de ejecucion de la ventana 
ventana.mainloop()
