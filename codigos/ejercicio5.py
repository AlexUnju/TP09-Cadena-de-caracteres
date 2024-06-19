def modificar_espacios(frase):
    frase_modificada = ' '.join(frase.split())
    return frase_modificada

# Solicitar al usuario que ingrese la frase
frase_original = input("Ingrese una frase: ")

# Modificar los espacios en blanco según lo requerido
frase_modificada = modificar_espacios(frase_original)

# Mostrar la frase modificada
print("Frase modificada:", frase_modificada)
