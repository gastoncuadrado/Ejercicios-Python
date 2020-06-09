class Vehiculos():

	def __init__(self, marca, modelo):
		
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEnmarcha: ", 
			self.enmarcha, "\nacelerando : ", self.acelera, "\nFrenando: ", self.frena)


class Furgoneta(Vehiculos):
	
	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta esta cargada"
		else:
			return "La furgoneta esta vacia"

class Moto(Vehiculos):
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy a caballito"

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEnmarcha: ", 
			self.enmarcha, "\nacelerando : ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

class VElectricos(Vehiculos):
	def __init__(self, marca, modelo):

		super().__init__(marca, modelo)

		self.autonomia=100

	def CargarEnergia(self):
		
		self.cargando=True
		

miMoto=Moto("Honda", "CBR")

miMoto.caballito()

miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print (miFurgoneta.carga(True))

class BicicletaElectrica(VElectricos,Vehiculos):

	pass

miBici=BicicletaElectrica("Orbea", "XX300")
