valido=False

email=(input("Introduce Email: "))

for i in range(len(email)):
	if email[i]=="@":
		valido=True

if valido:
	print("Email correcto")
else:
	print("Email incorrecto")

input("Presione para continuar")
