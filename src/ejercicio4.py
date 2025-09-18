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
print("Tu IMC = ", imc)
#Determinar la escala del imc
if imc > 18.5 and imc < 24.9:
    print("imc normal")
if imc > 25 and imc < 29.9:
    print("imc sobrepeso")
if imc > 30 and imc < 34.9:
    print("imc obesidad I")
if imc > 35 and imc < 39.9:
    print("imc obesidad II")
if imc >= 40:
    print("imc obesidad EXTREMA")
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

print(f"paciente {nombre},tiene un imc de {imc:0.2f} y su condicion es de {mensaje}")
    