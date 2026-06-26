import os 
os.system("cls")

#Ejercicios clse ciclos 

#Usando While
#Imprimir los números múltiplos de 3 entre 9 y el 66 usando while.

# numero = 9

# while numero <= 66:
#     print(numero)
#     numero += 3
#-------------------------------------------------------------------

#imprimir los números del 8 al 4 usando while.

# numero = 8 

# while numero >= 4:
#     print(numero)
#     numero -= 1
#-------------------------------------------------------------------

#Usando For

#Generar los números entre el 1 y el 50. A los números pares incluidos entre ellos sumarle 3 e imprimirlos. A los impares multiplicarlos por 2 e imprimirlos

# for numeros in range(1,51): 
#     print(f"{numeros}")
#     if numeros % 2 == 0: 
#         print(f"{numeros} es par, + 3 es igual a: {numeros + 3}")
#     elif numeros % 2 != 0:
#         print(f"{numeros} es impar, multiplicado por 2 es igual a: {numeros * 2}")

#-------------------------------------------------------------------

#Imprimir las letras de tu nombre completo.
# nombre = "Albert Emmanuel Hichez Perez"

# for letras in nombre: 
#     print(letras)

#-------------------------------------------------------------------

#Pide números al usuario y muéstralos hasta que se introduzca un número negativo. Usa break para lograrlo

# for i in range(1000000):
#     numeros_ingresados = int(input('Ingrese los nuemros positivos que desea: '))
#     if numeros_ingresados < 0:
#         print("El numero ingresado es negativo cerrando programa...")
#         break
#     else:
#         print(f"El numero ingresado es {numeros_ingresados}")

#-------------------------------------------------------------------

#Imprime los números del 1 al 20, excepto los que  terminen en 4. Usa continue para lograrlo.

# for i in range(1, 21): 
#     if i % 10 == 4: 
#         continue
#     print(i)

#-------------------------------------------------------------------
#EJERCICIOS CONTADORES, ACUMULADORES, BANDERA
#-------------------------------------------------------------------

#1. Introducir 5 números y contar los números pares. Mostrar al usuario la cantidad de numeros pares que se ingresaron

# cantidad_pares = 0

# for i in range(5):
#     numero = int(input('Ingrese un número: '))
#     if numero % 2 == 0:
#         cantidad_pares += 1

# print(f'Se ingresaron {cantidad_pares} números pares.')

#-------------------------------------------------------------------

#2. Haz un programa que solicite al usuario una cantidad n de números a ingresar. Luego, pide los n números y cuenta cuántos son menores que cero. Muestra el total de números negativos al final.

# n_numeros = int(input("¿Cuántos números desea ingresar? "))

# contador_De_numeros_negativos = 0

# for i in range(n_numeros):
#     numero = int(input("Ingrese un número: "))

#     if numero < 0:
#         contador_De_numeros_negativos += 1

# print("Cantidad de números negativos:", contador_De_numeros_negativos)

#-------------------------------------------------------------------

#3. Haz un programa que pida las edades de varias personas. El usuario debe indicar cuántas edades ingresará. El programa debe contar cuántas personas son mayores de edad (18 años o más).

# numero_de_edades_a_ingresar = int(input('Cuantas edades desea ingresar? '))
# n_edades_mayores_18 = 0

# for cantidad in range(numero_de_edades_a_ingresar):
#     edad_ingresada = int(input('Ingrese una edad: '))
    
#     if edad_ingresada >= 18:
#         n_edades_mayores_18 += 1
# print(f"Hay {n_edades_mayores_18} personas mayores de edad")

#-------------------------------------------------------------------

#Programas con acumulador:

#4. Introducir 5 números y sumar los números pares. Mostrar la usuario la sumatoria de numeros pares que se ingresaron

# numeros_ingresados = 5
# sumas_pares = 0 

# for i in range(numeros_ingresados):
#     numero_ingresado = int(input(f'Ingrese un numero: '))
#     if numero_ingresado  % 2 == 0:
#         sumas_pares = sumas_pares + numero_ingresado

# print(f"La sumatoria de los numeros pares ingresados previamente da como resultado: {sumas_pares}")
        
#-------------------------------------------------------------------

#5. Pide al usuario que introduzca el precio de varios productos uno por uno. El programa debe preguntar después de cada entrada si desea agregar otro producto. Al finalizar, muestra la suma total de los precios.

# suma_productos = 0
# otro_agregado = "si"

# while otro_agregado == "si":
#     precios_de_productos = float(input("Introduzca el precio de un productos: "))
#     suma_productos += precios_de_productos

#     otro_agregado = input('Desea agregar otro producto: si/no: ')
# print(f"Total a pagar: {suma_productos}")

