#PRACTICA 10/02/23 
#EJEMPLO 2, PROGRAMAR QUE EL USUARIO TE DE UNA EDAD Y DEPENDIENDO DE ESTA DIRA SI ERES MENOR O MAYOR DE EDAD O ESTAS EN 65 O MAS
#AUTOR:JUAN CARLOS ORTIZ SALAS
print("Hola, el dia de hoy ingresaras tu edad y dependiendo de esta te dire si eres mayor de edad, menor o si tienes 65 o mas")
edad=int(input("Ingresa tu edad: "))
if edad<18:
    print("Eres menor de edad")
else:
    if edad>17 and edad<65:
        print("Eres mayor de edad")
    else:
        if edad>=65 :
            print("Estas en el rango para tener el programa de 65 y mas")
print("Gracias por usar el programa, hasta luego C:")