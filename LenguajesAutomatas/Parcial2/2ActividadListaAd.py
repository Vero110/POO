class Graph:
    def __init__(self,edges,n):
        self.adjList =[[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def isSafe(graph, color, v, c):
    for u in graph.adjList[v]:
        if color[u] == c:
            return False
    return True

def kColorable(g, color, k, v, n):
    if v == n:
        print([COLORS[color[v]] for v in range(n)])
        return
    
    for c in range(1, k +1):
        if isSafe(g, color, v, c):
            color[v] = c
            kColorable(g,color,k,v + 1, n)
            color[v] = 0

if __name__ == '__main__':
    edges = []
    
    e = int(input("Ingresa la cantidad de aristas: "))
    
    for i in range(e):
        edge_str = input(f'Ingresa la arista {i + 1} en formato (x, y): ')
    
        edge_str = edge_str.replace(" ", "")
        
        if edge_str.startswith("(") and edge_str.endswith(")"):
            try:
                x, y = map(int, edge_str[1:-1].split(","))
                edges.append((x, y))
            except ValueError:
                print(f'La entrada "{edge_str}" no es valido. Debe ser un par de números separados por coma en paréntesis.')
        else:
            print(f'La entrada "{edge_str}" no es valida. Debe estar entre paréntesis.')
    
    
    print(edges)
    COLORS = []
    
    colores_genericos = int(input("Ingresa la cantidad de colores: "))
    
    for i in range(colores_genericos):
        colour = str(input(f"Ingresa el nombre del color {i + 1}: "))
        COLORS.append(colour)
        
    print(COLORS)
    
    n = int(input("Ingresa la cantidad de vertices: "))
    
    g = Graph(edges, n)
    k = 4
    color = [None] * n
    
    kColorable(g, color, k, 0, n)

