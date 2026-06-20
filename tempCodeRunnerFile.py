suma_productos = 0
otro_agregado = "si"

while otro_agregado == "si":
    precios_de_productos = float(input("Introduzca el precio de un productos: "))
    suma_productos += precios_de_productos

    otro_agregado = input('Desea agregar otro producto: si/no: ')
print(f"Total a pagar: {suma_productos}")
