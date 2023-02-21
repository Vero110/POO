
class Personaje: 
    
    #atributos del personaje
    especie = "Humano"
    nombre = "Je"
    altura = 1.90 
    
    #metodos Personaje
    def correr(self,status):
        if(status): 
            print("El personaje "+ self.nombre + "esta corriendo")
        else: 
            print("El personaje "+ self.nombre + "se detuvo") 
    
    def lanzarGranada(self): 
        print ("Se lanzo Granada ")
        
    def recargarArma(self, municiones):
        cargador = 5 
        cargador = cargador + municiones
        print ("El arma tiene ahora: "+ str(cargador) + "balas")
        