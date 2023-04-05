from logging import root
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from controladorBD import controladorBD

# Creamos un objeto de la clase controladorBD
controlador = controladorBD()

# Función para disparar el botón
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())

# Función para disparar el boton de busqueda
def ejecutaSelectU():
   usuario = controlador.consultarUsuario(varBus.get())
   for usu in usuario:
    
    cadena = str(usu[0])+ " " + usu[1]+ " " + usu[2]+ " " + str(usu[3])

   if(usuario):
       textEnc.insert("0.0",cadena)
   else:
       messagebox.showinfo("Usuario no encontrado","Ya no existe")


def cargarUsuarios():
    # 1. Obtener los datos de la tabla
    usuarios = controlador.consultarUsuarios()
    #Vista de arbol
    VUsuarios = ttk.Treeview(pestaña3, columns=("nombre", "correo", "contraseña"), show='headings')
    VUsuarios.column("nombre", width=50, minwidth=50, anchor=CENTER)
    VUsuarios.column("correo", width=50, minwidth=50, anchor=CENTER)
    VUsuarios.column("contraseña", width=50, minwidth=50, anchor=CENTER)

    VUsuarios.heading("nombre", text="Nombre")
    VUsuarios.heading("correo", text="Correo")
    VUsuarios.heading("contraseña", text="Contraseña")

    for usuario in usuarios:
        VUsuarios.insert("", END, values=(usuario[1], usuario[2], usuario[3]))

    VUsuarios.pack(fill=BOTH, expand=True)

def ejecutaActualizar():
    idUsu = varIDa.get()
    nomUsu = varNomac.get()
    corrUsu = varCorac.get()
    contUsu = varConta.get()
    menConf = messagebox.askyesno(" ", "Desea actualizar los datos?")
    if menConf:
        controlador.actualizarUsuario(idUsu, nomUsu, corrUsu, contUsu)
    else:
        messagebox.showinfo("Error", "Los datos no se han actualizado")

def ejecutaEliminar():
    IDUsuario = varIDe.get()
    menConf = messagebox.askyesno(" ", "Desea eliminar los datos?")
    if menConf:
        controlador.eliminarUsuario(IDUsuario)
    else:
        messagebox.showinfo(" ", "Los datos no han sido eliminados")
        
ventana = Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
pestaña4 = ttk.Frame(panel)
pestaña5 = ttk.Frame(panel)

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
Entry(pestaña1, textvariable=varCon, show="*").pack()

btnGuardar = Button(pestaña1, text="Guardar Usuario", command=ejecutaInsert)
btnGuardar.pack()

#Pestaña 2: Buscar Usuarios

titulo2 = Label(pestaña2,text="Buscar Usuario", fg='green', font=("Modern",18)).pack()

varBus = tk.StringVar()
lblid = Label(pestaña2,text= "Identificador de usuarios: ").pack()
txtid = Entry(pestaña2,textvariable=varBus).pack()
btnBus = Button(pestaña2, text="Buscar",command=ejecutaSelectU).pack()

subBus = Label(pestaña2,text="Encontrado: ", fg='green', font=("Modern",15)).pack()
textEnc = tk.Text(pestaña2,height=5,width=52)
textEnc.pack()

#Pestaña 3: Consultar usuarios

titulo3 = Label(pestaña3, text="Consultar Usuarios", fg='green', font=("Modern", 18)).pack()
btnCargarUsuarios = Button(pestaña3, text="Mostrar todos los usuarios:", command=cargarUsuarios).pack()

#Pestaña 4: Actualizar Usuario

titulo4 = Label(pestaña4,text="Actualizar usuario", fg='green', font=("Modern",18)).pack()

titulo5 = Label(pestaña4,text="ID del usuario a actualizar", fg='green', font=("Modern",10)).pack()
varIDa = StringVar()
Label(pestaña4, text="ID  ").pack()
Entry(pestaña4, textvariable=varIDa).pack()

titulo6 = Label(pestaña4,text="Datos del usuario a actualizar", fg='green', font=("Modern",10)).pack()
varNomac = StringVar()
Label(pestaña4, text="Nombre").pack()
Entry(pestaña4, textvariable=varNomac).pack()

varCorac = StringVar()
Label(pestaña4, text="Correo").pack()
Entry(pestaña4, textvariable=varCorac).pack()

varConta = StringVar()
Label(pestaña4, text="Contraseña").pack()
Entry(pestaña4, textvariable=varConta, show="*").pack()

btnActualizar = Button(pestaña4, text="Actualizar", command=ejecutaActualizar)
btnActualizar.pack()

#Pestaña 5: Eliminar Usuario
titulo5 = Label(pestaña5,text="Eliminar Usuario", fg='green', font=("Modern",18)).pack()
varIDe = StringVar()
Label(pestaña5, text="ID: ").pack()
Entry(pestaña5, textvariable=varIDe).pack()

btnEliminar = Button(pestaña5, text="Eliminar", command=ejecutaEliminar)
btnEliminar.pack()

panel.add(pestaña1, text='Formulario de usuarios')
panel.add(pestaña2, text='Buscar usuario')
panel.add(pestaña3, text='Consultar usuarios')
panel.add(pestaña4, text='Actualizar usuario')
panel.add(pestaña5, text='Eliminar usuario')

ventana.mainloop()