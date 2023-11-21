class Arbol:
    def __init__(self, carga=None, izq=None, der=None):
        self.carga = carga
        self.izquierda = izq
        self.derecha = der

    def __str__(self):
        return str(self.carga)


def principal():
    bucle = True
    raiz = Arbol("gato")
    while bucle:
        print("PIENSA EN UN ANIMAL")
        if (not si("Estas pensando en un animal? > ")):
            break
        arbol = raiz
        while arbol.izquierda != None:
            if si(arbol.carga + "? > "):
                arbol = arbol.izquierda
            else:
                arbol = arbol.derecha
        # adivinar
        animal = arbol.carga
        if si("Es un " + animal + " ? > "):
            print("He adivinado, soy el mejor")
            continue
        # obtener informacion
        nuevo = input("que animal era? > ")
        info = input("Que caracteristica diferenica un " +
                     animal + " de un " + nuevo + "? > ")
        indicador = "Si el animal fuera un " + nuevo + " cual seria la respuesta? > "
        arbol.carga = info
        if si(indicador):
            arbol.derecha = Arbol(animal)
            arbol.izquierda = Arbol(nuevo)
        else:
            arbol.izquierda = Arbol(animal)
            arbol. derecha = Arbol(nuevo)

    recorrer(input("desea recorrer el arbol? > "), raiz)
    return 0


def si(preg):
    resp = (input(preg))
    return (resp[0] == "s" or resp[0] == "S")


def recorrer(resp, raiz):
    if (resp[0] == 's' or resp[0] == 'S'):
        posorden(raiz)


def posorden(raiz):
    if (raiz == None):
        return None
    else:
        posorden(raiz.izquierda)
        print(raiz)
        posorden(raiz.derecha)


if __name__ == '__main__':
    principal()
