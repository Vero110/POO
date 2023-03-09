
#1. Importar la clase 
from Personaje import *

#2. Solicitar atributos para el objeto
print("")
print("### Solicitud de datos del Heroe ### ")
espH= input ("Escribe la especia del Heroe ")
nomH= input ("Escribe el nombre del Heroe ")
altH = float(input ("Escribe la altura del Heroe "))
cargaH= int(input ("¿Cuantas balas se recargaran al Heroe? "))

print("")
print("### Solicitud de datos del Villano ###")
espV= input ("Escribe la especia del Villano ")
nomV= input ("Escribe el nombre del Villano ")
altV = float(input ("Escribe la altura del Villano "))
cargaV= int(input ("¿Cuantas balas se recargaran al Villano? "))

#3. Creamos 2 objetos 
Heroe = Personaje (espH, nomH, altH)





Villano = Personaje (espV, nomV, altV)

#4. Acceder a sus atributos y metodos del cada OBJ
print("")
print ("## Atributos y Metodos del Heroe ## ")
print ("El personaje pertenece a la raza: " + Heroe.especie) 
print ("Se llama: " + Heroe.nombre)
print ("Mide: " + str(Heroe.altura) + " metros") 

Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(cargaH)

print("")
print ("## Atributos y Metodos del Villano ## ")
print ("El personaje pertenece a la raza: " + Villano.especie) 
print ("Se llama: " + Villano.nombre)
print ("Mide: " + str(Villano.altura) + " metros ") 

Villano.correr(False)
Villano.lanzarGranada()
Villano.recargarArma(cargaV)