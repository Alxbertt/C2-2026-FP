# Ejercicio 1: Tipos de datos

# NombreCompleto = "Albert Emmanuel Hichez Perez"
# Edad = 19
# EstaturaM = 181.52
# Estudiante = True

# print(type(NombreCompleto))
# print(type(Edad))
# print(type(EstaturaM))
# print(type(Estudiante))

#----------------------------------------------------

#Ejercicio 2: Operadores aritmeticos

# a = int(input("Ingrese un valor para a: "))
# b = int(input("Ingrese un valor para b: "))

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)

#----------------------------------------------------

#Ejercicio 3: Conversión de tipos

# numUs = int(input("Ingresa un numero entero: "))

# print(f"Este es el numero en float: {float(numUs)} y este es el valor en str {str(numUs)}")

#----------------------------------------------------

#Ejercicio 4: Cálculo de promedio

# num1 = int(input("Ingrese un primer numero: "))
# num2 = int(input("Ingrese un primer numero: "))
# num3 = int(input("Ingrese un primer numero: "))
# promresult = (num1 + num2 + num3) / 3
# print(float(promresult))

#----------------------------------------------------

#Ejercicio 5: Área de un círculo

# Radiodecirculo = float(input("Ingresa el radio de un circulo (Decimal): "))
# Area = 3.14 * (Radiodecirculo ** 2)
# print(f"El area del circulo es: {Area}")

#----------------------------------------------------

#Ejercicio 6: Concatenación de texto

# Nombreuser = input("Ingresa tu nombre: ")
# Edad = int(input("Ingresa tu edad: "))
# Edad10 = Edad + 10 
# print(f"Esta es la nueva edad con la suma: {Edad10}")
# Edad = (str(Edad))
# print(f"El nombre de usuario es: {Nombreuser}, edad + 10 es: {Edad10} y la edad original es: {Edad}")   

#----------------------------------------------------

#Ejercicio 7: Resto de una division 

# num1 = int(input("Ingrese un primer numero: "))
# num2 = int(input("Ingrese un segundo numero: "))

# division = (num1/num2)
# residuo = (num1%num2)
# print(f"Este es el resultado de la division: {division} y este es el residuo: {residuo}")

#----------------------------------------------------

#Ejercicio 8: Conversión de temperatura

# TempC = float(input("Ingrese una temperatura en celcius: "))
# TempF = (9/5) * TempC + 32
# print(f"El equivalente de {TempC} celcius a fahrenheit es: {TempF:.2f}")

#----------------------------------------------------

#Ejercicio 9: Promedio de notas con casting

# nota1 = float(input("Ingrese la primera nota (En decimal): "))
# nota2 = float(input("Ingrese la segunda nota (En decimal): "))
# nota3 = float(input("Ingrese la tercera nota (En decimal): "))

# promcalc = (nota1 + nota2 + nota3) / 3
# promint = int(promcalc)
# print(f"El promedio entero es: {promint}")

#----------------------------------------------------

#Ejercicio 11: Operadores lógicos

# a = True 
# b = False 

# print(a and b)
# print(a or b)
# print(not a)

#----------------------------------------------------

#+EJERCICIOS TIPOS DE DATOS

#Conversor de unidades 

# metros = float(input("ingrese una cantidad de metros: "))
# cm = (metros * 100)
# mm = (metros * 1000)
# print(f'Equivalente en Centimetros: {cm:.2f}')
# print(f'Equivalente en Milimetros: {mm:.2f}')

#----------------------------------------------------

#Area de un circulo

# VALORPI = 3.1416
# radio = float(input("Ingrese el radio del circulo: "))
# print(f"El area es igual a: {VALORPI * (radio ** 2):.2f}")

#----------------------------------------------------

#Operaciones basicas

# num1 = int(input("ingrese un primer numero (entero): "))
# num2 = int(input("ingrese un segundo numero (entero): "))

# print(f"Sumados: {num1+num2}")
# print(f"Restados: {num1-num2}")
# print(f"multiplicados: {num1*num2}")
# print(f"divididos: {num1/num2}")

#----------------------------------------------------

#Calculo de edad 

# FECHADENACIMIENTO = int(input("Ingrese su año de nacimiento: "))
# añoActual = int(input("Ingrese el año actual: "))
# edadactual = (añoActual - FECHADENACIMIENTO)
# print(f"Su edad es: {edadactual}")


#----------------------------------------------------

#Intercambio de valores

# val1 = float(input("Ingresa el primer valor: "))
# val2 = float(input("Ingresa el primer valor: "))

# print(f"Primer valor es: {val1}")
# print(f"Segundo valor es: {val2} ")
# print("-----------------------------")
# print(f"Ahora primer valor es: {val2}")
# print(f"Ahora Segundo valor es: {val1} ")