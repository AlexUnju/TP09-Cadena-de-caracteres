def binario_a_decimal(cadena_binaria):
    # Verificar que la cadena solo contenga '0' y '1'
    for bit in cadena_binaria:
        if bit != '0' and bit != '1':
            print("La cadena debe contener solo '0' y '1'")
            return None
    
    # Convertir la cadena binaria a decimal
    decimal = 0
    longitud = len(cadena_binaria)
    
    for i in range(longitud):
        bit = int(cadena_binaria[longitud - 1 - i])  # Convertir el carácter a entero
        decimal += bit * (2 ** i)  # Calcular el valor decimal
    
    return decimal

# Ejemplo de uso
cadena_binaria = "1011"
resultado = binario_a_decimal(cadena_binaria)
if resultado is not None:
    print(f"El valor decimal de '{cadena_binaria}' es: {resultado}")
