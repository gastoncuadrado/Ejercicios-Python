
"""

lista=[4,1,4,2,3] 
suma=0 
for elemento in lista: 
    if elemento%2 == 0: 
        suma = suma + elemento
        print(suma)

print("son", len(lista),"elementos")

promedio=suma/len(lista)
print(f'el promedio es {promedio}')

"""
lista = [9,13,2,7,124,-5]


cantidad=0
acumulador=0
promedio=0
for elemento in lista:
    cantidad=cantidad + 1
    acumulador=acumulador + elemento
    print(f'el elemento en la posición {cantidad} es {elemento}')
print()    
print(f'la cantidad de elementos es {cantidad}')
print(f'la suma de los elementos es {acumulador}')
print(f'el prmedio de los elementos es {(acumulador/cantidad)}')