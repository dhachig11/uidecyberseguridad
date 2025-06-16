<# uidecyberseguridad
Repositorio Diego Hachig
=========================================================================================
Aprendizaje Autonomo 2
Paso 1: Inicio del Desarrollo de Software / Configuración del Entorno - Entrega:

a) Link del repositorio en GitHub con la aplicación.
https://github.com/dhachig11/uidecyberseguridad
b) Diagramas de flujo cargados en el repositorio.
FLUJO LOGICO
Inicio
  ↓
Pedir longitud de la contraseña
  ↓
Validar que la longitud sea un número válido (>0)
  ↓
Importar módulos (random, string)
  ↓
Crear conjunto de caracteres (letras, dígitos, símbolos)
  ↓
Generar contraseña aleatoria
  ↓
Mostrar contraseña al usuario
  ↓
Fin
=========================================================================================
c) Generador de Contraseñas Básico en Python
  1.  Funciones del programa:
  2.  Solicita al usuario la longitud de la contraseña.
  3.  Usa letras, números y símbolos.
  4.  Genera la contraseña aleatoriamente.
  5.  Muestra la contraseña generada.
d) Avance del código cargado en GitHub.
    # Definir manualmente el conjunto de caracteres
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
    characters = letters + digits + symbols
    # Función simple para obtener un número pseudoaleatorio
    def simple_random(seed):
    # Algoritmo congruencial lineal básico
    a = 1664525
    c = 1013904223
    m = 2**32
    return (a * seed + c) % m
    # Obtener longitud válida usando while
    while True:
        try:
            length = int(input("Ingrese la longitud de la contraseña: "))
            if length > 0:
                break
            else:
                print("La longitud debe ser mayor que 0.")
        except ValueError:
            print("Debe ingresar un número válido.")
=========================================================================================
d) Video explicativo del proceso desarrollado hasta este punto máximo 2 min
Paso 2: Desarrollo del Programa Seleccionado - Entrega
a) Video explicativo del avance máximo 2 min.
b) Video demostrativo de las funcionalidades implementadas máximo 2 min
=========================================================================================
c) Código actualizado y cargado en el repositorio de GitHub.
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
=========================================================================================
#>


