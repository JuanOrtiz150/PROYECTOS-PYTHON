#ENCAPSULAMIENTO APLICADO A UN CODIGO DE PYTHON
#FECHA: 26/02/23
#AUTOR: JUAN CARLOS ORTIZ SALAS

print ("Hola, el dia de hoy te ayudare a logearte y decidir entra algunas opciones")

class usuario :
    def __init__(self, nom, contra) :
        self.nom=nom
        self.__contra=contra

    def get_contra (self):
        return self.__contra
    
    def set_contra (self, nueva_contra) :
        if nueva_contra == self.__contra :
            print ("la contraseña no puede ser la misma")
        else :
            self.__contra=nueva_contra
            print ("¡contraseña cambiada con exito!")

p=usuario(input("INGRESE SU NOMBRE-->"), input("INGRESE SU CONTRASEÑA-->"))

print("Hola, "+ p.nom+ " es un gusto ")
print ("Su contraseña se establecio como: "+ p.get_contra())
print("")
print("¿QUE DESEA HACER?")
print("[1]TE CUENTO LA HISTORIA DE TERROR MAS CORTA DEL MUNDO [2]TE CANTO FELIZ CUMPLEAÑOS [3]CAMBIAR CONTRASEÑA \n")

op="1"
op=input("Elija la opcion que mas desee-->")

while op != "1" and op != "2" and op != "3" :
    print("La opcion no esta en el rango de opciones, vuelva a intentar")
    op=input("Elija la opcion que mas desee-->")
    cont=cont+1
    if cont == 5 :
       print ("¡vamos, no es tan dificil! \n")
if op == "1" :
    print("")
    print(""" "El último hombre sobre la tierra estaba sentado solo en una habitación. 
    De repente, tocan a la puerta". """)
elif op == "2" :
    print("")
    print (" Cumpleaños feliz, cumpleaños feliz a "+ p.nom +", que los cumplas feliz") 
elif op == "3" :
    op3="1"
    while op3 != "2" :
        print("")
        print("Dato: La contraseña no puede ser la misma ")
        p.set_contra(input("INGRESE LA NUEVA CONTRASEÑA-->"))
        print("la contraseña es: "+p.get_contra())
        print ("\n ¿desea volver a intentar? [1] SI [2]NO")
        op3=input("ELIJA-->")


print ("\n Gracias por usar este codigo, hasta la proxima :)")


