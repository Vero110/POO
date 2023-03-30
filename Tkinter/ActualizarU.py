import tkinter as tk

# Base de datos ficticia de usuarios
usuarios = {'Juan': '1234', 'María': '5678', 'Pedro': '9012'}

# Función que busca un usuario en la base de datos
def buscar_usuario():
    user = entry_user.get()
    if user in usuarios:
        message['text'] = f'Usuario encontrado. Contraseña: {usuarios[user]}'
    else:
        message['text'] = 'Usuario no encontrado.'

# Creación de la ventana principal
ventana = tk.Tk()
ventana.title('Buscar usuario')

# Creación de los widgets
label_user = tk.Label(ventana, text='Usuario:')
entry_user = tk.Entry(ventana)
button_search = tk.Button(ventana, text='Buscar', command=buscar_usuario)
message = tk.Message(ventana, width=200)

label_user.grid(row=0, column=1)
entry_user.grid(row=0, column=2)
button_search.grid(row=1, column=0, columnspan=3)
message.grid(row=2, column=0, columnspan=3)

# Bucle principal
ventana.mainloop()
