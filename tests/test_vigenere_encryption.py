from Cryptography.vigenere_encryption import vigenere_encryption

print("Introduce el mensaje para ser cifrado: ")
Mensaje_Original = input()

print("Introduce la palabra clave: ")
Palabra_Clave = input()

print("Introduce el abecedario a utilizar")
Abecedario = input()

print(vigenere_encryption(Mensaje_Original, Palabra_Clave, Abecedario))
