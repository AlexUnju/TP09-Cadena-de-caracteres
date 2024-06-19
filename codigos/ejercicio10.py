import random

def geringoso(cadena):
    vocales = 'aeiouAEIOU'
    silabas_geringosas = ['pa', 'pe', 'pi', 'po', 'pu']
    cadena_geringosa = ''
    
    for letra in cadena:
        cadena_geringosa += letra
        
        # Si la letra es una vocal, agregar una sílaba geringosa aleatoria
        if letra in vocales:
            silaba = random.choice(silabas_geringosas)
            cadena_geringosa += silaba
    
    return cadena_geringosa

# Ejemplo de uso
cadena_original = "Hola mundo"
resultado = geringoso(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena geringosa:", resultado)
