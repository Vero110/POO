#funcion para encontrar el elemento mayoritario presente en una lista dada
def findMajorityElement(nums):
    #crea un 'HashMao' vacio 
    d = {}
    #almacena la frecuencia de cada elemento en un diccionario 
    for i in nums:
        d[i]=d.get(i,0) + 1
    
    #devuelve el elemento en su cuenta es mayor que 'n/2'
    for key, value in d.items(): 
        if value > len (nums)/2:
            return key 

    #ningun elemento mayoritario esta presente 
    return -1
if __name__=='__main__':
        #suposicion #entrada valida (el elemento mayoritario esta presente)
    nums = [1,8,7,4,1,2,2,2,2,2,2]
    result = findMajorityElement(nums)
    if result != -1: 
        print('El elemento mayoritario es', result)
    else: 
        print('El elemento mayoritario no existe')
        
    
    