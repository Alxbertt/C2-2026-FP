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
#--------------------------------------------------------------------------------
#EJERCICIOS FUNCIONES 4
#--------------------------------------------------------------------------------

#Funciones Auxiliares

# def es_par(numero):
#     return numero % 2 == 0


# def promedio(suma, cantidad):
#     if cantidad == 0:
#         return 0
#     return suma / cantidad


# def porcentaje(parte, total):
#     if total == 0:
#         return 0
#     return (parte / total) * 100


# def mayor(a, b):
#     return a if a > b else b


# def formato_moneda(monto):
#     return f"RD${monto:,.2f}"


#Funciones propias de cada utilidad

# def es_aprobado(nota):
#     return nota >= 70


# def clasificar(prom):
#     if prom >= 90:
#         return "Excelente"
#     elif prom >= 80:
#         return "Bueno"
#     elif prom >= 70:
#         return "Regular"
#     else:
#         return "Deficiente"


# def calcular_itbis(subtotal):
#     return subtotal * 0.18


# def tiene_longitud(clave):
#     return len(clave) >= 8


# def tiene_numero(clave):
#     for c in clave: 
#         if c.isdigit():
#             return True
#     return False


# def tiene_mayuscula(clave):
#     for c in clave: 
#         if c.isupper():
#             return True
#     return False


# def validar_clave(clave):
#     if not tiene_longitud(clave):
#         return "Inválida: debe tener mínimo 8 caracteres."
#     if not tiene_numero(clave):
#         return "Inválida: debe tener al menos un número."
#     if not tiene_mayuscula(clave):
#         return "Inválida: debe tener al menos una letra mayúscula."
#     return "Contraseña válida."


#Funciones procesadoras con toda la logica

# def procesar_notas():
#     cantidad = 0
#     suma = 0
#     aprobados = 0
#     nota_max = None

#     while True:
#         nota = float(input("Ingrese una nota (-1 para finalizar): "))
#         if nota == -1:
#             break
#         cantidad += 1
#         suma += nota
#         if es_aprobado(nota):
#             aprobados += 1
#         nota_max = nota if nota_max is None else mayor(nota_max, nota)

#     if cantidad == 0:
#         mostrar_notas(0, 0, 0, 0, 0, "Sin datos")
#         return

#     prom = promedio(suma, cantidad)
#     pct = porcentaje(aprobados, cantidad)
#     mostrar_notas(cantidad, prom, aprobados, pct, nota_max, clasificar(prom))


# def procesar_factura():
#     cantidad = 0
#     subtotal = 0
#     precio_max = None

#     while True:
#         precio = float(input("Ingrese el precio de un producto (0 para finalizar): "))
#         if precio == 0:
#             break
#         cantidad += 1
#         subtotal += precio
#         precio_max = precio if precio_max is None else mayor(precio_max, precio)

#     if cantidad == 0:
#         mostrar_factura(0, 0, 0, 0, 0, 0)
#         return

#     itbis = calcular_itbis(subtotal)
#     total = subtotal + itbis
#     prom = promedio(subtotal, cantidad)
#     mostrar_factura(cantidad, subtotal, itbis, total, prom, precio_max)


# def procesar_clave():
#     intentos = 0
#     while intentos < 3:
#         clave = input("Ingrese su contraseña: ")
#         resultado = validar_clave(clave)
#         mostrar_clave(resultado)
#         if resultado == "Contraseña válida.":
#             return
#         intentos += 1
#     mostrar_clave("Se excedio el limite de intentos")


# def procesar_numeros():
#     cantidad = 0
#     pares = 0
#     impares = 0
#     suma_pares = 0
#     numero_max = None

#     while True:
#         numero = int(input("Ingrese un número positivo (0 para finalizar): "))
#         if numero == 0:
#             break
#         cantidad += 1
#         if es_par(numero):
#             pares += 1
#             suma_pares += numero
#         else:
#             impares += 1
#         numero_max = numero if numero_max is None else mayor(numero_max, numero)

