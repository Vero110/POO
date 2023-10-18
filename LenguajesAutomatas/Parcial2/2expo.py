# Clase NodoBST: utilizada para representar un nodo en un árbol binario de búsqueda (BST).
# Valor: Almacena el valor que se asigna al nodo.
# izquierda: Es una referencia al nodo hijo izquierdo (valores menores).
# derecha: Es una referencia al nodo hijo derecho (valores mayores).
class NodoBST:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        # no tiene valor
        self.raiz = None

    def insertar(self, valor):
        #insertar un valor 
        self.raiz = self._insertar_recursivamente(self.raiz, valor)

    def _insertar_recursivamente(self, nodo, valor):
        #inserción recursiva de un valor.
        if nodo is None:
            #si el nodo es nulo, crea un nuevo nodo con el valor.
            return NodoBST(valor)
        if valor < nodo.valor:
            #sii el valor es menor, inserta en el subárbol izquierdo.
            nodo.izquierda = self._insertar_recursivamente(nodo.izquierda, valor)
        else:
            #si el valor es mayor o igual, inserta en el subárbol derecho.
            nodo.derecha = self._insertar_recursivamente(nodo.derecha, valor)
        return nodo

    def buscar(self, valor):
        #buscar un valor
        return self._buscar_recursivamente(self.raiz, valor)

    def _buscar_recursivamente(self, nodo, valor):
        #búsqueda recursiva de un valor.
        if nodo is None or nodo.valor == valor:
            #si el nodo es nulo o se encuentra el valor, se retorna el nodo.
            return nodo
        if valor < nodo.valor:
            #si el valor es menor, busca en el subárbol izquierdo.
            return self._buscar_recursivamente(nodo.izquierda, valor)
        return self._buscar_recursivamente(nodo.derecha, valor)

    def eliminar(self, valor):
        #eliminar un valor del árbol.
        self.raiz = self._eliminar_recursivamente(self.raiz, valor)

    def _eliminar_recursivamente(self, nodo, valor):
        # eliminación recursiva de un valor.
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            # si es menor, elimina en el subárbol izquierdo.
            nodo.izquierda = self._eliminar_recursivamente(nodo.izquierda, valor)
        elif valor > nodo.valor:
            # si es mayor, elimina en el subárbol derecho.
            nodo.derecha = self._eliminar_recursivamente(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.valor = self._encontrar_min_valor(nodo.derecha)
            nodo.derecha = self._eliminar_recursivamente(nodo.derecha, nodo.valor)
        return nodo

    def _encontrar_min_valor(self, nodo):
        #encontrar el valor mínimo en un subárbol.
        min_valor = nodo.valor
        while nodo.izquierda is not None:
            min_valor = nodo.izquierda.valor
            nodo = nodo.izquierda
        return min_valor

    def _encontrar_max_valor(self, nodo):
        #encontrar el valor máximo en un subárbol.
        max_valor = nodo.valor
        while nodo.derecha is not None:
            max_valor = nodo.derecha.valor
            nodo = nodo.derecha
        return max_valor

    def obtener_valor_minimo(self):
        #obtener el valor mínimo en el árbol.
        if self.raiz is not None:
            return self._encontrar_min_valor(self.raiz)
        else:
            return None

    def obtener_valor_maximo(self):
        #obtener el valor máximo en el árbol.
        if self.raiz is not None:
            return self._encontrar_max_valor(self.raiz)
        else:
            return None

    def imprimir_inorden(self):
        #imprimir los valores del árbol en orden
        self._imprimir_inorden_recursivamente(self.raiz)

    def _imprimir_inorden_recursivamente(self, nodo):
        #recorrido en orden del árbol.
        if nodo:
            self._imprimir_inorden_recursivamente(nodo.izquierda)
            print(nodo.valor, end=' ')
            self._imprimir_inorden_recursivamente(nodo.derecha)

# Ejemplo de uso
arbol = ArbolBinarioBusqueda()
valores = [50, 30, 70, 20, 40, 60, 80]

for valor in valores:
    arbol.insertar(valor)

print("Recorrido en orden del árbol BST:")
arbol.imprimir_inorden()

valor_buscar = int(input("\nIngrese el valor que desea buscar: "))
nodo_encontrado = arbol.buscar(valor_buscar)
if nodo_encontrado:
    print(f"Valor {valor_buscar} encontrado en el árbol.")
else:
    print(f"Valor {valor_buscar} no encontrado en el árbol.")

valor_eliminar = int(input("Ingrese el valor que desea eliminar: "))
arbol.eliminar(valor_eliminar)
print("Recorrido en orden después de la eliminación:")
arbol.imprimir_inorden()

valor_minimo = arbol.obtener_valor_minimo()
valor_maximo = arbol.obtener_valor_maximo()

print(f"\nValor mínimo en el árbol: {valor_minimo}")
print(f"Valor máximo en el árbol: {valor_maximo}\n") 


