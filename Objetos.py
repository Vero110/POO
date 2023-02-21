
#1. Importar la clase 
from Personaje import *

#2. Instanciar un objeto 
Heroe = Personaje()

#3. Acceder a sus atributos 
print ("El personaje pertenece a la raza: " + Heroe.especie)
print ("El personaje se llama: " + Heroe.nombre) 
print ("El personaje mide: " + str(Heroe.altura) + "metros") 

#4. Acceder a los metodos 
Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(23)
