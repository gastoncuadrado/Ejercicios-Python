
"""
Created on Sun Jul 11 20:49:21 2021P

Crea una variable de nombre par de tipo cadena que contenga todos los 
numeros pares del 1 al 86 concatenados uno detrás de otro
 (tipo "24681012....") y una variable de nombre impar también de tipo cadena 
 que contenga los impares
 
"""

"""
listaimpares=list(range(1, 86, 2))
listapares=list(range(2, 87, 2))
print(f'lista de impares {listaimpares}')
print()
print(f'lista de pares {listapares}')
"""
cadenapar=""
cadenaimpar=""
for elemento in range(1, 87):
    if elemento%2 == 0:
        cadenapar = cadenapar + str(elemento) + " "
    if elemento%2 != 0:
        cadenaimpar = cadenaimpar + str(elemento) + " "
        
print("los numeros pares son: "+ cadenapar)
print()
print("los numeros pares son: "+ cadenaimpar)