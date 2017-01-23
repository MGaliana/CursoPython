import sqlite3

conexion = sqlite3.connect("usuarios_auto.db")
cursor = conexion.cursor()

#cursor.execute('''
#	CREATE TABLE usuarios (
#		dni VARCHAR(9) PRIMARY KEY,
#		nombre VARCHAR(100),
#		edad INTEGER,
#		email VARCHAR(100)
#	)
#	''')

#usuarios = [
#	("47606707L","Miguel",32,"miguel@ejemplo.com"),
#	("11111111A","Mario",51,"mario@ejemplo.com"),
#	("22222222B","Rafa",35,"rafa@ejemplo.com"),
#	("33333333C","Oscar",25,"oscar@ejemplo.com"),
#]

#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

#cursor.execute( "INSERT INTO usuarios VALUES ( '44444444D','MiguelA',33,'miguel01@ejemplo.com' )" )

#cursor.execute('''
#	CREATE TABLE productos(
#		id INTEGER PRIMARY KEY AUTOINCREMENT,
#		nombre VARCHAR(100) NOT NULL,
#		marca VARCHAR(50) NOT NULL,
#		precio FLOAT NOT NULL
#	)
#	''')

#productos = [
#	('Teclado','Logitec', 19.85),
#	('Pantalla','LG', 89.95)
#]
#cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

#cursor.execute("SELECT * FROM productos")

#productos = cursor.fetchall()
#for producto in productos:
#	print(producto)

cursor.execute('''
	CREATE TABLE usuarios(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		dni VARCHAR(9) UNIQUE,
		nombre VARCHAR(100),
		edad INTEGER,
		email VARCHAR(100)
	)
	''')

usuarios = [
	("47606707L","Miguel",32,"miguel@ejemplo.com"),
	("11111111A","Mario",51,"mario@ejemplo.com"),
	("22222222B","Rafa",35,"rafa@ejemplo.com"),
	("33333333C","Oscar",25,"oscar@ejemplo.com"),
]

cursor.executemany("INSERT INTO usuarios VALUES (null,?,?,?,?)", usuarios)


conexion.commit()
conexion.close()