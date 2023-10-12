#La predicción de todos los movimientos posibles que puede realizar un caballo 
#en un tablero de ajedrez se puede lograr mediante un algoritmo de búsqueda exhaustiva
#como el algoritmo de búsqueda en profundidad (DFS) o el algoritmo de búsqueda 
#en anchura (BFS).

import tkinter as tk

def es_movimiento_valido(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def calcular_movimientos_caballo(event):
    tablero = [[False for _ in range(8)] for _ in range(8)]

    try:
        x = int(entry_fila.get())
        y = int(entry_columna.get())
    except ValueError:
        resultado_label.config(text="Ingresa filas y columnas válidas")
        return

    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    for i in range(8):
        nuevo_x = x + dx[i]
        nuevo_y = y + dy[i]

        if es_movimiento_valido(nuevo_x, nuevo_y):
            tablero[nuevo_x][nuevo_y] = True

    resultado_label.config(text="Movimientos posibles del caballo:")

    for i in range(8):
        for j in range(8):
            if tablero[i][j]:
                resultado_label.config(text=resultado_label.cget("text") + f" ({i}, {j})")

ventana = tk.Tk()
ventana.title("Movimientos de Caballo en Ajedrez")

fila_label = tk.Label(ventana, text="Fila inicial:")
fila_label.pack()
entry_fila = tk.Entry(ventana)
entry_fila.pack()

columna_label = tk.Label(ventana, text="Columna inicial:")
columna_label.pack()
entry_columna = tk.Entry(ventana)
entry_columna.pack()

calcular_button = tk.Button(ventana, text="Calcular Movimientos")
calcular_button.pack()
calcular_button.bind("<Button-1>", calcular_movimientos_caballo)

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

ventana.mainloop()
