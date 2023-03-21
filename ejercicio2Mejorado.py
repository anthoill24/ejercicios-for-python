def promedio_por_genero(genero):
	cantidad = int(input(f"ingrese la cantidad de {genero}s:  "))
	promedio = 0 
	suma = 0

	for i in range(cantidad):
		edad = int(input(f"edad tinene el/la {genero} {str(i+1)}: "))
		suma += edad

	promedio = suma / cantidad
	print(f"El promedio de edades de {genero}s es de {promedio}")

promedio_por_genero('hombre')
print('---------------------------------------')
promedio_por_genero('mujer')