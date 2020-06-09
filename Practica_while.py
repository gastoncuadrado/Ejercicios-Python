import math

print("Programa de calculo de raiz cuadrada")
numero=int(input("Numero a calcular: "))

intentos=0

while numero<0:
	print("No se puede hallar raiz de numero negativo")
	if intentos==2:
		print("No jodas")
		break

	numero=int(input("Numero a calcular: "))

	if numero<=0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)
	print("Solucion es: "+str(solucion)+ " es raiz de "+str(numero))