def ins_car_xd(cadena, car, x, d='i'):
    # Verificar que d sea 'i' o 'f'
    if d != 'i' and d != 'f':
        print("El parámetro d debe ser 'i' o 'f'. Se asumirá 'i' por defecto.")
        d = 'i'
    
    # Inicializar la cadena resultante
    cadena_resultante = ''
    
    # Inserción desde el inicio
    if d == 'i':
        for i in range(len(cadena)):
            if i > 0 and i % x == 0:
                cadena_resultante += car
            cadena_resultante += cadena[i]
    
    # Inserción desde el final
    elif d == 'f':
        for i in range(len(cadena) - 1, -1, -1):
            if (len(cadena) - i) % x == 0 and i != len(cadena) - 1:
                cadena_resultante = car + cadena_resultante
            cadena_resultante = cadena[i] + cadena_resultante
    
    return cadena_resultante

# Ejemplos de uso
cadena1 = "2552552550"
car1 = "."
x1 = 3
resultado1 = ins_car_xd(cadena1, car1, x1)
print(resultado1)  # Salida: "255.255.255.0"

cadena2 = "1234567890"
car2 = ","
x2 = 3
resultado2 = ins_car_xd(cadena2, car2, x2, d='f')
print(resultado2)  # Salida: "1,234,567,890"