#-------------------------------------------------------------------

#Programas con bandera:

#6. Introducir 5 números y detener el programa si se ha introducido algún número par. Mostrar al usuario un mensaje diciendo lo que ha pasado.

# cantidad_de_n_a_ingresar = 5
# encontro_n_par = False

# for numeros in range(cantidad_de_n_a_ingresar):
#     n = int(input('Favor introducir un numero: '))

#     if n % 2 == 0:
#         encontro_n_par = True
#         print("Programa detenido devido al ingreso de un numero par")
#         break

# if encontro_n_par == False: 
#     print("No se ingresó ningún número par")

#-------------------------------------------------------------------

#7. Realiza un programa que pida al usuario números enteros de uno en uno. El ciclo debe continuar hasta que el usuario escriba el número 0. Por cada número ingresado, muestra un mensaje indicando que el número fue recibido.

# numero_cero_encontrado = False
# numero_ingresado = 1

# while numero_ingresado != 0:
#     numero_ingresado = int(input('Ingrese un numero entero: '))
    
#     if numero_ingresado != 0:
#         print("Numero recibido")
        
# if numero_ingresado == 0:
#     numero_cero_encontrado = True
#     print("Numero cero detectado cerrando programa...")

#-------------------------------------------------------------------

#8. Escribe un programa que permita al usuario ingresar números positivos. El ciclo debe repetirse mientras la suma total sea menor que 100. Al finalizar, muestra la suma total alcanzada.

# sumador_de_ingresados = 0

# while sumador_de_ingresados < 100:
#     ingreso_de_numero = int(input("Ingrese un numero: "))
#     sumador_de_ingresados += ingreso_de_numero
# print(sumador_de_ingresados)      
                          
#-------------------------------------------------------------------
#+EJERCICIOS CICLOS
#-------------------------------------------------------------------

#1.while
# nombre = input('Ingrese su nombre: ')
# edad = int(input('Ingrese su edad: '))
# numero_de_repeticiones = 0

# while numero_de_repeticiones < edad:
#     print(f'Hola {nombre} como estas?')
#     numero_de_repeticiones += 1
#-------------------------------------------------------------------
#1.for
# nombre = input('Ingrese su nombre: ')
# edad = int(input('Ingrese su edad: '))

# for i in range(edad):
#     print(f'Hola {nombre} como estas?')

#-------------------------------------------------------------------

#2.While
# nombre = input('Ingrese su nombre: ')
# edad = int(input('Ingrese su edad: '))
# contador = 0


# if edad > 18:
#     while contador < edad:
#         print("Estudia en ITLA")
#         contador +=1
# else: 
#     while contador < 5:
#         print("Estudia en ITLA")
#         contador +=1

#-------------------------------------------------------------------

#2.for 
# nombre = input('Ingrese su nombre: ')
# edad = int(input('Ingrese su edad: '))


# if edad > 18:
#     for i in range(edad):
#         print("Estudia en ITLA")
# else: 
#    for i in range(5):
#         print("Estudia en ITLA")
#-------------------------------------------------------------------

#3.while
# n = int(input('ingrese un numero: '))
# contador = 1

# if n == 0:
#     print('No se permite este nuemro, cerrando programa...')
# else:
#     while contador <= n:
#         print(contador)
#         contador += 1

#-------------------------------------------------------------------
#3.For
# n = int(input('ingrese un numero: '))

# if n == 0:
#     print('No se permite este nuemro, cerrando programa...')
# else:
#     for i in range(1, n + 1):
#         print(i)
#-------------------------------------------------------------------

#4.While
# nombre = input('Ingrese su nombre: ')
# edad = int(input('Ingrese su edad: '))
# nacionalidad = input('Ingrese su nacionalidad: ')
# adivinansa = 0

# contador = 0
# limite_5 = 5
# suma = 0

# triple_de_repeticiones = edad * 3
# numero_secreto = 3
# contador_de_intentos = 0

# if edad >= 18 and nacionalidad == "dominicana":
#         while contador < limite_5:
#             solicitud_de_5_numeros = int(input('Ingrese un numero: '))
#             suma += solicitud_de_5_numeros
#             contador += 1
#         print(suma)
# elif edad >= 18 and nacionalidad != "dominicana":
#       while edad > contador: 
#             contador += 1
#             print('Visita RD')
# elif edad < 18 and nacionalidad == "dominicana":
#       while contador < triple_de_repeticiones:
#             contador += 1
#             print('Espera a crecer')
# elif edad < 18 and nacionalidad != "dominicana":
#       while adivinansa != numero_secreto:
#             adivinansa = int(input('Adivine un numero secreto del 1 al 10: '))
#             contador_de_intentos += 1
#       print(f"Felicidades lo logro, el numero de intentos fue de:{contador_de_intentos}")