#     if cantidad == 0:
#         mostrar_numeros(0, 0, 0, 0, 0)
#         return

#     pct = porcentaje(pares, cantidad)
#     mostrar_numeros(pares, impares, pct, suma_pares, numero_max)

#Aqui estan las funciones de muestra de datos:

# def mostrar_menu():
#     print("\nBienvenido al apartado de Consola de Utilidades")
#     print("1. Reporte de notas del grupo")
#     print("2. Factura de colmado")
#     print("3. Validador de contraseña")
#     print("4. Análisis de números")
#     print("5. Salir")


# def mostrar_notas(cantidad, prom, aprobados, pct, nota_max, clasificacion):
#     print("\nReporte de Notas del Grupo:")
#     print(f"Cantidad de notas: {cantidad}")
#     print(f"Promedio: {prom:.2f}")
#     print(f"Aprobados: {aprobados} ({pct:.2f}%)")
#     print(f"Nota más alta: {nota_max}")
#     print(f"Clasificación del grupo: {clasificacion}")


# def mostrar_factura(cantidad, subtotal, itbis, total, prom, precio_max):
#     print("\nFactura de Colmado:")
#     print(f"Cantidad de productos: {cantidad}")
#     print(f"Subtotal: {formato_moneda(subtotal)}")
#     print(f"ITBIS (18%): {formato_moneda(itbis)}")
#     print(f"Total: {formato_moneda(total)}")
#     print(f"Precio promedio: {formato_moneda(prom)}")
#     print(f"Producto más caro: {formato_moneda(precio_max)}")


# def mostrar_clave(mensaje):
#     print(mensaje)


# def mostrar_numeros(pares, impares, pct, suma_pares, numero_max):
#     print("\nAnálisis de Números: ")
#     print(f"Cantidad de pares: {pares}")
#     print(f"Cantidad de impares: {impares}")
#     print(f"Porcentaje de pares: {pct:.2f}%")
#     print(f"Suma de los pares: {suma_pares}")
#     print(f"Número mayor: {numero_max}")


#Funcion main:

# def main():
#     opcion = ""
#     while opcion != "5":
#         mostrar_menu()
#         opcion = input("Seleccione una opción (1-5): ")
#         if opcion == "1":
#             procesar_notas()
#         elif opcion == "2":
#             procesar_factura()
#         elif opcion == "3":
#             procesar_clave()
#         elif opcion == "4":
#             procesar_numeros()
#         elif opcion == "5":
#             print("Hasta luego.")
#         else:
#             print("Opción inválida.")

# main()

#--------------------------------------------------------------------------------
#Ejercicios funciones 5

#funciones minimas 
# def aplicar_tasa(monto, tasa):
#     return monto * tasa


# def calcular_afp(bruto):
#     return bruto * 0.0287


# def calcular_sfs(bruto):
#     return bruto * 0.0304


# def calcular_sueldo_quincenal(sueldo_mensual):
#     return sueldo_mensual / 2


# def calcular_valor_horas_extras(sueldo_mensual):
#     return (sueldo_mensual / 23.83 / 8) * 1.35


# def calcular_pago_horas_extras(valor_hora, horas):
#     return valor_hora * horas


# def calcular_bonificacion(sueldo_quincenal, aplica):
#     if aplica == "si":
#         return sueldo_quincenal * 0.08
#     return 0


# def calcular_ingreso_bruto(sueldo_quincenal, pago_horas, bonificacion):
#     return sueldo_quincenal + pago_horas + bonificacion

# def pedir_datos():
#     nombre = input("Favor ingresar su nombre: ")
#     sueldo_mensual = float(input("Sueldo mensual (RD$): "))
#     horas_extras = float(input("Horas extras trabajadas: "))
#     bonificacion = input("Uste Tiene bonificacion? (si/no): ")

#     return nombre, sueldo_mensual, horas_extras, bonificacion

