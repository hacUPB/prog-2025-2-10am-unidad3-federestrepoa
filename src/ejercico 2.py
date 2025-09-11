print("ingresa tu nombre y apellido")
nombre = input("ingresa tu nombre y apellido")
#opcion 2
print("Bienvenido: ", nombre)
#calcular el IMC de esa persona
#Leer peso, altura
peso = input("ingresa tu peso en kg: ")
peso = float(peso)
altura = input("ingresa tu talla en metros: ")
altura = float(altura)
#calculos
imc = peso/altura**2
#mostrar imc
print("Tu IMC = ",imc)
if imc < 18.5:
    mensaje = "bajo peso"
elif imc < 25: 
    mensaje = "peso normal"
elif imc < 35:
    mensaje = "obesidad tipo 1"
elif imc < 40:
    mesaje = "obesidad tipo 2" 
else : 
    mesaje = "obesidad extrema"

print(f"paciente {nombre},tiene un imc de {imc} y su condicion es {mensaje}")
    