import tkinter as tk
from tkinter import simpledialog, messagebox

def print_itinerary(dictionary, src):
    dest = dictionary.get(src)
    if not dest:
        return
    result_text.insert(tk.END, f'{src} --> {dest}\n')
    print_itinerary(dictionary, dest)

def findItinerary(tickets):
    destinations = {*tickets.values()}
    for k, v in tickets.items():
        if k not in destinations:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Itinerario mínimo:\n")
            print_itinerary(tickets, k)
            return

def calculate_itinerary():
    try:
        num_trayectos = int(simpledialog.askstring("Trayectos", "¿Cuántos trayectos son?"))
        tickets = {}
        for i in range(num_trayectos):
            origen = simpledialog.askstring("Origen", f"Parada inicio {i + 1}:")
            destino = simpledialog.askstring("Destino", f"  Parada destino {i + 1}:")
            tickets[origen] = destino

        findItinerary(tickets)
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido para la cantidad de trayectos.")

root = tk.Tk()
root.title("Itinerario Mínimo")

canvas = tk.Canvas(root, height=300, width=400)
canvas.pack()

frame = tk.Frame(root, bg="lightgray")
frame.place(relwidth=1, relheight=1)

calculate_button = tk.Button(frame, text="Calcular Itinerario", command=calculate_itinerary)
calculate_button.pack(pady=10)

result_text = tk.Text(frame, height=10, width=40)
result_text.pack(padx=20, pady=10)

root.mainloop()
