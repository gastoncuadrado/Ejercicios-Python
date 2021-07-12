
"""

lista = [9,13,2,7,124,-5]
print(7 in lista)

"""

lista = [9,13,2,7,124,-5]
print(lista)

try:
    elementobuscado=int(input('Ingrese elemento a buscar: '))
    existe=False
    for elemento in lista:
        print(f'buscando el eleento {elemento}')
        if elemento == elementobuscado:
            existe = True
    
    if existe == True: 
        print('el elemento buscado existe')
    else:
        print('el elemento buscado NO existe')
    
except Exception:
    print("solo se admite enteros")
