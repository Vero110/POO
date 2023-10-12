#CARTAS
import tkinter as tk
from tkinter import simpledialog
import itertools

# Función de barajado personalizada
def shuffle_deck(deck):
    n = len(deck)
    for i in range(n - 1, 0, -1):
        j = i - 1
        rand_idx = i
        while j >= 0:
            rand_idx = (rand_idx + 7) % n  # Cambia el valor 7 para ajustar la cantidad de mezclas
            deck[i], deck[rand_idx] = deck[rand_idx], deck[i]
            j -= 1

# Función para repartir cartas a los jugadores
def deal_cards(num_participants):
    players = [[] for _ in range(num_participants)]
    for _ in range(7):
        for i in range(num_participants):
            players[i].append(deck.pop(0))
    return players

# Crear una baraja de cartas (52 cartas)
suits = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [{'valor': value, 'palo': suit} for value in values for suit in suits]

# Crear ventana de tkinter
root = tk.Tk()
root.title("Juego de Baraja")

# Pedir el número de participantes (entre 2 y 4) usando un cuadro de diálogo
while True:
    num_participants = simpledialog.askinteger("Número de Participantes", "Ingrese el número de participantes (entre 2 y 4): ")
    if num_participants and 2 <= num_participants <= 4:
        break
    else:
        tk.messagebox.showerror("Error", "Número de participantes no válido. Intente nuevamente.")

# Barajar la baraja de cartas
shuffle_deck(deck)

# Repartir cartas a los jugadores
players = deal_cards(num_participants)

# Mostrar las cartas de cada jugador en cuadros de texto separados
for i, player_cards in enumerate(players):
    player_label = tk.Label(root, text=f"Cartas del Jugador {i + 1}:")
    player_label.pack()

    player_text = tk.Text(root, height=5, width=30)
    player_text.pack()

    for card in player_cards:
        player_text.insert(tk.END, f"{card['valor']} de {card['palo']}\n")

# Etiqueta para mostrar las cartas restantes en la baraja
remaining_label = tk.Label(root, text="Cartas restantes en la baraja:")
remaining_label.pack()

# Cuadro de texto para mostrar las cartas restantes
remaining_text = tk.Text(root, height=10, width=30)
remaining_text.pack()

for card in deck:
    remaining_text.insert(tk.END, f"{card['valor']} de {card['palo']}\n")

root.mainloop()



