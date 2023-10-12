import sys

# Una clase para representar un objeto graph
class Graph:
    # Constructor
    def _init_(self, edges, n):
        # Una lista de listas para representar una lista de adyacencia
        self.adjList = [[] for _ in range(n)]
        # Agrega bordes al grafo dirigido
        for (source, dest, weight) in edges:
            self.adjList[source].append((dest, weight))

# Realiza DFS en el grafo y establece la hora de salida de todos
# los vértices del grafo
def DFS(graph, v, discovered, departure, time):
    # Marca el nodo actual como descubierto
    discovered[v] = True

    # Establece hora de llegada - no es necesario
    # time = time + 1
    # Recorre cada arista (v, u)
    for (u, w) in graph.adjList[v]:
        # Si `u` aún no se ha descubierto
        if not discovered[u]:
            time = DFS(graph, u, discovered, departure, time)

    # Listo para dar marcha atrás
    # Establece la hora de salida del vértice `v`
    departure[time] = v
    time = time + 1
    return time

def findLongestDistance(graph, source, n):
    departure = [-1] * n
    # Para realizar un seguimiento de si se ha descubierto un vértice o no
    discovered = [False] * n
    time = 0
    # Realiza DFS en todos los vértices no descubiertos
    for i in range(n):
        if not discovered[i]:
            time = DFS(graph, i, discovered, departure, time)
    cost = [sys.maxsize] * n
    cost[source] = 0
    for i in reversed(range(n)):
        v = departure[i]
        # Arista de `v` a `u` con peso 'w'
        for (u, w) in graph.adjList[v]:
            w = -w
            if cost[v] != sys.maxsize and cost[v] + w < cost[u]:
                cost[u] = cost[v] + w

    # Imprime las distancias más largas
    for i in range(n):
        print(f'dist({source}, {i}) = {-cost[i]}')

if __name__ == '_main_':
    # Solicitar al usuario la entrada para crear el arreglo de tripletes
    n = int(input("Ingrese la cantidad de vértices: "))
    edges = []
    for i in range(n):
        source, dest, weight = map(int, input(f"Ingrese el vértice origen, destino y peso para el vértice {i+1}: ").split())
        edges.append((source, dest, weight))

    # Construye un grafo a partir de los bordes dados
    graph = Graph(edges, n)
    # Vértice fuente
    source = int(input("Ingrese el vértice de origen: "))
    # Encuentra la distancia más larga de todos los vértices desde una fuente dada
    findLongestDistance(graph, source, n)
    
                
            