# def calcular_isr(base):
#     if base <= 17342:
#         return 0
#     elif base <= 26013:
#         return (base - 17342) * 0.15
#     else:
#         return 1300.65 + ((base - 26013) * 0.20)


# def calcular_porcentaje_descuentos(total_descuentos, bruto):
#     return (total_descuentos / bruto) * 100


# def mostrar_recibo(nombre, sueldo_quincenal, pago_horas, bonificacion, bruto, afp, sfs, isr, sueldo_neto, porcentaje):
#     print("------------------- RECIBO DE NOMINA -------------------")
#     print(f"Empleado: {nombre}")
#     print("--------------------------------------------------------")
#     print(f"Sueldo quincenal: RD${sueldo_quincenal:,.2f}")
#     print(f"Horas extra      : RD${pago_horas:,.2f}")
#     print(f"Bonificación     : RD${bonificacion:,.2f}")
#     print("--------------------------------------------------------")
#     print(f"Ingreso bruto    : RD${bruto:,.2f}")
#     print("--------------------------------------------------------")
#     print(f"AFP (2.87%)      : RD${afp:,.2f}")
#     print(f"SFS (3.04%)      : RD${sfs:,.2f}")
#     print(f"ISR (3.04%)      : RD${isr:,.2f}")
#     print("--------------------------------------------------------")
#     print(f"Sueldo neto      : RD${sueldo_neto:,.2f}")
#     print(f"% Descuentos     : {porcentaje:,.2f}%")
#     print("--------------------------------------------------------")


# nombre, sueldo_mensual, horas_extras, aplica_bono = pedir_datos()
# sueldo_quincenal = calcular_sueldo_quincenal(sueldo_mensual)
# valor_hora = calcular_valor_horas_extras(sueldo_mensual)
# pago_horas = calcular_pago_horas_extras(valor_hora, horas_extras)
# bonificacion = calcular_bonificacion(sueldo_quincenal, aplica_bono)

# bruto = calcular_ingreso_bruto(
#     sueldo_quincenal,
#     pago_horas,
#     bonificacion
# )

# afp = calcular_afp(bruto)
# sfs = calcular_sfs(bruto)
# base_isr = bruto - afp - sfs
# isr = calcular_isr(base_isr)

# total_descuentos = afp + sfs + isr

# sueldo_neto = bruto - total_descuentos

# porcentaje = calcular_porcentaje_descuentos(
#     total_descuentos,
#     bruto
# )

# mostrar_recibo(
#     nombre,
#     sueldo_quincenal,
#     pago_horas,
#     bonificacion,
#     bruto,
#     afp,
#     sfs,
#     isr,
#     sueldo_neto,
#     porcentaje
# )

#--------------------------------------------------------------------

#EJERCICIOS FUNCIONES 6

#--------------------------------------------------------------------
# Funciones mínimas: caracter -> booleano
# ---------------------------------------------------------------------
 
# def es_vocal(caracter):
#     vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
#     return caracter in vocales
 
 
# def es_letra(caracter):
#     return caracter.isalpha()
 
 
# def es_digito(caracter):
#     return caracter.isdigit()
 

# def contar_vocales(texto):
#     contador = 0
#     for caracter in texto:
#         if es_vocal(caracter):
#             contador += 1
#     return contador
 
 
# def contar_consonantes(texto):
#     contador = 0
#     for caracter in texto:
#         if es_letra(caracter) and not es_vocal(caracter):
#             contador += 1
#     return contador
 
 
# def contar_letras(texto):
#     contador = 0
#     for caracter in texto:
#         if es_letra(caracter):
#             contador += 1
#     return contador
 
 
# def contar_digitos(texto):
#     contador = 0
#     for caracter in texto:
#         if es_digito(caracter):
#             contador += 1
#     return contador
 
 
# def contar_espacios(texto):
#     contador = 0
#     for caracter in texto:
#         if caracter == " ":
#             contador += 1
#     return contador
 
 
# def contar_palabras(texto):
#     palabras = texto.split()
#     return len(palabras)
 
 
# def palabra_mas_larga(texto):
#     palabras = texto.split()
#     if not palabras:
#         return ""
 
