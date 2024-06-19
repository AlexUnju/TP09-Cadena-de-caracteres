def s_sep(cadena, car):
    lpalabras = list()
    if car in cadena:
        lpalabras = cadena.split(car)
    else:
        print('Ingreso inválido')
    return lpalabras

mensaje = '''
Ingrese un texto y luego
un caracter separador por ejm:
Texto: 1-2-3-4
Separador: -
'''
print(mensaje)

txt = input('Texto:')
separador = input('Separador:')
lista = s_sep(txt, separador)
print(lista)

#salida
'''['192', '168', '0', '1']'''

#---------------------------------------------------------

def lee_edad():
    '''Solicita una edad'''
    i = 0
    while i < 3:
        i += 1
        valor = input(f'Intento {i}, edad:')
        try:
            edad = float(valor)
            if edad <= 0.0:
                print('La edad debe ser > 0')
            else:
                return edad
        except ValueError:
            print('Dato inválido')
    print(f'Incorrecto! {i} intentos')
    return None

edad = lee_edad()
print(edad)

#salida

#caso 1: 
'''Intento 1, edad: 25 
25.0'''

#caso 2:
'''Intento 1, edad: uno
Dato inválido
Intento 2, edad: 30
30.0
'''

#caso 3:

'''Intento 1, edad: texto
Dato inválido
Intento 2, edad: palabra
Dato inválido
Intento 3, edad: palabra
Incorrecto! 3 intentos
None
'''


