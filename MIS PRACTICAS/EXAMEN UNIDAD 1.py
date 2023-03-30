#EXAMEN UNIDAD 1 
#FECHA: 03/03/23
#AUTOR: JUAN CARLOS ORTIZ SALAS 

print("Hola, bienvenido al programa, esta vez elegiras entre calcular el promedio de un estudiante y el salario de un docente ")

#POLIFORMISMO, CLASES Y ATRIBUTOS
#INICIO POR IMPLEMENTAR POLIFORMISMO PARA QUE SALUDE AL USUARIO CON EL APODO QUE MAS LE GUSTE, 
class apodo:
    def __init__(self, apodo): 
        self.apodo=apodo

    def despedirse(self) :
        pass

#Esta clase returna el apodo junto con un print que despide al usuario con su apodo. 
class despedida(apodo):
    def despedirse(self) :
        return print("Adios ", self.apodo, " es un gusto que utilices nuestro programa")
    
#Fin del polimorfismo

#HERENCIA, CLASES Y ATRIBUTOS
#Luego implemento herencia para crear una clase padre que heredara los atributos de nombre y edad
    
class persona :
    def __init__(self, nom, edad):
        self.nom=nom
        self.edad=edad

    def result(self):
        return print("Hola ",self.nom, " tu edad es de: ", self.edad, " años")

#aqui creo las clases hijas, que llaman la la clase padre para heredar el nombre y edad con una clase super()

class estudiante (persona):
    def __init__(self, nom, edad, cal1, cal2, cal3) :
        super().__init__(nom, edad)
        self.cal1=cal1
        self.cal2=cal2
        self.cal3=cal3

    def result(self):
        super().result()
        return print("Y tu promedio es de: ", (self.cal1+self.cal2+self.cal3)/3)
    
    
class docente (persona):
    def __init__(self, nom, edad, sal, hor):
        super().__init__(nom, edad)
        self.sal=sal
        self.hor=hor

    def result(self):
        super().result()
        return print("Y tu salario semanal es :", (self.sal*self.hor))

#aqui terminan las clases que se usaran en el codigo y empiezo por llamar a la clase despedida para que el usuario ingrese su nombre 

apo=despedida(input("INGRESA EL APODO QUE MAS TE GUSTE--->"))

#Aqui inicio con imprimir las elecciones que puede tomar el usuario y posteriormente se lee la opcion que el usario desee

print ("Ingresa el tipo de dato que deseas ingresar y saber \n")
print("[1]ESTUDIANTE Y PROMEDIO  [2]DOCENTE Y SALARIO")

op=input("OPCION--->")

#con un if se inicia la eleccion del usuario 

if op == "1" :
    #se llaman las clases de poliformismo y herencia para darle al usuario su promedio y despedirse con el apodo que mas le guste
    p=estudiante(input("INGRESA TU NOMBRE-->"), int(input("INGRESA TU EDAD-->")), int(input("INGRESA TU CALIFICACION 1-->")), int(input("INGRESA TU CALIFICACION 2-->")), int(input("INGRESA TU CALIFICACION 3-->")) )
    p.result()
    print()
    apo.despedirse()
elif op == "2" :
    #Se llaman las clases de poliformismo y herencia para mostrar al docente su sueldo mensual y despedirse con el apodo que mas le guste
    p2= docente (input("INGRESA TU NOMBRE-->"), int(input("INGRESA TU EDAD-->")), float(input("INGRESA TU SALARIO POR HORA-->")), float(input("INGRESA LAS HORAS QUE TRABAJAS A LA SEMANA-->")))
    p2.result()
    print()
    apo.despedirse()




    




