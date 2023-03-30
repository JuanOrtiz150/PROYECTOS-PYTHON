#CODIGO PARA AYUDAR EN ALGUNOS PROBLEMAS QUE USEN FRACCIONES
#FECHA:11/02/23
#AUTOR: JUAN CARLOS ORTIZ SALAS

#***INICIO Y ELECCION***

print ("")
print ("Hola, te ayudare a sumar, restar, muliplicar o dividir fracciones, de una forma interactiva")
print ("")
eleccion = ["(1)SUMAR", "(2)RESTAR", "(3)MULTIPLICACION", "(4)DIVISION"]
print ("")

for names in eleccion :
    print (names)

print("")
op = str(input("ELIJA LA OPCION QUE DESEE REALIZAR--->"))

#VALIDAR LA ELECCION

while op != "1" and op != "2" and op != "3" and op != "4" :
    print ("EL valor seleccionado no esta entre las opciones, vuelva a intentar")
    op = str(input ("ELIJA LA OPCION QUE DESEE REALIZAR--->"))
    if op == "1" and op == "2" and op == "3" and op == "4" :
        continue 

#IF ANIDADO

if op == "1" :
    print("Usted eligio resolver Suma")
    print ("")
    print("FRACCION 1")
    num1 = int (input ("Ingrese el valor del numerador--->"))
    den1 = int (input ("Ingrese el valor del denominador--->"))
    print ("")
    print("FRACCION 2")
    num2 = int (input ("Ingrese el valor del numerador--->"))
    den2 = int (input ("Ingrese el valor del denominador--->"))
    print("")

    num3 = ((num1*den2)+(num2*den1))
    den3 = (den1*den2)

    print ("El resultado es: ", num3, "/", den3)
elif op == "2" :
    print("Usted eligio resolver Resta")
    print ("")
    print("FRACCION 1")
    num1 = int (input ("Ingrese el valor del numerador--->"))
    den1 = int (input ("Ingrese el valor del denominador--->"))
    print ("")
    print("FRACCION 2")
    num2 = int (input ("Ingrese el valor del numerador--->"))
    den2 = int (input ("Ingrese el valor del denominador--->"))
    print("")

    num3 = ((num1*den2)-(num2*den1))
    den3 = (den1*den2)

    print ("El resultado es: ", num3, "/", den3)
elif op == "3" :
    print("Usted eligio resolver Multiplicacion")
    print ("")
    print("FRACCION 1")
    num1 = int (input ("Ingrese el valor del numerador--->"))
    den1 = int (input ("Ingrese el valor del denominador--->"))
    print ("")
    print("FRACCION 2")
    num2 = int (input ("Ingrese el valor del numerador--->"))
    den2 = int (input ("Ingrese el valor del denominador--->"))
    print("")

    num3 = (num1*num2)
    den3 = (den1*den2)

    print ("El resultado es: ", num3, "/", den3)
elif op == "4" :
    print("Usted eligio resolver Division")
    print ("")
    print("FRACCION 1")
    num1 = int (input ("Ingrese el valor del numerador--->"))
    den1 = int (input ("Ingrese el valor del denominador--->"))
    print ("")
    print("FRACCION 2")
    num2 = int (input ("Ingrese el valor del numerador--->"))
    den2 = int (input ("Ingrese el valor del denominador--->"))
    print("")

    num3 = (num1*den2)
    den3 = (den1*num2)

    print ("El resultado es: ", num3, "/", den3)

print("gracias por usar este programa")













