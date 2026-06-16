import os
os.system('cls')

# nombre_cliente = input('Ingrese su nombre: ')
# edad = int(input('Ingrese su edad: '))
# tipo_entrada = int(input('''Cual es su tipo de entrada:
# 1 - General
# 2 - Estudiante
# 3 - VIP
# \n'''))

# cantidad_boletos = int(input('Ingrese una cantidad de boletos a comprar: '))
# precio_boleto = None
# #variables de descuentos especiales

# match tipo_entrada:
#     case 1: 
#         tipo_entrada = "General"
#         precio_boleto = 300
#         print('El precio de General = RD$300')
#     case 2:
#         tipo_entrada = "Estudiante"
#         precio_boleto = 200
#         print('El precio de Estudiante = RD$200')
#     case 3: 
#         tipo_entrada = "Vip"
#         precio_boleto = 500
#         print('El precio de VIP = RD$500')
#     case _:
#         tipo_entrada = False

# subtotal = precio_boleto * cantidad_boletos 

# if tipo_entrada != False and precio_boleto != False: 
#     if edad < 12 and cantidad_boletos > 5:
#         descuento = subtotal * 0.60
#         print("----------------------------------------------")
#         print("----------------------------------------------")
#         print("                   Final                      ")
#         print("----------------------------------------------")
#         print(f"Cliente:{nombre_cliente}                     ")
#         print(f"Tipo:{tipo_entrada}                          ")
#         print(f"Boletos:{cantidad_boletos}                   ")
#         print(f"Subtotal: RD${subtotal}                      ")
#         print(f"Descuento 60%: RD${descuento}                ")
#         print(f"Total a pagar: RD${subtotal - descuento}     ")
#         print("----------------------------------------------")
#         print("----------------------------------------------")
#     elif edad < 12:
#         descuento = subtotal * 0.50
#         print("----------------------------------------------")
#         print("----------------------------------------------")
#         print("                   Final                      ")
#         print("----------------------------------------------")
#         print(f"Cliente:{nombre_cliente}                     ")
#         print(f"Tipo:{tipo_entrada}                          ")
#         print(f"Boletos:{cantidad_boletos}                   ")
#         print(f"Subtotal: RD${subtotal}                      ")
#         print(f"Descuento 50%: RD${descuento}                ")
#         print(f"Total a pagar: RD${subtotal - descuento}     ")
#         print("----------------------------------------------")
#         print("----------------------------------------------")
#     if edad >= 60 and cantidad_boletos > 5:
#         descuento = subtotal * 0.40
#         print("----------------------------------------------")
#         print("----------------------------------------------")
#         print("                   Final                      ")
#         print("----------------------------------------------")
#         print(f"Cliente:{nombre_cliente}                     ")
#         print(f"Tipo:{tipo_entrada}                          ")
#         print(f"Boletos:{cantidad_boletos}                   ")
#         print(f"Subtotal: RD${subtotal}                      ")
#         print(f"Descuento 40%: RD${descuento}                ")
#         print(f"Total a pagar: RD${subtotal - descuento}     ")
#         print("----------------------------------------------")
#         print("----------------------------------------------")
#     elif edad >= 60: 
#         descuento = subtotal * 0.30
#         print("----------------------------------------------")
#         print("----------------------------------------------")
#         print("                   Final                      ")
#         print("----------------------------------------------")
#         print(f"Cliente:{nombre_cliente}                     ")
#         print(f"Tipo:{tipo_entrada}                          ")
#         print(f"Boletos:{cantidad_boletos}                   ")
#         print(f"Subtotal: RD${subtotal}                      ")
#         print(f"Descuento 30%: RD${descuento}                ")
#         print(f"Total a pagar: RD${subtotal - descuento}     ")
#         print("----------------------------------------------")
#         print("----------------------------------------------")
# else:
#     print('Favor ingresar un tipo de entrada!')