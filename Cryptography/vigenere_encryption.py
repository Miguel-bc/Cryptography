def vigenere_encryption(Mensaje_Original, Palabra_Clave, Idioma):
    
    from .constants import Abecedario_sp
    from .convert_to_numbers import convert_to_numbers
    
    if Idioma == "sp":
        Abecedario = Abecedario_sp
    
    Mensaje_Numeros = convert_to_numbers(Mensaje_Original, Abecedario)
        
    Mensaje_Encriptado = Mensaje_Numeros
        
    return Mensaje_Encriptado
    