from tkinter import (Tk, Text, Button, Label, Menu,
                     END, INSERT, SEL_FIRST, SEL_LAST, simpledialog)

class GUI(Tk):
    def __init__(self):
        super(GUI, self).__init__()
        self.geometry("300x300+350+80")
        self.title("Encriptador")
        self.resizable(width=False, height=False)

        # Cuadro de texto...
        self.texto = Text(self, font=datos.fuente2)
        self.texto.place(x=0, y=30, width=300, height=218)

        # Panel superior...
        self.panel = Label(self,
                           text="Ingrese un texto",
                           bg="gray93",
                           font=datos.fuente2)
        self.panel.place(x=0, y=0, width=300, height=30)

        # Botones...
        self.botones()

        # Menu desplegable...
        self.menu_desplegable()

    def botones(self):
        # Botones...
        boton_encriptar = Button(self,
                                 text="Encriptar",
                                 font=datos.fuente2,
                                 relief="flat",
                                 command=lambda: funcion.boton("encriptado"))
        # Se usa lambda para poder pasar argumentos...

        # Se posicionan los botones...
        boton_encriptar.place(x=0, y=248, width=150, height=52)

    def menu_desplegable(self):
        "Menu desplegable con 3 items (Cortar, copiar y pegar)..."
        # Se crea el menu...
        self.menu_desplegable = Menu(self, tearoff=0)

        # Se agrega el item "Cortar"...
        self.menu_desplegable.add_command(label="Cortar",
                                          font=datos.fuente,
                                          command=lambda: funcion.menu("cortar"))

        # Se agrega el item "Copiar"...
        self.menu_desplegable.add_command(label="Copiar",
                                          font=datos.fuente,
                                          command=lambda: funcion.menu("copiar"))

        # Se agrega un separador...
        self.menu_desplegable.add_separator()

        # Se agrega el item "Pegar"...
        self.menu_desplegable.add_command(label="Pegar",
                                          font=datos.fuente,
                                          command=lambda: funcion.menu("pegar"))

        # Evento del menu desplegable(lanza el menu si se presiona el clic derecho)...
        self.texto.bind("<Button-3>", lambda evento: self.menu_desplegable.post(evento.x_root, evento.y_root))
        # "evento" da la posición en donde luego se lanza el menu(.post) en las ubicaciones dadas(x_root,y_root)


class Funciones:
    "Conjunto de funciones..."

    def encriptado(self, mensaje, modo, capas):
        # Método para encriptar...
        # Se reemplaza cada letra por la siguiente según corresponda...

        for _ in range(capas):
            mensaje = self.encriptar_una_capa(mensaje, modo)
        return mensaje

    def encriptar_una_capa(self, mensaje, modo):
        if modo == "encriptado":
            clave = -2
        else:
            clave = 2
        traduccion = ""
        for simbolo in mensaje:
            if simbolo.isalpha():
                num = ord(simbolo)
                num += clave
                if simbolo.isupper():
                    if num > ord("Z"):
                        num -= 26
                    elif num < ord("A"):
                        num += 26
                elif simbolo.islower():
                    if num > ord("z"):
                        num -= 26
                    elif num < ord("a"):
                        num += 26
                traduccion += chr(num)
            else:
                traduccion += simbolo
        return traduccion

    def boton(self, modo):
        # Se lee lo escrito...
        mensaje = ventana.texto.get("0.0", END)

        # Preguntar al usuario cuántas capas de encriptación desea aplicar
        capas = simpledialog.askinteger("Capas de encriptación", "Ingrese el número de capas de encriptación:",
                                        parent=ventana, minvalue=1)

        if capas is not None:
            # Se lo lleva a encriptar...
            texto = self.encriptado(mensaje, modo, capas)

            # Se borra el texto escrito...
            ventana.texto.delete("0.0", END)

            # Se inserta el texto encriptado...
            ventana.texto.insert("0.0", texto)

            # Se cambia el mensaje del panel...
            ventana.panel.config(text="texto " + modo)

    def menu(self, modo):
        # Funciones del menu desplegable...
        if modo == "cortar":
            try:
                # Se limpia la memoria...
                ventana.texto.clipboard_clear()
                # Se agrega a memoria lo seleccionado...
                ventana.texto.clipboard_append(ventana.texto.selection_get())
                # Se borra lo seleccionado...
                ventana.texto.delete(SEL_FIRST, SEL_LAST)

            except:
                print("Selección vacía")

        elif modo == "copiar":
            try:
                # Se limpia la memoria...
                ventana.texto.clipboard_clear()
                # Se agrega a memoria lo seleccionado...
                ventana.texto.clipboard_append(ventana.texto.selection_get())

            except:
                print("Selección vacía")

        elif modo == "pegar":
            try:
                # Se inserta el texto en memoria a la zona del cursor en el cuadro de texto...
                ventana.texto.insert(INSERT, ventana.texto.selection_get(selection="CLIPBOARD"))

            except:
                print("Selección vacía")


class datos:
    "Conjunto de variables usadas por el programa..."
    fuente = ("Century Gothic", 9)
    fuente2 = ("Century Gothic", 10)


if __name__ == "__main__":
    funcion = Funciones()
    ventana = GUI()
    ventana.mainloop()