#-------------------------------------------------------------------

#4.for
# nombre = input('Ingrese su nombre: ')
# edad = int(input('Ingrese su edad: '))
# nacionalidad = input('Ingrese su nacionalidad: ')

# sumatoria = 0
# triple_de_repeticiones = edad * 3
# numero_secreto = 3
# contador_intentos = 0

# if edad >= 18 and nacionalidad == "dominicana":
#       for solicitud_numeros in range(5):
#             solicitud = int(input('Ingrese un numero: '))
#             sumatoria += solicitud
#       print(sumatoria)
# elif edad >= 18 and nacionalidad != "dominicana":
#       for numero in range(edad):
#             print("Visita RD")
# elif edad < 18 and nacionalidad == "dominicana":
#       for triple_de_edad in range(triple_de_repeticiones):
#             print('Espera a crecer')    
# elif edad < 18 and nacionalidad != "dominicana":
#       for i in range(1, 11):
#             contador_intentos +=1
#             adivinanza = int(input('Adivine un numero secreto del 1 al 10: '))
            
#             if adivinanza == numero_secreto:
#                   print(f"Felicidades lo logro, el numero de intentos fue de:{contador_intentos}")
#                   break

#-------------------------------------------------------------------
#ASIGNACION #3 (Válida hasta el martes 30/06/2026)
#-------------------------------------------------------------------

#Ejercicio 1 – Registro de notas 

# suma_notas = 0
# cantidad_de_notas_ingresadas = 0
# cantidad_de_notas_igual_o_mayores_a_70 = 0

# nota = int(input('Ingrese sus notas, -1 para finalizar el programa: '))

# while nota != -1:

#     suma_notas += nota
#     cantidad_de_notas_ingresadas += 1

#     if nota >= 70:
#         cantidad_de_notas_igual_o_mayores_a_70 += 1

#     nota = int(input('Ingrese sus notas, -1 para finalizar el programa: '))

# print('Cerrando programa...')

# if cantidad_de_notas_ingresadas > 0:
#     print(f'El promedio fue de: {suma_notas / cantidad_de_notas_ingresadas}')

# print(f'Cantidad de notas mayores o iguales a 70: {cantidad_de_notas_igual_o_mayores_a_70}')

#--------------------------------------------------------------------------------------------------------

#Ejercicio 2 – Tabla de multiplicar personalizada (Para ser realizado con ciclo for)

# numero_ingresado = int(input('Favor introducir un numero: '))
# contador_par = 0
# contador_impar = 0
# resultado = 0

# for i in range(1,13):
#    resultado = numero_ingresado * i
#    print(f"{numero_ingresado} x {i} = {resultado}")
#    if resultado % 2 == 0:
#     contador_par += 1
#    else: 
#      contador_impar += 1
# print(f"Hubieron {contador_par} numeros pares")
# print(f"Hubieron {contador_impar} numeros impares")

#--------------------------------------------------------------------------------------------------------

#3 Validacion de contraseña con intentos limitados

# password = 2026
# intentos = 0 
# acceso = False 
# ingreso_password = 0

# while intentos < 3:
#     ingreso_password = int(input('Ingrese la contraseaña: '))
#     intentos += 1

#     if password == ingreso_password:
#         acceso = True

#     if acceso:
#       print('Acceso concedido')
#       break
# if not acceso:
#     print('Acceso bloqueado')

#--------------------------------------------------------------------------------------------------------

#4 Suma de numeros pares en un rango 

# n_inicial = int(input('Ingrese un numero inicial: '))
# n_final = int(input('Ingrese un numero final: '))
# acumulador_par = 0

# for i in range(n_inicial, n_final +1):
#     print(i)

#     if i % 2 != 0:
#         continue
#     acumulador_par += i

# print(f"La suma de los numeros pares da como resultado {acumulador_par}")

#--------------------------------------------------------------------------------------------------------

#Ejercicio 5 – Análisis de números ingresados 

# numero = 1
# contador_par = 0
# contador_impar = 0
# numero_mayor_100 = False

# while numero != 0:
#     numero = int(input('Ingrese un número positivo (0 para cerrar el programa): '))

#     if numero == 0:
#         break

#     if numero % 2 == 0:
#         contador_par += 1
#     else:
#         contador_impar += 1

#     if numero > 100:
#         numero_mayor_100 = True

# if numero_mayor_100:
#     print('Algún número mayor a 100 fue ingresado ✅')
# else:
#     print('No se ingresó ningún número mayor a 100 ❌')

# print(f'La cantidad de números pares fue de: {contador_par}')
# print(f'La cantidad de números impares fue de: {contador_impar}')