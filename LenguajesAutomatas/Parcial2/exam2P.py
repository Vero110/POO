class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def encontrar_ancestro_comun(persona1, persona2):
    ancestros1 = obtener_ancestros(persona1)
    ancestros2 = obtener_ancestros(persona2)

    ancestros_comunes = [ancestro for ancestro in ancestros1 if ancestro in ancestros2]

    if len(ancestros_comunes) > 0:
        return ancestros_comunes[-1]
    else:
        return None

def obtener_ancestros(persona):
    ancestros = [persona]
    while persona.hijos:
        persona = persona.hijos[0]
        ancestros.append(persona)
    return ancestros

def crear_arbol_genealogico():
    jupiter = Persona("Jupiter")
    marte = Persona("Marte")
    venus = Persona("Venus")
    jupiter.agregar_hijo(marte)
    jupiter.agregar_hijo(venus)

    marte.agregar_hijo(Persona("Romulo"))
    marte.agregar_hijo(Persona("Remo"))

    remo = marte.hijos[1]
    remo.agregar_hijo(Persona("Faustulos"))
    remo.agregar_hijo(Persona("Hersillia"))

    hersillia = remo.hijos[1]
    hersillia.agregar_hijo(Persona("Romulus"))
    hersillia.agregar_hijo(Persona("Remus"))

    venus.agregar_hijo(Persona("Cupit"))
    venus.agregar_hijo(Persona("Aeneas"))

    cupit = venus.hijos[0]
    cupit.agregar_hijo(Persona("Amor"))
    cupit.agregar_hijo(Persona("Psyche"))

    psyche = cupit.hijos[1]
    psyche.agregar_hijo(Persona("Voluptus"))
    psyche.agregar_hijo(Persona("Gedone"))

    aeneas = venus.hijos[1]
    aeneas.agregar_hijo(Persona("Ascanius"))
    lavinia = Persona("Lavinia")
    aeneas.agregar_hijo(lavinia)

    ascanius = aeneas.hijos[0]
    ascanius.agregar_hijo(Persona("Lulus"))
    lulus = ascanius.hijos[0]
    lulus.agregar_hijo(Persona("Silvius"))

    silvius = lulus.hijos[0]
    silvius.agregar_hijo(Persona("Brutus"))
    brutus = silvius.hijos[0]
    brutus.agregar_hijo(Persona("Tiberius"))
    tiberius = brutus.hijos[0]
    tiberius.agregar_hijo(Persona("Caligula"))
    caligula = tiberius.hijos[0]
    caligula.agregar_hijo(Persona("Agripina"))

    tiberius.agregar_hijo(Persona("Gaius"))

    gaius = tiberius.hijos[1]
    gaius.agregar_hijo(Persona("Nero"))
    nero = gaius.hijos[0]
    nero.agregar_hijo(Persona("Mesalina"))

    nero.agregar_hijo(Persona("Domitian"))
    domitian = nero.hijos[1]
    domitian.agregar_hijo(Persona("Titus"))
    domitian.agregar_hijo(Persona("Domitia"))

    return jupiter

def main():
    arbol_genealogico = crear_arbol_genealogico()

    # Solicitar los nombres de las personas desde la consola
    nombre1 = input("Ingresa el nombre de la primera persona: ")
    nombre2 = input("Ingresa el nombre de la segunda persona: ")

    persona1 = buscar_persona_por_nombre(arbol_genealogico, nombre1)
    persona2 = buscar_persona_por_nombre(arbol_genealogico, nombre2)

    if persona1 is not None and persona2 is not None:
        ancestro_comun = encontrar_ancestro_comun(persona1, persona2)
        if ancestro_comun:
            print(f"El ancestro común más cercano de {persona1.nombre} y {persona2.nombre} es {ancestro_comun.nombre}")
        else:
            print(f"No tienen ancestro común.")
    else:
        print("Al menos una de las personas no se encontró en el árbol genealógico.")

def buscar_persona_por_nombre(persona, nombre):
    if persona.nombre == nombre:
        return persona
    for hijo in persona.hijos:
        resultado = buscar_persona_por_nombre(hijo, nombre)
        if resultado:
            return resultado
    return None

if __name__ == "__main__":
    main()
