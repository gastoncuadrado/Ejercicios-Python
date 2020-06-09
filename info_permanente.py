import pickle

class Persona:

	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una persona con el nombre de: ", self.nombre)

	def __str__(self):
		return"{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

	personas=[]

	def __init__(self):

		listaDePersonas=open("ArchivoExterno.txt","ab+")
		listaDePersonas.seek(0)

		try:
			self.personas=pickle.load(listaDePersonas)
			print("Se cargaron {} personas del archivo externo".format(len(self.personas)))

		except:
			print("archivo vacio")

		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnArchivo()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasEnArchivo(self):
		listaDePersonas=open("ArchivoExterno.txt","wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarInfoArchivo(self):
		print("El archivo contiene:")
		for p in self.personas:
			print (p)

miLista=ListaPersonas()
persona=Persona("Julio", "Masculino", 35)
miLista.agregarPersonas(persona)
miLista.mostrarInfoArchivo()