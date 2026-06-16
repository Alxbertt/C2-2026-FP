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

for i in range(1, 21): 
    if i % 10 == 4: 
        continue
    print(i)




    