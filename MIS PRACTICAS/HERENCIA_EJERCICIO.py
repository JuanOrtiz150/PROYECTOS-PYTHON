#APLICAR HERENCIA EN EL CODIGO
#FECHA:25/02/23
#AUTOR: JUAN CARLOS ORTIZ SALAS 

print ("""Hola, hoy ingresaremos algunos datos sobre tu manga favorito y tu comic favorito, 
dos tipos de forma de representar una historia grafica""")

class historia() :
    def __init__(self, nom, anio, editorial, autor) :
        self.nom=nom
        self.anio=anio
        self.editorial=editorial
        self.autor=autor

    def datos(self):
        print("Nombre de la obra: "+self.nom+" Año de publicacion: "+self.anio+" Editorial: "+self.editorial+" Autor: "+self.autor)

class manga(historia):
    def __init__(self, nom, anio, editorial, autor, tomos) :
        super().__init__(nom, anio, editorial, autor)
        self.tomos=tomos

    def datos(self):
        super().datos()
        print("numero de tomos: "+self.tomos)

class comic(historia):
    def __init__(self, nom, anio, editorial, autor, volumen) :
        super().__init__(nom, anio, editorial, autor)
        self.volumen=volumen

    def datos(self):
        super().datos()
        print("numero de volumenes: "+self.volumen)
print()
print("Ingresa los datos de tu manga favorito, en caso de no conocer algun dato dejalo vacio o escribe 0")
man=manga(input("INGRESA EL NOMBRE DE LA OBRA-->"), input("INGRESA EL AÑO DE LANZAMIENTO-->"), input("INGRESA LA EDITORIAL DE LA OBRA-->"), input("INGRESA EL AUTOR DE LA OBRA-->", ), input("INGRESA LA CANTIDAD DE TOMOS-->"))
print()
print("Ahora ingresa los datos de tu comic favorito")
com=comic(input("INGRESA EL NOMBRE DE LA OBRA-->"), input("INGRESA EL AÑO DE LANZAMIENTO-->"), input("INGRESA LA EDITORIAL DE LA OBRA-->"), input("INGRESA EL AUTOR DE LA OBRA-->", ), input("INGRESA LA CANTIDAD DE VOLUMENES-->"))
print()

print("Bueno, hora de ver los datos de tus obras favoritos")
man.datos()
print()
com.datos()