class DisjointSet:
    parent={}
    
    def makeSet(self,n):
    #crear 'n' conjuntos disjuntos (uno para cada vertice)
        for i in range(n):
            self.parent[i] = i
            
    def find(self, k):
            #si 'k' es root
        if self.parent[k] == k:
            return k
        #recurre para el paso hasta encontrar la raiz
        return self.find(self.parent[k])
    
    #realizar union de dos subconjuntos
    def union (self,a,b):
        #encontrar la raiz de los conjuntos a los que pertenecen los elementos 'x' y 'y'
        x = self.find(a)
        y = self.find(b)
        
        self.parent[x]=y 
    #funcion para construir MST usando el alg de kruskal 
def runKruskalAlgorithm(edges,n):
    #almacena los bordes presentes en MST    
    MST = []
        
    ds = DisjointSet()
    ds.makeSet(n)
        
    index = 0 
        
    #ordena los bordes aumentando el peso 
    edges.sort(key=lambda x: x[2])
        
    #MST contiene exactamente aristas 'V-1'
    while len(MST) !=n-1:
        #considerar el borde sig con peso minimo del graph
        (src, dest, weight)=edges[index]
        index = index + 1 
            
        x = ds.find(src)
        y = ds.find(dest)
        if x !=y: 
            MST.append((src, dest, weight))
            ds.union(x,y)
            
    return MST
    
if __name__ == '__main__':
    edges = [(0,1,7), (1,2,8),(0,3,5), (1,3,9),(1,4,7), (2,4,5),(3,4,15),(3,5,6),(4,5,8), (4,6,9),(5,6,11)]
                
    n=7
    e=runKruskalAlgorithm(edges,n)
    print(e)
            
        
            
            