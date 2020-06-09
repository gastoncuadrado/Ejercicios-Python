class Persona():
	
	def __init__(self, nombre, edad, lugar_residencia):
	
		self.nombre=nombre

		self.edad=edad

		self.lugar_residencia=lugar_residencia
		
	def descripcion(self):
		
		print("Nombre: ", self.nombre, "Edad: ", self.edad, "Residencia: ", self.lugar_residencia)


class Empleado(Persona):
		
	def __init__(self, salario, antiguedad, nombre_Empleado, edad_empleado, residencia_empleado):

		super().__init__(nombre_Empleado, edad_empleado, residencia_empleado)

		self.salario=salario

		self.antiguedad=antiguedad

	def descripcion(self):

		super().descripcion()

		print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad)

Manuel=Persona("Manuel", 55, "Colombia")

Manuel.descripcion()

print(isinstance(Manuel, Empleado))