
#clases y objetos

class Persona:
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludarPersona(self):
        print("Hola, mi nombre es " + self.nombre + " y tengo " + str(self.edad) + " años.")

person = Persona("Ligia",43)
person.saludarPersona()

#clases y objetos2

class Persona:
    nombre = ""
    edad = ""
    curp = ""

    def _init_(self, nom, ed, curp):
        self.nombre = nom
        self.edad = ed
        self.curp = curp

    def mostrarDatos(self):
        print(f'Hola {self.nombre} tienes {self.edad} años y tu curp es: {self.curp}')


objetoPersona = Persona('Ligia', 42, 'CURP')
objetoPersona.mostrarDatos()

#ejemplo persona 1

#Se crea una clase, se declara tres atributos y dos métodos, luego se instancia un objeto de esa clase y se manda a  llamar a sus métodos,
# el primero se encarga de pedir los datos y el segundo de imprimirlos

class Persona:
    nombre = ""
    edad = ""
    curp = ""

    def pedirDatos(self):
        self.nombre = input('Ingrese su nombre ')
        self.edad = int(input('Ingrese su edad: '))
        self.curp = input('Ingrese su curp: ')

    def mostrarDatos(self):
        print(f'Hola {self.nombre} tienes {self.edad} años y tu curp es: {self.curp}')


objetoPersona = Persona()
objetoPersona.pedirDatos()
objetoPersona.mostrarDatos()


#ejemplo persona 2

#Se utiliza el constructor para pedir los datos, como ves el constructor no tiene que ser llamado se invoca solito
# cuando creamos la instancia de la clase.
class Persona:
    nombre = ""
    edad = ""
    curp = ""

    def _init_(self):
        self.nombre = input('Ingrese su nombre ')
        self.edad = int(input('Ingrese su edad: '))
        self.curp = input('Ingrese su curp: ')

    def mostrarDatos(self):
        print(f'Hola {self.nombre} tienes {self.edad} años y tu curp es: {self.curp}')


objetoPersona = Persona()
objetoPersona.mostrarDatos()