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

#-----------------------------------------------------------------------------

#ASIGNACION #2 (5PTS. FECHA LIMITE: 15/06/2026)

#Ejercicio 1 – Impuesto progresivo

# ingreso_mensual = int(input("Cual es su ingreso mensual? "))

# if ingreso_mensual > 0:
#     if ingreso_mensual <= 20000:
#         print('Exento')
#     elif 20001 <= ingreso_mensual <= 40000:
#         print(f"Se le calcula 10% de impuesto: {ingreso_mensual * 0.10}")
#     else:
#         print(f"Se le calcula 20% de impuesto: {ingreso_mensual * 0.20}")
# else:
#     print('El ingreso debe ser mayor a 0')

#-----------------------------------------------------------------------------

#Ejercicio 2 – Plan telefónico

# plan_telefonico = input('Ingrese el tipo de plan deseado: Basico, Estandar o Premium\n')

# match plan_telefonico:
#     case "Basico": print('''El plan basico tiene un costo de: RD$500
# beneficios: 5 GB de internet, 100 minutos de llamadas y 100 SMS.''')
#     case "Estandar": print('''El plan basico tiene un costo de: RD$900
# beneficios: 15 GB de internet, llamadas ilimitadas nacionales y 500 SMS.''')
#     case "Premium":  print('''El plan basico tiene un costo de: RD$1,500
# beneficios: Internet ilimitado, llamadas ilimitadas nacionales e internacionales y SMS ilimitados.''')
#     case _:
#         print("El plan no existe, favor de ingresar uno valido")
        
#-----------------------------------------------------------------------------

#Ejercicio 3 – Mayor de tres números

# num1 = int(input('Ingrese un primer numero: '))
# num2 = int(input('Ingrese un segundo numero: '))
# num3 = int(input('Ingrese un tercer numero: '))
# resultado = (num1 + num2 + num3) % 2
# suma = num1 + num2 + num3

# if num1 > num2 and num1 > num3:
#     print('El primer número es mayor que los demás')
# elif num2 > num1 and num2 > num3:
#     print('El segundo número es mayor que los demás')
# elif num3 > num1 and num3 > num2:
#     print('El tercer número es mayor que los demás')

# if num1 == num2 == num3:
#     print('Todos son iguales')
# elif num1 == num2 or num2 == num3 or num1 == num3:
#     print('Hay empate de dos números iguales')

# if resultado != 0: 
#     print(f'La suma de los 3 numeros es: {suma}')

#-----------------------------------------------------------------------------

#Ejercicio 4 – Validación de contraseña

# contraseña = input('Ingrese una contraseña: ')
# tiene_numero = False 
# tiene_mayuscula = False 

# for caracter in contraseña: 
#     if caracter.isdigit():
#         tiene_numero = True
#     elif caracter.isupper():
#         tiene_mayuscula = True

# if len(contraseña) >= 8 and tiene_numero and tiene_mayuscula: 
#     print('contraseña valida')
# else:
#     print('La contraseña debe tener al menos 8 caracteres y un numero y una mayuscula')

#-----------------------------------------------------------------------------

#Ejercicio 5 – Clasificación de triángulos

# lad1 = float(input('Ingrese la longitud del primer lado: ')) 
# lad2 = float(input('Ingrese la longitud del segundo lado: '))
# lad3 = float(input('Ingrese la longitud del tercer lado: '))

# if lad1 + lad2 > lad3 and lad1 + lad3 > lad2 and lad2 + lad3 > lad1:
#     print('Pueden formar un triángulo')

#     if lad1 == lad2 == lad3:
#         print('Este es un triangulo de tipo: Equilatero')
#     elif lad1 == lad2 or lad2 == lad3 or lad1 == lad3:
#         print('Este es un triangulo de tipo: Isosceles')
#     else:
#         print('Este es un triangulo de tipo: Escaleno')
# else:
#     print('No pueden formar un triángulo')