#     mas_larga = palabras[0]
#     for palabra in palabras:
#         if len(palabra) > len(mas_larga):
#             mas_larga = palabra
#     return mas_larga
 
 
# def normalizar(texto):
#     tildes = {
#         "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
#         "Á": "a", "É": "e", "Í": "i", "Ó": "o", "Ú": "u",
#         "ü": "u", "Ü": "u",
#     }
 
#     texto_sin_tildes = ""
#     for caracter in texto:
#         if caracter in tildes:
#             texto_sin_tildes += tildes[caracter]
#         else:
#             texto_sin_tildes += caracter
 
#     texto_sin_espacios = texto_sin_tildes.replace(" ", "")
#     return texto_sin_espacios.lower()
 
 
# def invertir(texto):
#     return texto[::-1]
 
 
# def es_palindromo(texto):

#     texto_normalizado = normalizar(texto)
#     return texto_normalizado == invertir(texto_normalizado)
 
 
# def porcentaje(parte, total):
#     if total == 0:
#         return 0
#     return (parte / total) * 100
 
 
# def clasificar_frase(cantidad_caracteres):
#     if cantidad_caracteres > 50:
#         return "Frase larga"
#     elif cantidad_caracteres >= 20:
#         return "Frase media"
#     else:
#         return "Frase corta"
 
 

# def pedir_frase():
#     frase = input("Escribe una frase: ")
#     return frase
 
 
# def mostrar_resultados(frase, total_caracteres, vocales, consonantes,
#                         espacios, digitos, palabras, palabra_larga,
#                         porcentaje_vocales, palindromo, veredicto):
    
#     print("\n--- Análisis de la frase ---")
#     print(f"Frase: {frase}")
#     print(f"Cantidad total de caracteres: {total_caracteres}")
#     print(f"Cantidad de vocales: {vocales}")
#     print(f"Cantidad de consonantes: {consonantes}")
#     print(f"Cantidad de espacios: {espacios}")
#     print(f"Cantidad de dígitos: {digitos}")
#     print(f"Cantidad de palabras: {palabras}")
#     print(f"Palabra más larga: '{palabra_larga}' ({len(palabra_larga)} letras)")
#     print(f"Porcentaje de vocales respecto al total de letras: {porcentaje_vocales:.2f}%")
#     print(f"¿Es palíndromo?: {'Sí' if palindromo else 'No'}")
#     print(f"Veredicto: {veredicto}")
 
#main 
 
# def main():
#     frase = pedir_frase()
 
#     total_caracteres = len(frase)
#     vocales = contar_vocales(frase)
#     consonantes = contar_consonantes(frase)
#     espacios = contar_espacios(frase)
#     digitos = contar_digitos(frase)
#     palabras = contar_palabras(frase)
#     letras = contar_letras(frase)
#     palabra_larga = palabra_mas_larga(frase)
#     porcentaje_vocales = porcentaje(vocales, letras)
#     palindromo = es_palindromo(frase)
#     veredicto = clasificar_frase(total_caracteres)
 
#     mostrar_resultados(frase, total_caracteres, vocales, consonantes,
#                         espacios, digitos, palabras, palabra_larga,
#                         porcentaje_vocales, palindromo, veredicto)
# main()

#--------------------------------------------------------------------
#ASIGNACION #4

#Ejercicio 1- Calculo de promedio de notas

# def recibidor_de_notas():
#     nota1 = int(input('Ingrese la primera nota: '))
#     nota2 = int(input('Ingrese la segunda nota: '))
#     nota3 = int(input('Ingrese la tercera nota: '))
    
#     promedio = calculador_de_promedio(nota1, nota2, nota3)
#     return promedio

# def calculador_de_promedio(nota1, nota2, nota3):
#     promedio = (nota1 + nota2 + nota3) / 3
#     return promedio 

