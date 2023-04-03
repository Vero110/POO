from tkinter import *
from tkinter import ttk
from controladorBD import controladorBD
import tkinter as tk
from tkinter import messagebox

# Creamos un objeto de la clase controladorBD
controlador = controladorBD()

# Función para disparar el botón
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())
# Funcion para disparar el botón de busquedad
def ejecutaSelectU():
    usuario  = controlador.consultarUsuario(varBus.get())
    
    for usu in usuario:
        cadena = str (usu[0]) + " " + usu [1] + " " + usu[2] + " " + str(usu[3])
    if (usuario):
    #print (cadena)
        textEnc.insert("0.0", cadena)      
    else:
        
        messagebox.showinfo("Usuario no encontrado","Ya no existe")
        
def ejecutaConsultaU():
    usuarios = controlador.consultaUsuarios()
    
    #Vista de arbol
    VUsuarios = ttk.Treeview(pestaña3, columns= ("Nombre", "Correo", "Contraseña"), show='headings')
    VUsuarios.column("Nombre", width=50, minwidth=50, anchor=CENTER)
    VUsuarios.column("Contraseña", width=50, minwidth=50, anchor=CENTER)
    
    VUsuarios.heading("Nombre", text="Nombre")    
    VUsuarios.heading("Correo", text="Correo")    
    VUsuarios.heading("Contraseña", text="Contraseña")   
    
    for usu in usuarios: 
        VUsuarios.insert("", END, values = (usu[1], usu[2], usu[3]))
        
    VUsuarios.pack(fill = BOTH, expand=True)

        
ventana = Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
pestaña4 = ttk.Frame(panel)

# Pestaña1: Formulario de usuarios
Label(pestaña1, text='Registro de usuarios', fg='blue', font=('Modern', 18)).pack()
varNom = StringVar()
Label(pestaña1, text="Nombre: ").pack()
Entry(pestaña1, textvariable=varNom).pack()
varCor = StringVar()
Label(pestaña1, text="Correo: ").pack()
Entry(pestaña1, textvariable=varCor).pack()
varCon = StringVar()
Label(pestaña1, text="Contraseña: ").pack()
Entry(pestaña1, textvariable=varCon).pack()
btnGuardar = Button(pestaña1, text="Guardar Usuario", command=ejecutaInsert)
btnGuardar.pack()


#Pestaña2: Buscar usuario 
titulo2 = Label(pestaña2, text = "Buscar Usuario", fg = 'green', font = ("Modern", 18)).pack()

varBus = tk.StringVar()
lblid = Label (pestaña2, text = " Identificador Usuario:").pack()
txtid =Entry (pestaña2, textvariable = varBus).pack()
btnBus= Button(pestaña2, text = "Buscar", command= ejecutaSelectU).pack()

subBus = Label (pestaña2, text = "Encontrado: ", fg = 'blue', font = ("Modern", 18)).pack()
textEnc = tk.Text(pestaña2, height = 2, width = 52)
textEnc.pack()

#Pestaña3: Consultar usuario 
titulo3 = Label(pestaña3, text = "Consultar Usuarios", fg = 'green', font = ("Modern", 18)).pack()

btnCons = Button(pestaña3, text="Mostrar todos los usuarios: ", command=ejecutaConsultaU).pack()

panel.add(pestaña1, text='Formulario de usuarios')
panel.add(pestaña2, text='Buscar usuario')
panel.add(pestaña3, text='Consultar usuarios')
panel.add(pestaña4, text='Actualizar usuario')

ventana.mainloop()