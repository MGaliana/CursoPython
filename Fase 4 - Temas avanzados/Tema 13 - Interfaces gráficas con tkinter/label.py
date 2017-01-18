from tkinter import *


# Configuración raiz
root = Tk()
"""
# Variables dinamicas
texto = StringVar()
texto.set("Un Nuevo texto")


Label(root, text="Hola Mundo").pack(anchor="nw")
label = Label(root, text="Otra etiqueta")
label.pack(anchor="center")
Label(root, text="Tres etiqueta").pack(anchor="se")


label.config(bg="green", fg="blue", font=("Verdana", 24))
label.config(textvariable=texto)
"""
imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")
# Bucle aplicación
root.mainloop()