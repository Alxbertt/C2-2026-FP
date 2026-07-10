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

#--------------------------------------------------------------------------------

#Ejercicios funciones 2 y validar contraseña mediante funcion con una funcion main() que no contenga la logica de negocio

# def main():
#     edad = int(input('''!Bienvenido, verifiquemos su edad...
# Ingresar edad: ''')) 
    
#     print(f"De acuerdo a su edad usted es un: {clasificar_edad(edad)}")

#     password = input('Ingrese una contraseña: ')

#     print(validar_password(password))


#logica de negocio:

# def clasificar_edad(edad): 
#     if edad <= 12:
#         return "niño"
#     elif 13 <= edad <= 18:
#         return "adolescente"
#     else:
#         return "adulto"

#validar contraseña mediante funcion

# def validar_password (password):
#     min_8_caracteres = False
#     al_menos_un_caracter_numerico = False
#     al_menos_un_caracter_alfabetico_en_mayuscula = False
#     al_menos_un_caracter_alfabetico_en_minuscula = False

#     if len(password) >= 8: 
#         min_8_caracteres = True 
#     for caracter_de_contrasenia in password:
#         if caracter_de_contrasenia.isdigit():
#             al_menos_un_caracter_numerico = True

#         if caracter_de_contrasenia.isupper():
#             al_menos_un_caracter_alfabetico_en_mayuscula = True 
            
#         if caracter_de_contrasenia.islower():
#             al_menos_un_caracter_alfabetico_en_minuscula = True

#     if (min_8_caracteres
#          and al_menos_un_caracter_alfabetico_en_minuscula
#          and al_menos_un_caracter_alfabetico_en_mayuscula 
#          and al_menos_un_caracter_numerico):
        
#         return "Contraseña Valida!!!"
#     else: 
#         return "Contraseña invalida"
    
#llamada de la logica de negocio:
# main()

#--------------------------------------------------------------------------------
#EJERCICIOS FUNCIONES 3

# def main():
#     numero_limite_a_sumar = int(input("Ingrese un número para calcular la suma desde 1 hasta ese número: "))
#     resultado_suma = suma_hasta_n(numero_limite_a_sumar)

#     print(f"La suma desde 1 hasta {numero_limite_a_sumar} es: {resultado_suma}")

#     numero_a_multiplicar = int(input("Ingrese un número para generar su tabla de multiplicar: "))

#     tabla_de_multiplicar(numero_a_multiplicar)


# def suma_hasta_n(numero_limite_a_sumar):
#     acumulador = 0

#     for i in range(1, numero_limite_a_sumar + 1):
#         acumulador += i

#     return acumulador


# def tabla_de_multiplicar(numero_a_multiplicar):
#     for i in range(1, 11):
#         resultado = numero_a_multiplicar * i
#         print(f"{numero_a_multiplicar} x {i} = {resultado}")
# main()