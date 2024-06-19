def convertir(listaExterna):
    lst = list()
    for item in listaExterna: 
        movimiento = item.split(',')
        importe = movimiento[2]
        importe = float(importe[:-2] + '.' + importe[-2:])
        movimiento[2] = importe
        lst.append(movimiento) # Agrego movimiento a la lista
    return lst    

def movimientos(lst):
    print('Lista de todos los movimientos')
    for item, mov in enumerate(lst): 
        print(item, mov)

def sumar_depositos(lst):
    print('Lista de depósitos')
    suma = 0.
    for item, mov in enumerate(lst): 
        if mov[4] == 'D':
            print(item, mov)
            suma += mov[2]
    print('Total Acumulado: ', suma)        

def movimiento_cuenta(lst):
    numeroCuenta = input('Ingrese Nro de Cuenta: ')
    existe = False

    for item, mov in enumerate(lst):
        if mov[0] == numeroCuenta:
            print(item, mov)
            existe = True
    if not existe:
        print('No existe la cuenta ingresada...')


listaExterna = ["27200123456,MARIA FERNANDEZ,0000500056,30-05-2021,E",
                "27200321654,CARLOS TORRES,0000400045,31-05-2021,D",
                "27200987125,LAURA AQUINO,0000230000,30-05-2021,D",
                "27200852369,MARTIN ESTRADA,0000700000,25-05-2021,E",
                "27200123456,MARIA FERNANDEZ,0000250099,31-05-2021,E",
                "27200795169,FLORENCIA ROBLES,0000350080,20-05-2021,D"]

cuentas = convertir(listaExterna)
movimientos(cuentas)
sumar_depositos(cuentas)
movimiento_cuenta(cuentas)
