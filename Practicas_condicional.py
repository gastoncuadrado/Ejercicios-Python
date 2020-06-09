print("Asignaturas optativas  año 2020")
print("Informatica - Pruebas - Usabilidad")
opcion=input("Asignatura escogida ")

asignatura_elegida=opcion.lower()

if asignatura_elegida in ("informatica", "pruebas", "usabilidad"):

	print("Asignatura elegida "+ asignatura_elegida)

else:

	print("No contemplada")	