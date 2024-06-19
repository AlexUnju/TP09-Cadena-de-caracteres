import random

# Inicialización de la lista de estudiantes para pruebas
estudiantes = [
    ['12345678', 'Clave123', 'Juan Pérez', 'juan@example.com', '388-1234567'],
    ['23456789', 'Password1', 'María López', 'maria@example.com', '388-2345678'],
    ['34567890', 'SecurePass2', 'Pedro Gómez', 'pedro@example.com', '388-3456789'],
    ['45678901', 'StrongPass3', 'Ana Martínez', 'ana@example.com', '388-4567890'],
    ['56789012', 'Secret123', 'Luis Rodríguez', 'luis@example.com', '3886-5678901'],
    ['67890123', 'SuperPass4', 'Laura Sánchez', 'laura@example.com', '3886-6789012'],
    ['78901234', 'TopSecret5', 'Mariano Pérez', 'mariano@example.com', '3887-7890123'],
    ['89012345', 'Hidden678', 'Carolina López', 'carolina@example.com', '3888-8901234'],
    ['90123456', 'UltraPass6', 'Lucas González', 'lucas@example.com', '3888-9012345'],
    ['01234567', 'MegaPass7', 'Julieta Fernández', 'julieta@example.com', '3888-0123456']
]

# Función para verificar si un DNI ya está registrado
def dni_existe(dni):
    for estudiante in estudiantes:
        if estudiante[0] == dni:
            return True
    return False

# Función para validar el formato del DNI
def validar_dni(dni):
    if len(dni) != 8 or not dni.isdigit():
        return False
    return True

# Función para validar la clave
def validar_clave(clave):
    if len(clave) < 6:
        return False
    tiene_mayuscula = False
    tiene_numero = False
    for c in clave:
        if c.isupper():
            tiene_mayuscula = True
        if c.isdigit():
            tiene_numero = True
    return tiene_mayuscula and tiene_numero

# Función para validar el nombre
def validar_nombre(nombre):
    if len(nombre) < 3:
        return False
    for c in nombre:
        if not c.isalpha() and c != ' ':
            return False
    return True

# Función para validar el correo electrónico
def validar_email(email):
    if '@' not in email or email.startswith('@') or email.endswith('@'):
        return False
    return True

# Función para validar el número de celular
def validar_celular(celular):
    if '-' not in celular:
        return False
    codigo_area, numero = celular.split('-')
    if codigo_area not in ['388', '3886', '3887', '3888']:
        return False
    if len(numero) != 7 or not numero.isdigit():
        return False
    return True

# Función para registrar un estudiante nuevo
def registrar_estudiante():
    print("Registro de nuevo estudiante:")
    dni = input("DNI (8 dígitos numéricos): ")
    while not validar_dni(dni) or dni_existe(dni):
        print("DNI inválido o ya registrado. Intente nuevamente.")
        dni = input("DNI (8 dígitos numéricos): ")
    
    clave = input("Clave (mínimo 6 caracteres, al menos una mayúscula y un número): ")
    while not validar_clave(clave):
        print("Clave inválida. Intente nuevamente.")
        clave = input("Clave: ")
    
    nombre = input("Nombre (sin números ni caracteres especiales, al menos 3 caracteres): ")
    while not validar_nombre(nombre):
        print("Nombre inválido. Intente nuevamente.")
        nombre = input("Nombre: ")
    
    email = input("Correo electrónico (debe contener '@' y no empezar ni terminar con '@'): ")
    while not validar_email(email):
        print("Correo electrónico inválido. Intente nuevamente.")
        email = input("Correo electrónico: ")
    
    celular = input("Número de celular (código de área-guion-número, ej: 388-1234567): ")
    while not validar_celular(celular):
        print("Número de celular inválido. Intente nuevamente.")
        celular = input("Número de celular: ")
    
    # Agregar el estudiante a la lista de estudiantes
    estudiantes.append([dni, clave, nombre, email, celular])
    print("\nEstudiante registrado exitosamente.\n")

# Función para buscar estudiantes por nombre
def buscar_estudiante_por_nombre(nombre_buscar):
    if nombre_buscar == '':
        print("\nListado completo de estudiantes:")
        for estudiante in estudiantes:
            print(f"DNI: {estudiante[0]}, Nombre: {estudiante[2]}, Email: {estudiante[3]}")
    else:
        print(f"\nEstudiantes cuyo nombre contiene '{nombre_buscar}':")
        encontrados = False
        for estudiante in estudiantes:
            if nombre_buscar.lower() in estudiante[2].lower():
                print(f"DNI: {estudiante[0]}, Nombre: {estudiante[2]}, Email: {estudiante[3]}")
                encontrados = True
        if not encontrados:
            print(f"No se encontraron estudiantes cuyo nombre contenga '{nombre_buscar}'.")
    print()

# Función para realizar el login
def login():
    dni = input("Ingrese su DNI: ")
    clave = input("Ingrese su clave: ")
    encontrado = False
    for estudiante in estudiantes:
        if estudiante[0] == dni and estudiante[1] == clave:
            print("\nIngreso exitoso.")
            print(f"Nombre: {estudiante[2]}, Email: {estudiante[3]}\n")
            encontrado = True
            break
    if not encontrado:
        print("\nUsuario o clave incorrectos.\n")

# Ejecución del programa
while True:
    print("\nBienvenido al sistema de registro de estudiantes\n")
    print("1. Registrar nuevo estudiante")
    print("2. Buscar estudiante por nombre")
    print("3. Ingresar (Login)")
    print("4. Salir")
    
    opcion = input("Ingrese la opción deseada: ")
    
    if opcion == '1':
        registrar_estudiante()
    elif opcion == '2':
        nombre_buscar = input("Ingrese el nombre del estudiante a buscar (deje vacío para listar todos): ")
        buscar_estudiante_por_nombre(nombre_buscar)
    elif opcion == '3':
        login()
    elif opcion == '4':
        print("\nGracias por utilizar el sistema. ¡Hasta luego!")
        break
    else:
        print("\nOpción inválida. Intente nuevamente.\n")
