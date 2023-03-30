#INTENTO DE USO DE CLASES Y OBJETOS APLICADOS AL CODIGO
#FECHA: 20/02/23
#AUTOR: JUAN CARLOS ORTIZ SALAS

print()
print ("hola, este programa almacenará la informacion de un estudiante y devolvera un saludo de bienvenida")
print()


class estudiante :
    def __init__(self, nombre1, nombre2, apellido1, apellido2, edad, carrera) :

        self.nombre1=nombre1
        self.nombre2=nombre2
        self.apellido1=apellido1
        self.apellido2=apellido2
        self.edad=edad
        self.carrera=carrera
        
    def Nombre1(self) :
        return self.nombre1
    def Nombre2(self) :
        return self.nombre2
    def Apellido1(self) :
        return self.apellido1
    def Apellido2(self) :
        return self.apellido2
    def Edad(self) :
        return self.edad
    def Carrera(self) :
        return self.carrera

    def datos (self) :
        print(""" Hola, """+self.Nombre1(), self.Nombre2(), self.Apellido1(), self.Apellido2(), """ 
        es un honor para nosotros tenerte en nuestra institucion educativa, esperamos que disfrutes tu carrera como futuro: """, self.Carrera(),
        """. """, str(self.Edad()),""" años es una buena edad para aprender, te deseamos lo mejor en esta aventura llena de aprendizajes.""")


nombre1 = input(">porfavor, ingresa tu primer nombre: ")
print()
nombre2 = input(">porfavor, ingresa tu segundo nombre: ")
print()
apellido1 = input(">porfavor, ingresa tu primer apellido: ")
print()
apellido2 = input(">porfavor, ingresa tu segundo apellido: ")
print()
edad = input(">porfavor, ingresa tu edad: ")
print()
carrera = input(">porfavor, ingresa tu carrera:")
print()

if carrera == "ISIC":
    carrera="ISIC (Los mas duros del instituto)"
else :
    carrera=carrera


imp=estudiante(nombre1, nombre2, apellido1, apellido2, edad, carrera)
imp.datos()




