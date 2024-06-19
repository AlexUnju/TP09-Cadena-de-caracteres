def primera_letra_mayuscula(cadena):
    palabras = cadena.split()  # Divide la cadena en palabras
    resultado = []
    for palabra in palabras:
        primera_letra = palabra[0].upper()  # Obtiene la primera letra de la palabra y la convierte a mayúscula
        resultado.append(primera_letra)  # Agrega la primera letra al resultado
    
    resultado = ''.join(resultado)  # Une todas las letras obtenidas en un solo string
    return resultado

# Ejemplo de uso
cadena = "universal serial bus"
resultado = primera_letra_mayuscula(cadena)
print(resultado)  # Debería imprimir "USB"