# def determinacion_de_estudiante(promedio):
#     if promedio >= 70:
#         return "Aprueba"
#     else:
#         return "Reprueba"

    
# promedio = recibidor_de_notas()
# print(determinacion_de_estudiante(promedio))

#--------------------------------------------------------------------
#Ejercicio 2 – Conversión de temperatura modular


# def celcius_a_fahrenheit(ingreso_de_temp):
#     resultado_de_conversion_c_f = (ingreso_de_temp * 9/5) + 32
#     return resultado_de_conversion_c_f

# def fahrenheit_a_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9


# tipo_de_conversion = int(input('Que conversion desea realizar: 1-Celcius a fahrenheit o 2-Fahrenheit a celcius: '))

# if tipo_de_conversion == 1:
#     ingreso_de_temp = int(input('Ingrese la temperatura a convertir: '))
#     resultado = celcius_a_fahrenheit(ingreso_de_temp)
#     print(f"El resultado en Fahrenheit es: {resultado:.2f}")
    
# elif tipo_de_conversion == 2:
#     ingreso_de_temp = int(input('Ingrese la temperatura a convertir: '))
#     resultado = fahrenheit_a_celsius(ingreso_de_temp)
#     print(f"El resultado en Celsius es: {resultado:.2f}")

# else:
#     print("Opción incorrecta. Elige 1 o 2.")

#--------------------------------------------------------------------
#Ejercicio 3 – Operaciones básicas con funciones

# def sumar(a, b):
#     return a + b

# def restar(a, b):
#     return a - b

# def multiplicar(a, b):
#     return a * b

# def dividir(a, b):
#     if b == 0:
#         return "imposible dividir entre cero!!!"
#     return a / b

# def ejecutar_operacion(opcion, num1, num2):
#     if opcion == 1:
#         return sumar(num1, num2)
#     elif opcion == 2:
#         return restar(num1, num2)
#     elif opcion == 3:
#         return multiplicar(num1, num2)
#     elif opcion == 4:
#         return dividir(num1, num2)
#     else:
#         return "Opción no valida"

# print("--- CALCULADORA BASICA ---")
# n1 = float(input("Ingrese el primer numero: "))
# n2 = float(input("Ingrese el segundo numero: "))

# print("\nOperaciones disponibles:")
# print("1- Suma\n2- Resta\n3- Multiplicación\n4- Division")
# seleccion = int(input("Seleccione la operacion a realizar (1-4): "))

# resultado_final = ejecutar_operacion(seleccion, n1, n2)

# print(f"\nResultado: {resultado_final}")

#--------------------------------------------------------------------
#Ejercicio 4 – Análisis de número

# def determinar_par_impar(numero):
#     if numero % 2 == 0:
#         return "Par"
#     else:
#         return "Impar"


# def determinar_signo(numero):
#     if numero > 0:
#         return "Positivo"
#     elif numero < 0:
#         return "Negativo"
#     else:
#         return "Cero"


# numero = int(input("Ingrese un número: "))

# print(determinar_par_impar(numero))
# print(determinar_signo(numero))

#--------------------------------------------------------------------
#Ejercicio 5 – Validación de contraseña modular

# def validar_longitud(password):
#     return len(password) >= 8


# def validar_numero(password):
#     for caracter in password:
#         if caracter.isdigit():
#             return True
#     return False


# def validar_mayuscula(password):
#     for caracter in password:
#         if caracter.isupper():
#             return True
#     return False


# def validar_password(password):

#     if not validar_longitud(password):
#         print("Debe contar con al menos 8 caracteres")

#     if not validar_numero(password):
#         print("Lo sentimos su contraseña debe tener al menos un numero")

#     if not validar_mayuscula(password):
#         print("Lo sentimos su contraseña debe tener al menos una letra mayuscula")

#     if (validar_longitud(password)
#             and validar_numero(password)
#             and validar_mayuscula(password)):
#         print("Contraseña valida!!!")


# password = input("Ingrese una contraseña: ")
# validar_password(password)