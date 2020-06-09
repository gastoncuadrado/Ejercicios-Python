import math

def calculaRaiz(num1):

	if num1<0:
		raise ValueError("El numero es negativo")

	else:
		return math.sqrt(num1)


op1=(int(input("numero: ")))

try:
	print(calculaRaiz(op1))

except ValueError as ErrorNumeroNegativo:

	print(ErrorNumeroNegativo)

print("Fin bueno")