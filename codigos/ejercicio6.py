def validar_palabra_clave(palabra):
    if len(palabra) <= 6:
        return False, "La palabra clave debe tener más de 6 caracteres."
    
    tiene_numero = any(char.isdigit() for char in palabra)
    if not tiene_numero:
        return False, "La palabra clave debe contener al menos un número."
    
    tiene_mayuscula = any(char.isupper() for char in palabra)
    if not tiene_mayuscula:
        return False, "La palabra clave debe contener al menos un carácter en mayúscula."
    
    return True, "La palabra clave es válida."

# Solicitar al usuario que ingrese la palabra clave
while True:
    palabra_clave = input("Ingrese una palabra clave: ")

    es_valida, mensaje = validar_palabra_clave(palabra_clave)
    print(mensaje)

    if es_valida:
        break
