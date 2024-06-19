def verificar_email(email):
    if email.count('@') == 1:
        return True
    else:
        return False

# Solicitar al usuario que ingrese la dirección de correo electrónico
direccion_email = input("Ingrese una dirección de correo electrónico: ")

# Verificar si la dirección de correo electrónico contiene un solo "@"
if verificar_email(direccion_email):
    print("La dirección de correo electrónico es válida.")
else:
    print("La dirección de correo electrónico no es válida. Debe contener exactamente un '@'.")
