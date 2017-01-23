import sqlite3

conexion = sqlite3.connect("usuarios_auto.db")
cursor = conexion.cursor()

cursor.execute("UPDATE usuarios SET nombre='Miguel Galiana', edad = 33 WHERE dni='47606707L'")





conexion.commit()
conexion.close()