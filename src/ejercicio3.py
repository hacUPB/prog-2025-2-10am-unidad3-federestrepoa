#determinar si un numero es par o impar
numero = int(input("ingrese el numero entero: "))
residuo = numero % 2
#si residuo es 0 es por 
if residuo == 0:
    print(numero, " es par")
#si no es impar 
else:
    print(numero," es impar")