

class Persona:
    print('Persona creada')

    #metodo constructor..............
    def __init__(self,nom,ape,ed,ced):
        #atributos
        #atributos de instancia
        self.nombre = nom
        self.apellido = ape
        self.edad= ed
        self.cedula= ced
def crearPersona():
    print('Digite su nombre:')
    nom=input()
    print('Digite su Apellido:')
    ape = input()
    print('Digite su Edad:')
    ed = input()
    print('Digite su cedula:')
    ced = input()
    p= Persona(nom,ape,ed,ced)
    return p

def imprimePersona(x):
        print('Nombre:',x.nombre)
        print('Apellido:', x.apellido)
        print('Edad:', x.edad)
        print('Cedula:', x.cedula)


#Creacion de un objeto
#Juan= Persona()
#imprime(Juan)

#x=crearPersona()
#imprimePersona(x)


#----------------------ANIMAL--------------------------


class Animal:
    print('Animal Creado')

    #metodo constructor..............
    def __init__(self,esp,nom,ed):

        self.especie = esp
        self.nombre = nom
        self.edad= ed


def crearAnimal():
    print('Digite su Especie:')
    esp = input()
    print('Digite su nombre:')
    nom=input()
    print('Digite su Edad:')
    ed = input()
    a= Animal(esp,nom,ed)
    return a

def imprimeAnimal(x):
        print('Especie:',x.especie)
        print('Nombre:', x.nombre)
        print('Edad:', x.edad,'años')

def creceAnimal(x):
    eda= x.edad
    e=x.especie
    n= x.nombre
    eda= int(eda)+ 3
    print('El animal es mas viejo')
    print('Nueva informacion del animal:  ')
    h=Animal(e,n,eda)
    imprimeAnimal(h)


#--------------------------------PLANTA----------------------------------

class Planta:

    #metodo constructor..............
    def __init__(self,nom,est,alt):

        self.nombre = nom
        self.estado = est
        self.altura= alt



def crearPlanta():
    print('Digite el nombre de la planta:')
    nom=input()
    print('Digite su Altura:')
    alt = input()
    est='Viva'
    p= Planta(nom,est,alt)
    return p

def imprimePlanta(x):
        print('Nombre:',x.nombre)
        print('Estado:', x.estado)
        print('Altura:', x.altura,'cm')
        print('\n\n')
def regarPlanta(x):
    alt= x.altura
    est='Muerta'
    n= x.nombre
    alt= int(alt)+ 30
    print('Regamos la planta....')
    print('La planta crece....')
    print('Nueva altura de la planta:')
    print(alt,'cm')
    print('La planta envejece y luego muere')
    print('Nueva informacion de la planta:\n  ')
    p=Planta(n,est,alt)
    imprimePlanta(p)




print('---------------ejercicio animal -------------')
a=crearAnimal()
imprimeAnimal(a)
print('---------------el animal crece -------------')

creceAnimal(a)
print('---------------ejercicio planta -------------')
pl=crearPlanta()
imprimePlanta(pl)
print('---------------regamos la planta -------------')
regarPlanta(pl)