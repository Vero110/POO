import networkx as nx

def kruskal_path():
    # Pedir el número de aristas
    num_aristas = int(input("Ingrese el número de aristas: "))

    # Crear un grafo vacío
    G = nx.Graph()

    # Pedir las aristas y sus pesos
    for i in range(num_aristas):
        inicio = input("Ingrese el nodo de inicio de la arista {}: ".format(i+1))
        final = input("Ingrese el nodo de final de la arista {}: ".format(i+1))
        peso = float(input("Ingrese el peso de la arista {}: ".format(i+1)))

        # Agregar la arista al grafo con su peso
        G.add_edge(inicio, final, weight=peso)

    # Calcular el árbol de expansión mínima utilizando Kruskal
    mst = nx.minimum_spanning_tree(G)

    # Calcular el camino mínimo entre dos nodos
    inicio = input("Ingrese el nodo de inicio del camino mínimo: ")
    final = input("Ingrese el nodo de final del camino mínimo: ")

    try:
        camino_minimo = nx.shortest_path(mst, source=inicio, target=final, weight='weight')
        peso_camino_minimo = nx.shortest_path_length(mst, source=inicio, target=final, weight='weight')
        print("El camino mínimo es:", camino_minimo)
        print("El peso del camino mínimo es:", peso_camino_minimo)
    except nx.NetworkXNoPath:
        print("No hay camino entre los nodos proporcionados.")

if __name__ == "__main__":
    kruskal_path()

