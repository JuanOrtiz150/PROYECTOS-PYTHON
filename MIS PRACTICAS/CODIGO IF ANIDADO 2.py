#CODIGO PARA AYUDAR EN ALGUNOS PROBLEMAS MATEMATICOS, NCLUYENDO RAMAS COMO EL CALCULO, ALGEBRA BASICA Y FORMULA GENERAL
#FECHA:11/02/23
#AUTOR: JUAN CARLOS ORTIZ SALAS

#***INICIO Y ELECCION***

print ("")
print("Hola, te ayudare a resolver alguna de las siguientes operaciones dependiendo de cual elijas")
print("")
print("******Para elegir presione el numero de la opcion que desee******")
print("")
opciones = ["(1)FORMULA GENERAL" , "(2)INTEGRAL SENCILLA"]
for names in opciones:
    print(names)

print("")

op = str(input("INGRESA LA OPCION QUE DESEAS REALIZAR----->"))

#VALIDAR QUE EL VALOR INGRESADO ESTE ENTRE LAS OPCIONES

while op != "1" and op != "2" :
    print("El valor seleccionado no esta entre las opciones, vuelva a ingresar")
    op=str(input("INGRESA LA OPCION QUE DESEAS REALIZAR----->"))
    print ("")
    if op == "1" and op == "2" :
        continue

#IF ANIDADO

if op == "1" :

    #(OPCION 1) FACTORIZAR POR FORMULA GENERAL

    print("Eligio resolver por formula general")
    print("***importante***")
    print("Tener en cuenta que la factorizacion es de la forma ax2 + bx + c, por lo que si no tiene el valor de c escriba 0")

    #ELEGIR VALORES DE A B Y C

    a = int(input("Ingrese el valor de a----->"))
    while a == 0 :
        print("No se puede tener un valor 0 en a, de ese modo no se podria factorizar, ingrese de nuevo")
        print("")
        a = int(input("Ingrese el valor de a----->"))
        if a > 0 or a < 0 :
            continue
    print ("")
    b = int (input("Ingrese el valor de b----->"))
    print("")
    c = int (input("Ingrese el valor de c----->"))

    fgp = (-b + ((b**2) - (4*a*c))**(1/2))/(2*a)
    fgn = (-b - ((b**2) - (4*a*c))**(1/2))/(2*a)

    #RESULTADOS DE LA FORMULA GENERAL

    print ("X1 = ", fgp)
    print ("X1 = ", fgn) 
    print ("")
else:
    if op == "2" :

        print ("")

        #(OPCION 2) RESOLVER UNA INTEGRAL SENCILLA DE LA FORMA X^n

        print ("Eligio resolver una integral indefinida sencilla")
        print ("Recuerda que la integral se resolvera de la forma X^n")

        #ELEGIR VALORES PARA RESOLVER

        x1 = int (input("Ingrese un valor para x------>"))
        print("")
        n = int (input("Ingrese un valor para n------>"))

        #RESOLVER LA INTEGRAL

        if x1 == 1 and n > 0 :
            print ("El resultado es: x^", n+1, " / ", n+1, " + C")
        elif n == 0 :
            print ("El resultado es: x + C")
        elif x1 != 0 and n != 0 and n != -1 :
            print ("El resultado es:  ", x1, "x^", n+1, " / ", n+1)
        elif x1 == 0 and n == 0 :
            print ("El resultado es: C")
        elif x1 == 1 and n == -1 :
            print ("El resultado es: ln |x| +C")
        elif x1 != 1 and n == -1 : 
            print ("El resultado es: ", x1, " ln |x| + C")
        else:
            print ("La integral no esta definida")

print ("")        
print ("Gracias por usar este programa :D")
print("")


