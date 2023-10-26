class TreeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def find_lca(root, person1, person2):
    if root is None:
        return None

    if root.name == person1 or root.name == person2:
        return root

    left_lca = find_lca(root.left, person1, person2)
    right_lca = find_lca(root.right, person1, person2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca else right_lca

def find_common_ancestor(root, persons):
    if len(persons) < 2:
        return None

    common_ancestor = find_lca(root, persons[0], persons[1])

    for i in range(2, len(persons)):
        common_ancestor = find_lca(root, common_ancestor.name, persons[i])

    return common_ancestor

# Construir el árbol de ejemplo
root = TreeNode("UZIEL I ")
root.left = TreeNode("JESUS")
root.right = TreeNode("GRACIELA")
root.left.left = TreeNode("JOSE")
root.left.right = TreeNode("LUIS MIGUEL")
root.right.left = TreeNode("VALENTINA")
root.right.right = TreeNode("ALFREDITO OLIVAS")
root.left.left.left = TreeNode("CRISTIAN")
root.left.left.right = TreeNode("XAVIER")
root.left.right.left = TreeNode("LIONEL")
root.left.right.right = TreeNode("CRISTIANO R")
root.left.left.left.left = TreeNode("MICHAEL")
root.left.left.left.right = TreeNode("MICHELLE")
root.left.left.right.right = TreeNode("BARACK")
root.left.right.left.left = TreeNode("RONALDINHO")
root.left.right.left.right = TreeNode("DANA")
root.left.right.right.left = TreeNode("CRISTIAN N")
root.left.right.right.right = TreeNode("DIEGO")
root.right.left.left= TreeNode("MAGY")
root.right.left.right= TreeNode("BART")
root.right.right.left= TreeNode("JOAQUIN")
root.right.right.right= TreeNode("JUAN")
root.left.left.right.right.left = TreeNode("GEORGE")
root.left.left.right.right.right = TreeNode("KALEB")
root.left.right.left.right.right = TreeNode("GOKU")
root.left.right.right.right.right = TreeNode("BENITO")
root.right.left.left.left= TreeNode("BRAYAN")
root.right.left.left.right= TreeNode("VALENTINA II")
root.right.right.left.left= TreeNode("ARTURO")
root.right.right.right.right= TreeNode("MELCHOR")
root.left.right.left.right.right.left = TreeNode("GOHAN")
root.left.right.left.right.right.right = TreeNode("GOTEN")
root.left.right.right.right.right.left = TreeNode("DANIEL")
root.left.right.right.right.right.right = TreeNode("KEVIN")
root.right.left.left.left.left= TreeNode("KIMBERLY")
root.right.left.left.left.right= TreeNode("BRITANNY")
root.right.right.left.left.left= TreeNode("OVIDIO GUZMAN")
root.right.right.right.right.left= TreeNode("GASPAR")
root.right.right.right.right.right= TreeNode("BALTAZAR")
root.left.right.left.right.right.left.left = TreeNode("PANQUE")
root.right.left.left.left.left.right= TreeNode("IAN")
root.right.left.left.right.left= TreeNode("ALEX")
root.right.left.left.right.right= TreeNode("PENELOPE")
root.right.right.right.right.left.left= TreeNode("ELIEL")
root.right.right.right.right.right.right= TreeNode("OMAR")
root.left.right.left.right.right.left.left.right = TreeNode("GOKU II")
root.right.left.left.left.left.right.left= TreeNode("YANDEL")
root.right.left.left.left.left.right.right= TreeNode("KENIA OS TU PATRONA ")

# Lista de nombres
names = ["UZIEL I", "JESUS", "GRACIELA", "JOSE", "LUIS MIGUEL", "VALENTINA", 
         "ALFREDITO OLIVAS", "CRISTIAN", "XAVIER", "LIONEL", "CRISTIANO R", 
         "MICHAEL", "MICHELLE", "BARACK", "RONALDINHO", "DANA", "CRISTIAN N", 
         "DIEGO", "MAGY", "BART", "JOAQUIN", "JUAN", "GEORGE", "KALEB", "GOKU", 
         "BENITO", "BRAYAN", "VALENTINA II", "ARTURO", "MELCHOR", "GOHAN", "GOTEN",
         "DANIEL", "KEVIN", "KIMBERLY", "BRITANNY", "OVIDIO GUZMAN", "GASPAR", "BALTAZAR",
         "PANQUE", "IAN", "ALEX", "PENELOPE", "ELIEL", "OMAR", "GOKU II", "YANDEL", 
         "KENIA OS TU PATRONA"]

# Función para encontrar un nodo dado un nombre
def find_node(root, name):
    if root is None:
        return None

    if root.name == name:
        return root

    left = find_node(root.left, name)
    if left:
        return left

    right = find_node(root.right, name)
    return right

# Preguntas de ejemplo para encontrar el ancestro común
person1 = "YANDEL"
person2 = "IAN"
person3 = "ALEXANDER"
ancestors = [person1, person2, person3]

# Verificar si las personas están en el árbol
for person in ancestors:
    if find_node(root, person) is None:
        print(f"{person} no tiene ancestros")
        break
else:
    common_ancestor = find_common_ancestor(root, ancestors)
    print(f"El ancestro común de {', '.join(ancestors)} es {common_ancestor.name}")
