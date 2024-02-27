def teorema():
    num_eventos = int(input("ingrese la cant de eventos: "))
    eventos = []
    for i in range(num_eventos):
        prob_evento = float(input(f"ingrese la probabilidad del evento A{i + 1}: "))
        eventos.append(prob_evento)
    if len(eventos) != num_eventos:
        raise ValueError("la cantidad de eventos y probabilidades no coincide")
    probabilidades = []
    for i in range(num_eventos):
        prob_condicional = float(input(f"ingrese la probabilidad condicional de B dado A{i + 1}: "))
        probabilidades.append(prob_condicional)
        
    numerador = eventos[1] * probabilidades[1] 
    denominador = sum([p_a * p_b for p_a, p_b in zip(eventos, probabilidades)])  
    resultado = numerador / denominador
    return resultado

resultado = teorema()
print(f"el resultado es: {resultado:.4f}")
