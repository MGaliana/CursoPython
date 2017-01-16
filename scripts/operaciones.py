def suma(a,b):
	try:
		r = a + b
	except TypeError:
		print("Error: Tipo de datos no valido")
	else:
		return r

def resta(a,b):
	try:
		r = a - b
	except TypeError:
		print("Error: Tipo de datos no valido")
	else:
		return r

def producto(a,b):
	try:
		r = a * b
	except TypeError:
		print("Error: Tipo de datos no valido")
	else:
		return r

def division(a,b):
	try:
		r = a / b
	except TypeError:
		print("Error: Tipo de datos no valido")
	except ZeroDivisionError:
		print("Error: No Es posible dividir por cero")
	else:
		return r