from io import open

archivo_texto=open("archivo.txt","r+") #lectura y escritura

archivo_texto.seek(len(archivo_texto.readline()))

print(archivo_texto.read())