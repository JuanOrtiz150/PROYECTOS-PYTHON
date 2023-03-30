#EJERCICIO DE ABSTRACCION, QUE RESUELVE DOS TIPOS DE EJERCICIOS MATEMATICOS LLAMANDO A LA CLASE DE LA CUAL REQUIERA EL USUARIO
#FECHA: 28/02/23
#AUTOR: JUAN CARLOS ORTIZ SALAS

print("Hola, hoy te ayudare a resolver una division de fracciones o sumar dos valores")

class suma :
    def  __init__(self, num1, num2) :
        self.num1=num1
        self.num2=num2
    
    def sumar (self) :
        return self.num1+self.num2
    
class fraccion :
    def __init__(self, nume1, nume2, den1, den2) :
        self.nume1=nume1
        self.nume2=nume2
        self.den1=den1
        self.den2=den2
    
    def mul1 (self):
        return float(self.nume1*self.den2)
    def mul2 (self):
        return float(self.nume2*self.den1)


print("")
print ("[1] PARA HACER SUMA  [2]PARA HACER DIVISION DE FRACCIONES \n")
op=input("Ingresa tu eleccion-->")

while op != "1" and op != "2" :
    print("Dato fuera de las opciones, vuelva a intentar... \n")
    op=input("Ingresa tu eleccion-->")

if op=="1":
    
    print("Haz elegido realizar la suma")
    while True :
        try:
            p=suma(float(input("INGRESA EL PRIMER VALOR-->")), float(input("INGRESA EL SEGUNDO VALOR-->")))
            break
        except ValueError :
            print("valor erroneo, intenta de nuevo...")

    print ("El resultad de la suma es: "+p.sumar())

elif op=="2":
    print("Haz elegido la opcion de division de fracciones \n")
    while True:
        try:
            p=fraccion(float(input("Ingresa el primer numerador-->")), float(input("Ingresa el segundo numerador-->")), float(input("Ingresa el primer denominador-->")), float(input("Ingresa el segundo denominador-->")))
            break
        except ValueError :
            print("Valor no numerico ingresado, vuelva a intentar...")
    
    print("El resultado de la division de fracciones es: ", p.mul1(), "/", p.mul2())

print("Gracias por usar este codigo :D")

