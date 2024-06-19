'''3. Analizar, ejecutar y mejorar el siguiente código.
'''
import random

def bienvenida(mensaje):
    bienv_inp = ['hola', 'buenas', 'que tal', 'hi', 'buenos', 'buen', 'todo']
    bienv_out = [
        'Hola, ¿cómo estás?',
        'Hola, ¿qué tal?',
        'Hola, ¿te puedo ayudar?',
        'Hola, encantado de comunicarme contigo',
        'Hola, espero que estés bien!'
    ]
    
    # Convertir el mensaje a minúsculas para hacer la comparación
    palabras = mensaje.lower().split()
    
    for palabra in palabras:
        if palabra in bienv_inp:
            return random.choice(bienv_out)
    
    # Si ninguna palabra de saludo esperada está presente
    return 'Tu mensaje no está en mi base de datos'

# Preguntar al usuario por el saludo
cad = input('Soy un robot, salúdame por favor: ')

# Mostrar la respuesta de bienvenida
print(bienvenida(cad))




#-----------------------------------------------------------------------

import random

def bienvenida(mensaje):
    bienv_inp = ['hola', 'buenas', 'que', 'hi', 'hey', 'buen', 'todo']
    bienv_out = [
        'Hola, ¿cómo estás?',
        'Hola, ¿qué tal?',
        'Hola, ¿te puedo ayudar?',
        'Hola, encantado de comunicarme contigo',
        'Hola, espero que estés bien!',
        '¡Hola! ¿Cómo puedo ayudarte?',
        '¡Hey! ¿Qué tal?',
        '¡Hola! ¿Qué hay de nuevo?',
        '¡Hola! ¿Cómo te va?',
        '¡Hola! ¿Listo para comenzar?'
    ]
    
    # Convertir el mensaje a minúsculas para hacer la comparación
    palabras = mensaje.lower().split()
    
    for palabra in palabras:
        if palabra in bienv_inp:
            return random.choice(bienv_out)
    
    # Si ninguna palabra de saludo esperada está presente
    return 'Lo siento, no entendí tu saludo. ¿Puedes decir "Hola" o algo similar?'

# Preguntar al usuario por el saludo
cad = input('Soy un robot, salúdame por favor: ')  # Por ejemplo: Hola robot

# Mostrar la respuesta de bienvenida
print(bienvenida(cad))
