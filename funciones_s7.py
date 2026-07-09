import os 
os.system('cls')

#Ejercicios de Funciones

#Crear una función bienvenida() que imprima un saludo genérico.
# def bienvenida():
#     print('Hola bienvenido ?')
# bienvenida()

#--------------------------------------------------------------------------------
#Crear una función cuadrado(numero) que reciba un número y retorne su cuadrado.

# num = int(input('Ingrese un numero: '))
# def cuadrado(num):
#     return num ** 2
# print(f"El cuadrado de este numero es: {cuadrado(num)}")

#--------------------------------------------------------------------------------
#Crear una función es_par(num) que devuelva True si el número es par.

# def es_par(num):
#     return num % 2 == 0
# print(f"Es par ? {es_par(num)}")

#--------------------------------------------------------------------------------

#Ejercicio 2

#--------------------------------------------------------------------------------
#Crear una función area_rectangulo(base, altura) que devuelva el área.

# print('Hey bienvenido al programa!')
# base = int(input('Ingrese la base para calcular el area: '))
# altura = int(input('Ingrese la altura para calcular el area: '))

# def area_rectangulo(base, altura):
#     return base * altura
# print(f"El area es igual a: {area_rectangulo(base, altura)}")

#--------------------------------------------------------------------------------
#Crear una función convertir_a_fahrenheit(celsius) que convierta grados.

# print('Ahora trabajemos con la temperatura de celcius a fahrenheit')

# celcius = int(input('Ingrese la temperatura a convertir (celcius): '))
# def convertir_a_fahrenheit(celcius):
#     return celcius * (9/5) + 32
# print(f"{convertir_a_fahrenheit(celcius)}")

#--------------------------------------------------------------------------------
#Crear una función es_economico(precio) que retorne True si la el precio es menor que 1000. Mostrar un mensaje en consecuencia, donde se este llamando la funcion

# print('Bien ahora verifiquemos si el precio de algo es economico')

# precio = int(input('Ingrese el precio aqui: '))

# def es_economico(precio):
#     return precio < 1000

# if es_economico(precio):
#     print('Es economico ✅')
# else: 
#     print('No es economico ❌ ')