class Persona:
    nombre=''
    edad=''
    def __init__ (self, nombre, edad):
        self.nombre=nombre
        self.edad=edad

        #Aqui se comienza con herencia

class estudiante(Persona):
    nombre=""
    edad=""
    carrera=""
    materia1=""
    caliT1=""
    caliT2=""
    caliT3=""

    def __init__(self, nombre, edad, carrera, materia1, caliT1, caliT2, caliT3):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.materia1=materia1
        self.caliT1=caliT1
        self.caliT2=caliT2
        self.caliT3=caliT3


    def mostrardatos(self):
        return print(f'Hola {self.nombre} tienes {self.edad} años y tu primera calificacion en la materia de: {(self.caliT1+self.caliT2+self.caliT3)/3}' )

p=estudiante(input(), input(), input(), input(), int(input()), int(input()), int(input()))
p.mostrardatos()

class docente (Persona):
    nombre=""
    edad=""
    carrera=""
    salario=""
    horas=""
    

    def __init__(self, nombre, edad, carrera, salario, horas,):
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.salario=salario
        self.horas=horas
        


    def mostrardatos(self):
        return print(f'Hola {self.nombre} tienes {self.edad} años y tu salario es de: {(self.salario * self.horas)/3}' )

