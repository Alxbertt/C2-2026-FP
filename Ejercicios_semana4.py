import os 
os.system("cls")
#------------------------------------------------------------
# Ejercicio 1: Condicional simple
# persona buscada

# nombreus = "Albert Hichez"
# nombre_de_ingresar = input("Ingrese su nombre: ")

# if nombreus == nombre_de_ingresar: 
#     print("Bienvenido")
# else:
#     ()

#------------------------------------------------------------

#Ejercicio 2: Condicional doble
#Numero mayor

# num1 = int(input("Ingrese un primer numero: "))
# num2 = int(input("Ingrese un segundo numero: "))

# if num1 > num2: 
#     print('El primer numero es mayor')
# else: 
#     print('El segundo numero es mayor o son iguales')

#------------------------------------------------------------

#Ejercicio 3: Condicional multiple
#Clasificación de temperatura

# temp_c = float(input('Ingrese una temperatura en Celcius: '))

# if temp_c < 0:
#     print('Temperatura bajo cero')
# elif temp_c >= 0 and temp_c <= 25:
#     print('Temperatura templada')
# elif temp_c >= 26 and temp_c <= 35:
#     print('Temperatura calida')
# elif temp_c > 35: 
#     print('Temperatura alta')

#------------------------------------------------------------

#Ejercicio 4: Condicional anidada
#Descuento por tipo de cliente

# monto_de_compra = float(input("Ingrese el monto de la compra: "))
# tipo_de_cliente = input("Es cliente regular o vip ?")

# if monto_de_compra > 0:

#     if tipo_de_cliente == "vip":

#         if monto_de_compra >= 5000:
#             print(f'''Usted recibe descuento del 20% en su compra de RD${monto_de_compra:.2f}
#             ----------------------------------------
#             SubTotal: {monto_de_compra:.2f} - 20%
#             TOTAL: {monto_de_compra - (monto_de_compra * 0.20):.2f}
#             ----------------------------------------''')

#         else:
#             print(f'''Usted recibe descuento del 10% en su compra de RD${monto_de_compra:.2f}
#             ----------------------------------------
#             SubTotal: {monto_de_compra:.2f} - 10%
#             TOTAL: {monto_de_compra - (monto_de_compra * 0.10):.2f}
#             ----------------------------------------''')

#     elif tipo_de_cliente == "regular":

#         if monto_de_compra >= 5000:
#             print(f'''Usted recibe descuento del 10% en su compra de RD${monto_de_compra:.2f}
#             ----------------------------------------
#             SubTotal: {monto_de_compra:.2f} - 10%
#             TOTAL: {monto_de_compra - (monto_de_compra * 0.10):.2f}
#             ----------------------------------------''')

#         else:
#             print("El monto debe ser mayor a 5000 para aplicar el descuento")

# else:
#     print("El monto debe ser mayor a 0")


#------------------------------------------------------------

#EJERCICIOS ESTRUCTURA CONDICIONAL

#Ejercicio 1: PROGRAMA QUE LEA UN NUMERO Y DETERMINE SI ES POSITIVO O NEGATIVO, MOSTRANDO UN MENSAJE PARA CADA CASO.

# num1 = int(input('Ingrese un numero: '))
# if num1 > 0: 
#    print("Este es un numero positivo") 
# else: 
#    print('Este numero es negativo')


#------------------------------------------------------------

#Ejercicio 2: PROGRAMA QUE LEA UN NUMERO DE DOS DÍGITOS Y DETERMINE SI AMBOS DÍGITOS SON PARES O IMPARES. DEBE MOSTRAR UN MENSAJE DANDO LA INFORMACIÓN DE CADA DÍGITO (DECIR: "EL 1ER DÍGITO ES __(PAR  O IMPAR), EL SEGUNDO...").

# numero = int(input("Ingrese un número de dos dígitos: "))

# primer_digito = numero // 10
# segundo_digito = numero % 10

# estado1 = "PAR" if primer_digito % 2 == 0 else "IMPAR"
# estado2 = "PAR" if segundo_digito % 2 == 0 else "IMPAR"

# print(f"El 1er dígito es {estado1} y el 2do dígito es {estado2}.")

#------------------------------------------------------------

