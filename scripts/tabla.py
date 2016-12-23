import sys

if len(sys.argv) == 3:
	fila = int(sys.argv[1])
	columnas = int(sys.argv[2])

	if fila < 1 or fila > 9 or columnas < 1 or columnas > 9:
		print("Error - Filas o columnas incorrectos")
	else:
		#logica
		for f in range(fila):
			print("")
			for c in range(columnas):
				print(" * ", end= '')


else:
	print("Error Argumento incorrecto")

