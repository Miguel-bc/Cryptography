import math

def vigenere_encryption(Mensaje_Original, Palabra_Clave, Idioma):
    
    from .constants import Abecedario_sp
    from .convert_to_numbers import convert_to_numbers
    
    if Idioma == "sp":
        Abecedario = Abecedario_sp
        
    tamanyo = len(Mensaje_Original)
    longitud = math.ceil(len(Mensaje_Original) / len(Palabra_Clave))
    
    Mensaje_Original_Numeros = convert_to_numbers(Mensaje_Original, Abecedario)       
    Clave_Extendida = convert_to_numbers(Palabra_Clave, Abecedario) * longitud
    Clave_Extendida = Clave_Extendida[:tamanyo]   
    
    Mensaje_Encriptado = list(map(sum, zip(Mensaje_Original_Numeros, Clave_Extendida)))
        
    return Mensaje_Encriptado
    