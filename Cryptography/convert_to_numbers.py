def convert_to_numbers(Mensaje, Abecedario):
    
    def obtener_valores(diccionario, lista_claves):
        return [diccionario[clave] for clave in lista_claves]
    
    letras = list(Mensaje)
    
    try:
        valores = obtener_valores(Abecedario, letras)   
             
    except KeyError as e:
        print(f"Error: Clave '{e.args[0]}' no encontrada en el diccionario.")
    
    return valores
