#from databasebuild import insertRow
#from databasebuild import readRow

class Arbol:
    def __init__(self, carga=None, izq=None, der=None):
        self.carga = carga
        self.izquierda = izq
        self.derecha = der
         
    def __str__(self):
        return str(self.carga)
 
 
def si(preg):
    resp = str.lower(input(preg))
    return (resp[0] == 's')
 
 
def main(): 

    bucle = True
    raiz = Arbol("Aragorn")
    while bucle:
        if not si("¿Estas pensando en alguien? "): break
         
        arbol = raiz
        while arbol.izquierda != None:
            if si("¿Es " + arbol.carga + "?"):
                arbol = arbol.izquierda
            else:
                arbol = arbol.derecha
         
        personaje = arbol.carga
        if si("Es " + personaje + " ¿Cierto? "):
            print ("¡No puedes proteger tu mente del señor sauron!")
            continue
         
        nuevo = input("¿Qué personaje era? ")
        info = input("¿Qué diferencia a " + personaje + " de " + nuevo + "? ")
        indicador = "Si el personaje fuera " + personaje + " ¿cual seria la respuesta?"
        arbol.carga = info
        #if indicador=='si' or indicador=='Si' or indicador=='Si' or indicador=='sI':
            #insertRow(personaje, info)
        #else:
            #insertRow(nuevo, info)
            
        if si(indicador):
            arbol.izquierda = Arbol(personaje)
            arbol.derecha = Arbol(nuevo)
        else:
            arbol.derecha = Arbol(personaje)
            arbol.izquierda = Arbol(nuevo)

    return 0
 
if __name__ == '__main__':
    main()