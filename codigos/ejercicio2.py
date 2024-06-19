def contar_vocales1(cadena):
    contador = 0
    for letra in cadena:
        if letra.lower() in 'aeiouáéíóúü':
            contador += 1
    return contador

def contar_vocales2(texto):
    return sum(map(texto.lower().count, 'aeiouáéíóúü'))

import re
def contar_vocales3(texto):
    return len(re.findall('[aeiouáéíóúü]', texto, re.IGNORECASE))

cad = input('Ingrese una frase:') #'Pájaro de mal agüero'
print(contar_vocales1(cad))
print(contar_vocales2(cad))
print(contar_vocales3(cad))
