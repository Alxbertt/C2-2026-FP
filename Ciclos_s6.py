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

#-------------------------------------------------------------------
#Practica #3 en clase en vivo (Válida hasta el martes 29/06/2026)
#-------------------------------------------------------------------

# Ejercicio 1 — Control de Acceso a un Concierto

# Contexto
# Un promotor de eventos necesita un programa para registrar la entrada de asistentes a un concierto y detectar si hubo menores de edad.

# El programa debe pedir, repetidamente, la edad de cada asistente que va entrando.

# El registro termina cuando ocurra primero una de estas dos condiciones:

# El usuario ingresa -1 (significa que ya no entran más asistentes), o
# Ya se registraron 10 asistentes (el concierto alcanzó su cupo de prueba para esta simulación).
# Mientras se registran los asistentes, el programa debe:

# Llevar un contador de cuántos asistentes se han registrado (sin contar el -1).
# Llevar un acumulador con la suma de todas las edades registradas, para calcular el promedio al final.
# Mantener una bandera que se active si en algún momento se registra un asistente con edad menor a 18 años.
# Al finalizar el registro, el programa debe imprimir:

# Cuántos asistentes se registraron en total.
# El promedio de edad de los asistentes registrados (si no se registró ninguno, evita la división entre cero y muestra un mensaje indicándolo).
# Si la bandera de menores de edad quedó activada, imprime: "Alerta: se detectaron asistentes menores de edad." En caso contrario, imprime: "Ningún asistente menor de edad detectado."
# Si el registro terminó porque se llegó al cupo de 10 (no porque el usuario escribió -1), imprime adicionalmente: "Cupo de prueba alcanzado."
# Estructuras requeridas (obligatorias): while · break · contador · acumulador · bandera

# Pregunta reflexiva
# ¿Por qué la condición del while no fue suficiente para resolver este ejercicio y fue necesario usar break? ¿Qué hubiera pasado si solo usabas while entrada != -1: sin nada más?


# contador_asistentes = 0
# acumulador_edades = 0
# hay_menor_de_edad = False
# edad = 0

# while edad != -1 and contador_asistentes < 10:
#     edad = int(input('Hey bienvenido al concierto!, favor ingresar su edad: '))

#     if edad == -1:
#         break
#     contador_asistentes += 1
#     acumulador_edades += edad
#     if edad < 18:
#         hay_menor_de_edad = True

#     if contador_asistentes == 10:
#         print("El concierto alcanzó su cupo de prueba para esta simulación.")
#         break
# print(f"La cantidad total de asistentes fue de {contador_asistentes}") 

# if contador_asistentes > 0:  
#     promedio_de_edades = acumulador_edades / contador_asistentes
#     print(f"La media de edades que asistieron fue de: {promedio_de_edades:.2f}") 

#     if hay_menor_de_edad:
#         print("Alerta: se detectaron asistentes menores de edad.") 
#     else: 
#         print('Ningún asistente menor de edad detectado.')
# else:
#     print('No hubo asistentes registrados')

#--------------------------------------------------------------------------

# Ejercicio 2 — Procesamiento de Ventas Diarias

# Contexto
# Una pequeña tienda quiere registrar las ventas de los 6 turnos de hoy. El cajero digita el monto de cada turno a medida que el programa lo pide. A veces el cajero se equivoca y digita el monto como negativo; esos montos son inválidos y no deben contarse como venta real (pero sí deben quedar contados como errores).

# El programa debe solicitar exactamente 6 montos de venta, uno por uno.

# Para cada venta ingresada:

# Si la venta es negativa, no debe sumarse ni contarse como válida, pero sí debe incrementar un contador de ventas inválidas.
# Si la venta es válida (≥ 0):
# Debe sumarse a un acumulador del total de ventas válidas.
# Debe incrementar un contador de ventas válidas.
# Si la venta es mayor a RD$1000, debe incrementar además un contador de "ventas grandes".
# Debe mantenerse una bandera que se active apenas se detecte la primera venta inválida en todo el recorrido.
# Al finalizar las 6 solicitudes, el programa debe imprimir, en este orden:

# Cantidad de ventas válidas.
# Total acumulado de ventas válidas.
# Cantidad de ventas grandes (mayores a RD$1000).
# Cantidad de ventas inválidas detectadas.
# Si la bandera quedó activada: "Se detectaron errores de digitación en el registro de ventas." Si no: "No se detectaron errores en el registro de ventas."
# Estructuras requeridas (obligatorias): for con range() · continue · dos contadores distintos · acumulador · bandera

# Pregunta reflexiva
# Si en vez de continue hubieras usado un if que envuelve todo el resto del cuerpo del ciclo (sin continue), ¿el resultado final habría sido el mismo? ¿Qué ventaja real (no solo de estilo) tiene usar continue aquí?

# contador_de_ventas_validas = 0
# contador_de_ventas_invalidas = 0
# contador_de_ventas_grandes = 0
# acumulador_del_total_de_ventas_validas = 0
# por_lo_menos_una_venta_invalida = False 

# for una_venta in range(1, 6 + 1):
#     monto_de_venta = int(input('Ingrese el monto de la venta: '))
#     if monto_de_venta < 0:
#         contador_de_ventas_invalidas += 1
#         por_lo_menos_una_venta_invalida = True
#         continue
#     else: 
#         contador_de_ventas_validas += 1
#         acumulador_del_total_de_ventas_validas += monto_de_venta

#     if monto_de_venta > 1000:
#         contador_de_ventas_grandes += 1


# print(f'Ventas validas: {contador_de_ventas_validas}')
# print(f'TOTAL de ventas validas: {acumulador_del_total_de_ventas_validas}')
# print(f'Ventas grandes: {contador_de_ventas_grandes}')
# print(f'Ventas invalidas: {contador_de_ventas_invalidas} ')

# if por_lo_menos_una_venta_invalida:
#     print('Se detectaron errores de digitación en el registro de ventas.')
# else:
#     print("No se detectaron errores en el registro de ventas.")