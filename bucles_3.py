
"""
lista = [9,13,2,7,124,-5]
print (lista)
print(max(lista))
print(min(lista))
"""

lista = [9,13,2,7,124,-5]
print(lista)
print()
maximo = lista[0]
minimo = lista[0]

for elemento in lista:
 
    if elemento >= maximo:
        maximo = elemento
    
    if elemento <= minimo:
        minimo = elemento
        
print(f'el maximo es {maximo} y el minimo es {minimo}')
print(13 in lista)