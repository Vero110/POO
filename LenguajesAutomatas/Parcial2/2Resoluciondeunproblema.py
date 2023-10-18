def meridaje_de_vinos(comida, salsa, tipo_vino):
    if tipo_vino == "tinto":
        if comida in ["carne roja", "cordero"] or salsa in ["chimichurri", "barbacoa"]:
            return [["Malbec", "Carne roja", "Chimichurri"], ["Cabernet Sauvignon", "Carne roja", "Chimichurri"]]
        if comida in ["pollo", "pavo", "cerdo"] or salsa in ["setas", "tomate"]:
            return [["Malbec", "Pollo o Cerdo", "Setas o Tomate"], ["Pinot Noir", "Pollo o Cerdo", "Setas o Tomate"]]
    elif tipo_vino == "blanco":
        if comida in ["pescado", "pollo"] or salsa in ["limón", "crema"]:
            return [["Suavignon Blanc", "Pescado o Pollo", "Limón o Crema"], ["Chardonnay", "Pescado o Pollo", "Limón o Crema"]]
        if comida in ["ensalada", "mariscos"] or salsa in ["ajo", "mantequilla"]:
            return [["Chardonnay ", "Ensalada o Mariscos", "Ajo o Mantequilla"], ["Sauvignon Blanc", "Ensalada o Mariscos", "Ajo o Mantequilla"]]

    return [["No se encontraron recomendaciones para esta combinación de comida, salsa y tipo de vino."]]

def main():
    print(".")
    comida = input("Ingresa el tipo de comida (carne roja, pescado, pollo, ensalada, mariscos.): ")
    salsa = input("Ingresa el tipo de salsa (chimichurri, tomate, crema): ")
    tipo_vino = input("¿Prefieres vino tinto o vino blanco?: ").lower()

    recomendaciones = meridaje_de_vinos(comida, salsa, tipo_vino)

    print("Recomendaciones de maridaje:")
    for i, recomendacion in enumerate(recomendaciones, 1):
        print(f"Opción {i}: {recomendacion}")

if __name__ == "__main__":
    main()
