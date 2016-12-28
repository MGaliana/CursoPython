class Pelicula:
    #COnsturctor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Seha creado una Peli", self.titulo)
        
    #Destructor de clase
    def __del__(self):
        print("Se borra la pelicula",self.titulo)
p = Pelicula ("El Padrino", 175,1972)
del(p)