
class Personaje:
    #Creamos al constructor
    def __init__(self, esp, nom, alt):  #(..)Son los parametros
    #atributos del personaje
        self.especie = esp
        self.nombre = nom
        self.altura = alt 
    
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
        