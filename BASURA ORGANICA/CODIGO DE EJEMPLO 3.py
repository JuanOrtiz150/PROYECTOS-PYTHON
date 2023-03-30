#CODIGO PARA RESOLVER TABAS DE MULTIPLICAR
#FECHA: 16/02/23
#AUTOR: JUAN CARLOS ORTIZ SALAS

#MENU E INICIO

print()
print("Hola, hoy te enseñare las tablas de multiplicar dependiendo de cual elijas")
print("(tener en cuenta que las tablas de multiplicar van del 1 al 12 o en caso de que usted desee, \n tambien tener en cuenta que no se aceptan decimales)")

#ELECCION

print ("dependiendo de cual sea su necesidad elija la opcion que desee \n")
print ("(PRESIONE 1) TABLAS DE MULTIPLICAR DE 1X1 - 1X12")
print ("(PRESIONE 2) TABLAS DE MULTIPLICAR DE 1X1 - 1XN")
print ("(PRESIONE 3) TABLAS DE MULTIPLICAR DE 1X1 - 1XN NEGATIVAS \n")

opcion = (input("ELIJA LA OPCION QUE DESEE--->"))
print()

#VALIDAR QUE ESTE ENTRE LAS OPCIONES

while opcion != "1" and opcion != "2" and opcion != "3" :

    print("El valor ingresado no esta en las opciones, vuelva a intentar \n")

    opcion = (input("ELIJA LA OPCION QUE DESEE--->"))
    if opcion == "1" or opcion == "2" or opcion == "3" :
        continue

#INICIAR A MOSTRAR LAS TABLAS

if opcion == "1" :

    mul=input("INGRESE EL NUMERO DE LA TABLA QUE DESEE VER--->")
    

    #VALIDAR CON UN WHILE QUE EL VALOR NO SEA STRING

    while mul.isdigit() != True :
        print("el valor ingresado no es un entero, vuelva a intentar")
        mul = input("INGRESE EL NUMERO DE LA TABLA QUE DESEE VER--->")
        if mul.isdigit() == True :
            continue

    int_mul = int(mul)

    for i in range (1, 13) :
        print (int_mul," x ",i, " = ", int_mul*i)

elif opcion == "2" :
    print()

    mul=input("INGRESE EL NUMERO DE LA TABLA QUE DESEE VER--->")

    while mul.isdigit() != True:
        print("el valor ingresado no es un entero, vuelva a intentar")
        mul = input("INGRESE EL NUMERO DE LA TABLA QUE DESEE VER--->")
        print()
        if mul.isdigit() == True :
            continue

    int_mul = int(mul)

    print ()

    N=input("INGRESE EL RANGO MAXIMO DE FILAS QUE DESEA VER--->")

    while N.isdigit() != True:

        print("el valor ingresado no es un entero, vuelva a intentar")

        N = input("INGRESE EL NUMERO DE LA TABLA QUE DESEE VER--->")
        if N.isdigit() == True :
            continue

    int_N= int(N)

    for i in range (1, int_N+1) :
        print (int_mul," x ",i, " = ", int_mul*i)
elif opcion == "3" :
    print()

    mul=input("INGRESE EL NUMERO DE LA TABLA QUE DESEE VER--->")

    while mul.isdigit() != True:
        print("el valor ingresado no es un entero, vuelva a intentar")
        mul = input("INGRESE EL NUMERO DE LA TABLA QUE DESEE VER--->")
        print()
        if mul.isdigit() == True :
            continue

    int_mul = int(mul)
    int_mul = int_mul*-1

    print ()

    N=input("INGRESE EL RANGO MAXIMO DE FILAS QUE DESEA VER--->")

    while N.isdigit() != True:

        print("el valor ingresado no es un entero, vuelva a intentar")

        N = input("INGRESE EL NUMERO DE LA TABLA QUE DESEE VER--->")
        if N.isdigit() == True :
            continue

    int_N= int(N)

    for i in range (1, int_N+1) :
        print (int_mul," x ",i, " = ", int_mul*i)



print()
print("Gracias por usar este programa, hasta la proximaaaaaaaaaa *dupstep*")
















