#Ejercicio 1 saludo personalizado

#nombre = input("Cual es tu nombre?: ")
#Edad = input("Cuantos años tienes?: ")
#Carrera = input("Que carrera estudias en el itla?: ")

#print(f"¡Hola {nombre}!, tienes{Edad} años y estudias {Carrera} en el itla")

#-------------------------------------------------------------------------------

#Ejercicio 2 Calculadora de propina

#montoDeCuenta = float(input ("Hola, bienvenido cual es el monto de la cuenta en el restaurante ?"))
#print("Porcentaje de propina (%): 10%")
#propina = (montoDeCuenta * 0.10)
#total = montoDeCuenta + propina
#DivididoA4 = total/4

#print(f"Propina: RD${propina}")
#print(f"Total a pagar: RD${total}")
#print(f"Cada uno paga: RD${DivididoA4}")

#-------------------------------------------------------------------------------

#Ejercicio 3 Conversor de unidades 

#METROS_A_PIES = 3.28084 
#KILOGRAMOS_A_LIBRAS = 2.20462 
#CELSIUS_A_FAHRENHEIT_FACTOR = 9/5 
#CELSIUS_A_FAHRENHEIT_AJUSTE = 32 

#AlturaEnMetros = float(input("Ingrese su altura en metros:"))
#Kilogramos = float(input("Ingrese su peso en kilogramos:"))
#TempC = float(input("Ingrese su temperatura en Celcius:")) 
#print("-----------------------------------------------------")
#print("-----------------------------------------------------")
#print (f"{AlturaEnMetros} M, equivale a: {AlturaEnMetros * METROS_A_PIES/1.0} ft")
#print (f"{Kilogramos} kg, equivale a: {Kilogramos * KILOGRAMOS_A_LIBRAS/1.0} lb")
#print (f"{TempC} °C, equivale a: {TempC * CELSIUS_A_FAHRENHEIT_FACTOR + CELSIUS_A_FAHRENHEIT_AJUSTE} °F")

#-------------------------------------------------------------------------------

#Ejercicio 4 Validador de condiciones

#Edad = int(input("Cual es tu edad? "))
#Cedula = input("Tienes cedula (si/no)? ")
#Saldo = float(input("Digita tu saldo (RD$): "))
#print("-------------------------------------------------------------")
#print("-------------------------------------------------------------")

#print(f"Mayor de edad ? {Edad >= 18} ")
#print(f"Puede votar? {Edad and Cedula == "si"} ")
#print(f"Puede pedir prestamo? {Edad and Cedula and Saldo >=5000} ")
#print(f"Necesita ayuda financiera? {Saldo < 1000 or Cedula == "no"} ")#

#-------------------------------------------------------------------------------

#Ejercicio 5 Análisis de promedio 

#Calificacion_parcial_1 = float(input("Ingrese su calificacion del primer parcial: "))
#Calificacion_parcial_2 = float(input("Ingrese su calificacion del segundo parcial: "))
#PromedioAsignaciones = float(input("Ingrese su promedio de asignaciones: "))
#PromedioPracticas = float(input("Ingrese su promedio de practicas: "))
#calificacion_tentatica_proyectof = float(input("Ingrese una calificacion tentativa para el proyecto final: "))


#promedio_final = (Calificacion_parcial_1 + Calificacion_parcial_2 + PromedioAsignaciones + PromedioPracticas + calificacion_tentatica_proyectof) / 5

#Riesgo = 65 >= promedio_final < 70 

#print(f"Promedio final: {promedio_final:.2f}")
#print(f"Aprueba? {promedio_final >=70}")
#print(f"Esta en riesgo? {Riesgo}")