#APLICAR POLIFORMISMO EN UN CODIGO 
#FECHA: 26/02/23
#AUTOR: JUAN CARLOS ORTIZ SALAS

print("Hola, hoy te dire la capital de tu pais dependiendo de donde seas \n")

class pais:
    nom=""
    def __init__(self):
        self.nom=input("POR FAVOR INGRESE SU NOMBRE--->")

    def decir(self):
        pass

class mexico(pais):
    def decir(self):
        return ("Hola, ", self.nom, "La capital de Mexico es CDMX")

class usa(pais):
    def decir(self):
        return ("Hola, ", self.nom, "La capital de Estados Unidos es Washington D.C.")

class canada(pais):
    def decir(self):
        return ("Hola, ", self.nom, "La capital de canada es Ottawa")
    
class japon(pais):
    def decir(self):
        return ("Hola, ", self.nom, "La capital de japon es Tokyo")
    
class SurCor(pais):
    def decir(self):
        return ("Hola, ", self.nom, "La capital de Corea del sur es Seul")
    
class rusia(pais):
    def decir(self):
        return ("Hola, ", self.nom, "La capital de Rusia es Moscu") 
    
class china(pais):
    def decir(self):
        return ("Hola, ", self.nom, "La capital de China es Pekin") 
    
class brazil(pais):
    def decir(self):
        return ("Hola, ", self.nom, "La capital de Brazil es Brazilia")
    
print (" \n")
print ("[1]MEXICO        [2]ESTADOS UNIDOS")
print ("[3]CANADA        [4]JAPON")
print ("[5]COREA DEL SUR [6]RUSIA")
print ("[7]CHINA         [8]BRAZIL")
print ("")

op=0
while True:
    try:
        op=int(input("INGRESA TU PAIS--->"))
        break
    except ValueError:
        print("\n valor no encontrado, por favor seleccione escribiendo un numero de la lista")
    except op<1 :
        print("\n valor no encontrado, por favor seleccione escribiendo un numero de la lista")

if op==1 :
    nom=mexico()
    print(nom.decir()) 
elif op==2 :
    nom=usa()
    print(nom.decir())
elif op==3 :
    nom=canada()
    print(nom.decir())
elif op==4 :
    nom=japon()
    print(nom.decir())
elif op==5 :
    nom=SurCor()
    print(nom.decir())
elif op==6 :
    nom=rusia()
    print(nom.decir())
elif op==7 :
    nom=china()
    print(nom.decir())
elif op==8 :
    nom=brazil()
    print(nom.decir())
