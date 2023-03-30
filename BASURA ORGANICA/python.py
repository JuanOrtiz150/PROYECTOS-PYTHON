#EVALUACION DIAGNOSTICA
#PEDIR 10 NUMEROS Y CONTAR PARES E IMPARES
#PROGRAMA HECHO POR: Juan Carlos Ortiz Salas
print("Hola, dame 10 numeros y determinare cuales son pares e impares")
num= int(input ("holaaaaa")[:2])

cont=0
cont2=0
vector=[None]*10
for i in range (0, 10):
    print ("Dame un numero")
    vector[i]=int(input())
    if vector[i]!=0:
        num=vector[i]%2
        if num==0:
            cont=cont+1
        else:
            cont2=cont2+1
    else:
        while vector[i]==0:
            print("No se acepta el valor 0, ingrese de nuevo")
            vector[i]=int(input())
            if vector[i]!=0:
                num=vector[i]%2
                if num==0:
                   cont=cont+1
                else:
                   cont2=cont2+1
                continue
print("la cantidad de numeros pares es: ",cont)
print("la cantidad de numeros impares es: ",cont2)