def proba(p_ingeniero, p_economista, p_directivo_ingeniero, p_directivo_economista, p_directivo_no_ingeniero_no_economista):
    # P(Ingeniero|Directivo) = P(Directivo|Ingeniero) * P(Ingeniero) / P(Directivo)
    
    # P(Directivo) = P(Directivo|Ingeniero) * P(Ingeniero) + P(Directivo|Economista) * P(Economista) + P(Directivo|NoIngenieroNoEconomista) * P(NoIngenieroNoEconomista)
    p_directivo = p_directivo_ingeniero * p_ingeniero + p_directivo_economista * p_economista + p_directivo_no_ingeniero_no_economista * (1 - p_ingeniero - p_economista)
    
    # P(Ingeniero|Directivo) = P(Directivo|Ingeniero) * P(Ingeniero) / P(Directivo)
    p_ingeniero_dado_directivo = (p_directivo_ingeniero * p_ingeniero) / p_directivo
    
    return p_ingeniero_dado_directivo

ingeniero = float(input("Ingrese la probabilidad de ser ingeniero: "))
economista = float(input("Ingrese la probabilidad de ser economista: "))
directivo_ingeniero = float(input("Ingrese la probabilidad de ser directivo dado que es ingeniero: "))
directivo_economista = float(input("Ingrese la probabilidad de ser directivo dado que es economista: "))
directivo_no_ingeniero_no_economista = float(input("Ingrese la probabilidad de ser directivo dado que no es ingeniero ni economista"))

resultado = proba(ingeniero, economista, directivo_ingeniero, directivo_economista, directivo_no_ingeniero_no_economista)

print(f"La probabilidad de que un empleado directivo elegido al azar sea ingeniero es: {resultado}")
