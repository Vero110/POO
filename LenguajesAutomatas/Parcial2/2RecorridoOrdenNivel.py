from collections import deque 
#una clase para almacenar un nodo de arbol binario 
class Node: 
    def __init__(self,key=None, left=None,right=None):
        self.key = key 
        self.left = left 
        self.right = right 
    #Funcion para imprimir el recorrido del orden de nivel de un arbol binario 
def levelOrderTraversal(root):
    #caja base
    if not root: 
        return  
    queue = deque()
    queue.append(root)
    #bucle hasta que la queue este vacia 
    while queue: 
        #procesa cada nodo en la que queue y pone en sus hijo izq y derecho no vacio 
        curr = queue.popleft()
        print(curr.key, end='')
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
if __name__ == '__main__':
    root = Node (15)
    root.left = Node(10)
    root.right = Node (20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
    
    levelOrderTraversal(root)




                
    

        