#Ejercicio 3: PROGRAMA QUE LEA UN NUMERO ENTERO DE DOS DÍGITOS Y DETERMINE SI SUS DOS DÍGITOS SON IGUALES.

# numero = int(input('Digite un numero de dos digitos: '))

# primer_digito = numero // 10 
# segundo_digito = numero % 10 

# if primer_digito == segundo_digito: 
#     print('Sus digitos son iguales')
# else:
#     print('Los digitos son diferentes')

#------------------------------------------------------------

#Ejercicio 4:PROGRAMA QUE LEA DOS NÚMEROS Y DETERMINE CUAL ES EL MAYOR

# num1 = int(input('Ingrese un primer numero: '))
# num2 = int(input('Ingrese un segundo numero: '))

# if num1 > num2: 
#     print('El primer numero es mayor que el segundo')
# else: 
#     print('El segundo numero es mayor que el primero')

#------------------------------------------------------------

#Ejercicio 5:PROGRAMA QUE LEA DOS NÚMEROS Y DETERMINE SI LA SUMATORIA DE AMBOS NÚMEROS ES PAR O IMPAR

# num1 = int(input('Ingrese un primer numero: '))
# num2 = int(input('Ingrese un segundo numero: '))

# suma_de_ambos = num1 + num2 
# if suma_de_ambos % 2 ==0: 
#     print(f'La sumatoria de ambos da {suma_de_ambos} y es un numero par')
# else: 
#     print(f'La sumatoria de ambos da {suma_de_ambos} y es impar')


#------------------------------------------------------------

#1: PROGRAMA QUE LEA UN NUMERO DE DOS DÍGITOS Y DETERMINE SI UN DÍGITO ES MÚLTIPLO DE OTRO

# num = int(input('Ingrese un numero de dos digitos: '))

# digito_1 = num // 10
# digito_2 = num % 10

# if digito_1 == 0 or digito_2 == 0:
#     print('No se puede determinar porque uno de los digitos es 0')
# elif digito_1 % digito_2 == 0:
#     print(f'El {digito_1} es multiplo de {digito_2}')
# elif digito_2 % digito_1 == 0:
#     print(f'El {digito_2} es multiplo de {digito_1}')
# else:
#     print('NO SON MULTIPLOS')

#------------------------------------------------------------

#2: PROGRAMA QUE LEA TRES NÚMEROS Y LOS MUESTRE EN ORDEN ASCENDENTE (DE MENOR A MAYOR)

# num1 = int(input('Ingrese un primer numero: '))
# num2 = int(input('Ingrese un segundo numero: '))
# num3 = int(input('Ingrese un tercer numero: '))

# if num1 >= num2 >= num3:
#     print(num3, num2, num1)

# elif num1 >= num3 >= num2:
#     print(num2, num3, num1)

# elif num2 >= num1 >= num3:
#     print(num3, num1, num2)

# elif num2 >= num3 >= num1:
#     print(num1, num3, num2)

# elif num3 >= num1 >= num2:
#     print(num2, num1, num3)

# elif num3 >= num2 >= num1:
#     print(num1, num2, num3)

#------------------------------------------------------------

#3: PROGRAMA QUE LEA UN NUMERO ENTERO DE TRES DIGITOS Y DETERMINE SI EL PRIMERO ES IGUAL AL ULTIMO.

# numero_de_3_digitos = int(input('Ingrese un numero de 3 digitos: '))

# digito_1 =  numero_de_3_digitos // 100 
# digito_3 = numero_de_3_digitos % 10 

# if digito_1 == digito_3:
#     print('El primer digito es igual al ultimo')
# else:
#     print("El primer digito y el tercero son diferentes")

#------------------------------------------------------------

#4:PROGRAMA QUE LEA LA EDAD DEL USUARIO. SI ES MAYOR QUE 50 MOSTRAR MENSAJE QUE DIGA "ABUELO." SI ES MAYOR QUE 30 MOSTRAR MENSAJE QUE DIGA "PADRE". EN CASO CONTRARIO MOSTRAR MENSAJE QUE DIGA "HIJO"

# edad_usuario = int(input('Ingrese su edad: '))

# if edad_usuario > 50:
#     print('ABUELO')
# elif edad_usuario > 30:
#     print('PADRE')
# else: 
#     print('HIJO')