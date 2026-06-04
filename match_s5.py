import os
os.system("cls")

#EJERCICIOS ESTRUCTURA MATCH

#1. Calificación con letra

# calificacion = input('Ingrese su calificacion sea A,B,C,F: ')

# match calificacion:
#     case "A": 
#         print('Excelente')
#     case "B":
#         print("Bueno")
#     case "C":
#         print("Deficiente")
#     case "F":
#         print("Reprobado")
#     case _:
#         print("No ingreso ninguna de las mencionadas")

#-----------------------------------------------------------------------------

#2. Nombre del mes

# meses = int(input("Ingrese un numero del 1-12 correspondiente a los meses del año: "))

# match meses: 
#     case 1: 
#         print('Enero')
#     case 2: 
#         print('Febrero')
#     case 3: 
#         print('Marzo')
#     case 4: 
#         print('Abril')
#     case 5: 
#         print('Mayo')
#     case 6: 
#         print('Junio')
#     case 7: 
#         print('Julio')
#     case 8: 
#         print('Agosto')
#     case 9: 
#         print('Septiembre')
#     case 10: 
#         print('Octubre')
#     case 11: 
#         print('Noviembre')
#     case 12: 
#         print('Diciembre')
#     case _: 
#         ()

#-----------------------------------------------------------------------------

#3. Clasificador de grupo etario

# edad = int(input('Ingrese su edad: '))

# match edad: 
#     case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
#         print("Eres un niño")
#     case 13 | 14 | 15 | 16 | 17:
#         print("Eres un adolescente")
#     case edad if 18 <= edad <= 64:
#         print("Eres un adulto")
#     case edad if edad >= 65: 
#         print("Eres un adulto mayor")
#     case _: 
#         print() 

#-----------------------------------------------------------------------------

#4. Cálculo del Índice de Masa Corporal (IMC)

# peso_kg = float(input('Ingrese su peso en kilogramos: '))
# altura_metros = float(input('Ingrese su altura en metros: '))
# imc_calc = (peso_kg / (altura_metros ** 2 ))
# print(f"IMC es de: {imc_calc:.2f} y esta en:")

# match imc_calc:
#     case imc_calc if imc_calc < 18.5:
#         print("Bajo peso")
#     case imc_calc if 18.5  <= imc_calc <= 24.9:
#         print("Peso normal")
#     case imc_calc if 25 <= imc_calc <= 29.9:
#         print("Sobrepeso")
#     case imc_calc if imc_calc >=30: 
#         print("Obesidad")
#     case _:
#         ()

#-----------------------------------------------------------------------------


#+EJERCICIOS ESTRUCTURA MATCH

#1. Operaciones con menú interactivo

# print('''1.Sumar
# 2.Restar
# 3. Multiplicar
# 4. Dividir''')

# opcion_seleccionada = int(input('Elija una opcion: '))
# num1 = int(input('Ingrese un primer numero: '))
# num2 = int(input('Ingrese un segundo numero: '))

# match opcion_seleccionada:
#     case 1:
#         print(num1 + num2)
#     case 2:
#         print(num1 - num2)
#     case 3:
#         print(num1 * num2)
#     case 4:
#         print(num1 / num2)
#     case _:
#         print("Opcion no validad")

#-----------------------------------------------------------------------------

#2. Conversor de unidades

# opciones = int(input('''Escoja una de las siguientes opciones:
# 1→ Convertir kilómetros a metros
# 2 → Convertir metros a centímetros
# 3 → Convertir kilogramos a gramos\n'''))

# cantidad_a_convertir = float(input('Ahora ingrese una cantidad a convertir: '))

# K_A_M = (cantidad_a_convertir * (1000 / 1))
# M_A_C = (cantidad_a_convertir * (100 / 1))
# K_A_G = (cantidad_a_convertir * (1000 / 1.0))

# match opciones:
#     case 1: 
#         print(K_A_M)
#     case 2: 
#         print(M_A_C)
#     case 3: 
#         print(K_A_G)
#     case _:
#         print('Opcion no validad')


#-----------------------------------------------------------------------------

#3. Tipo de figura geométrica

# nombre_de_figura = input('''Ingrese el nombre de una figuara entre
# Triangulo, Cuadrado, Circulo\n''')

# match nombre_de_figura:
#     case "Triangulo":
#         print("Tiene 3 lados.")
#     case "Cuadrado":
#         print("Tiene 4 lados.")
#     case "Circulo":
#         print("No tiene lados.")
#     case _:
#         ("Figura no reconocida")


#-----------------------------------------------------------------------------

#4. Sistema de acceso por rol

# rol_de_usuario = input('''Ingrese su rol de usuario:
                       
# admin

# docente

# estudiante\n
# :''')

# match rol_de_usuario:
#     case "admin":
#         print("Acceso total al sistema.")
#     case "docente":
#         print("Acceso a gestión académica.")
#     case "estudiante":
#         print("Acceso a consultas y tareas.")
#     case _:
#         ("Rol no autorizado.")



