import random
import string

# Inicio

while True:
    try:
        length = int(input("Ingrese la longitud de la contraseña: "))
        if length > 0:
            break
        else:
            print("La longitud debe ser mayor que 0.")
    except ValueError:
        print("Debe ingresar un número válido.")

# Crear conjunto de caracteres (letras, dígitos, símbolos)
characters = string.ascii_letters + string.digits + string.punctuation

# Generar contraseña aleatoria usando for
password = ""
for _ in range(length):
    password += random.choice(characters)

# Mostrar contraseña al usuario
print("Contraseña generada:", password)

# Fin