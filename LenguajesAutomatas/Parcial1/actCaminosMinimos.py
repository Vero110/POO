#funcion para imprimir el itinerario partiendo de una fuente dada src
def print_itinerary(dictionary, src):
    dest=dictionary.get(src)
    if not dest:
        return 
    print(src+ '-->' + dest)
    print_itinerary(dictionary, dest)
    
    #funcion para encontrar el itinerario de la lista dada
def finditinerary(tickets):
    #construir un conjunto de aeropuertos de destino 
    destinations = {*tickets.values()}
    #considere cada aeropuerto de salida 
    for k, v in tickets.items(): 
        #el aeropuerto de origen no estara presente en la lista de aeropuerto de destino 
        if k not in destinations: 
            #cuando se encuentre en el aeropuerto de origen 
            print_itinerary(tickets,k)
            return
if __name__ == '__main__':
    #entrada: lista de tickets 
    tickets = {
        'LAX':'DXB',
        'DFW':'JFK',
        'LHR':'DFW',
        'JFK':'LAX'
    }
    finditinerary(tickets)
    