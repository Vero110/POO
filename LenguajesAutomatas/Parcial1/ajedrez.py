import tkinter as tk

def es_movimiento_valido(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def mostrar_movimientos(x, y):
    movimientos = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    for dx, dy in movimientos:
        nuevo_x = x + dx
        nuevo_y = y + dy
        if es_movimiento_valido(nuevo_x, nuevo_y):
            canvas.create_rectangle(nuevo_x * 50, nuevo_y * 50, (nuevo_x + 1) * 50, (nuevo_y + 1) * 50, fill="green")

def on_click(event):
    x = event.x // 50
    y = event.y // 50

    canvas.delete("movimiento")
    mostrar_movimientos(x, y)

root = tk.Tk()
root.title("Movimientos de Caballo en Ajedrez")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

for x in range(8):
    for y in range(8):
        color = "white" if (x + y) % 2 == 0 else "black"
        canvas.create_rectangle(x * 50, y * 50, (x + 1) * 50, (y + 1) * 50, fill=color)

canvas.bind("<Button-1>", on_click)

root.mainloop()


