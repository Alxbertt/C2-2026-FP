import os
os.system('cls')

nombre = input('ingrese su nombre: \n')
edad =  int(input("Ingrese su edad: \n"))
nacionalidad = input('Cual es su nacionalidad: \n')
tipo_de_membresia = int(input('Cual es su tipo de membresia: 1-Básica, 2-Premium, 3-VIP, 4-ninguna: \n'))
membresia_valida = False

if tipo_de_membresia == 1 or 2 or 3:
    membresia_valida = True 
else: 
    membresia = False

print('----------------------------------------------')
print('              BIENVENIDO AL CLUB              ')
print('----------------------------------------------')
print('          ESCOJA UNA OPCION DEL MENU:         ')
print('')
opciones = int(input('''
1-Entrar al club
2-Comprar membresía
3-Salir: \n'''))

match opciones:
    case 1: 
        if edad > 18 and tipo_de_membresia == True:
            print('Bienvenido!!!')
            invitados = int(input('Cuantos invitados traera: \n'))
            while invitados > 5:
                invitados = int(input('Cuantos invitados traera: \n'))
            if invitados == 5:
                print(f'Invitados:{invitados} Maximo alcanzado!')
            elif invitados < 5:
                print(f'Invitados:{invitados}')
        else:
            print('Algo esta mal con sus datos, favor revisar de nuevo.')
    case 2: 
        print('----------------------------------------------')
        print('            Compra de membresia               ')
        print('----------------------------------------------')
        membresias = int(input('''
        1-BASICA
        2-Premium
        3-VIP: \n'''))
        match membresias:
            case 1: 
                print("Básica -> RD$500")
            case 2: 
                print("Premium -> RD$1200")
            case 3: 
                print("VIP -> RD$2500")
        confirmacion = input('Desea confirmar la compra (si/no): ?')