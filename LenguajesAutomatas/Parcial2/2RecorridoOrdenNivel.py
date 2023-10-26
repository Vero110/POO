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

        