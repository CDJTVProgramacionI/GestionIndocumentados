from Personas import Persona
from dataclasses import dataclass
from Estructuras.listaDobleDinamica import DoubleLinkedList
from Estructuras.listaSimpleDinamica import LinkedList


# Crear el arreglo de listas ligadas
arreglo_listas = [DoubleLinkedList() for _ in range(3)] ###0=Asesor, 1=Refugio, 2=Alimentos

lista_recursos_asignados = DoubleLinkedList() ###Lista para guardar los recursos asignados
#ASESOR LEGAL
@dataclass
class AsesorLegal:
#ATRIBUTOS
    nombreasesor: str
    disponibilidad: bool


    #CONSTRUCTOR
    def __init__(self, nombre, disponibilidad=True):
        self.nombre = nombre
        self.disponibilidad = disponibilidad ###inicialmente el asesor está disponible
            
        AsesorLegal1 = AsesorLegal("Asesor 1")
        AsesorLegal2 = AsesorLegal("Asesor 2")
        AsesorLegal3 = AsesorLegal("Asesor 3")

        ###Insertar datos de los Asesores en el arreglo de listas (en el indice 0, el del AsesorLegal)
        arreglo_listas[0].insertAtEnd(AsesorLegal1)
        arreglo_listas[0].insertAtEnd(AsesorLegal2)
        arreglo_listas[0].insertAtEnd(AsesorLegal3)
            
    #agregar un metodo para asignar asesor que cambie la disponibilidad a false
    def asignarAsesor(self, arreglo_listas):
        ###Recorrer la lista para asignar el primer asesor disponible
        actual=arreglo_listas[0].cabeza ###Apunta al primer nodo de la lista en la posicion 0
        while actual: ###recorre mientras que el nodo no apunte a null (es decir mientras siga habiendo nodos)
            if actual.dato.disponibilidad: ###Si el asesor (nodo) está disponible
                actual.dato.disponibilidad = False ### lo asigna cambiando la disponibilidad a false
                print(f"El asesor {actual.dato.nombre} se ha asignado.")
                return #para que se salga de la funcion cuando encuentra algo
            actual=actual.siguiente #si no esta disponible, pasa al siguiente
            
        #si no encontró asesores
        print(f"Error: No hay asesores disponibles.")
        


    #agregar otro metodo para liberar asesor que cambie la disponibilidad a true (PENDIENTE JOU)
#agregar otro metodo para liberar asesor que cambie la disponibilidad a true (PENDIENTE JOU)
def liberarAsesor(self, nombre):
    a = AsesorLegal(nombre) #variable arbitraria para guardar el nombre
    asesor=arreglo_listas[0].search(a)#retorna none si no encuentra nada (no esta disponible)
    
    if asesor==None:
        print(f"El asesor {asesor.nombre} no se encuentra.")
        return
    else: asesor.disponibilidad = True ### lo libera cambiando la disponibilidad a true


class recursos:
    def __init__(self, nombre):
        self.nombre = nombre # Nombre del recurso

    def asignarAsesoria(self, persona: Persona):
        if not self.disponibilidad:
            print(f"Error: La asesoría legal {self.nombre} no está disponible.")
            return
        #asignar asesor
        asesor = AsesorLegal()
        asesor.asignarAsesor(arreglo_listas)

        # Registrar en la lista doble
        lista_recursos_asignados.insertAtEnd({
            'persona': persona,
            'recurso': 'Asesoría Legal',
            'nombre_recurso': self.nombre
        })
        print(f"Se ha registrado la asesoría legal {self.nombre} para la persona {persona.nombre}.")

    def asignarAlimento(self, persona: Persona, lista_alimentos):
        ###Recorrer la lista para asignar el primer alimento disponible 
        alimentos = lista_alimentos[2].deleteAtBegin()
        if alimentos is None:
            print("Error: No hay alimentos disponibles.")
            return

        # Registrar en la lista doble
        lista_recursos_asignados.insertAtEnd({
            'persona': persona,
            'recurso': 'Alimentos',
            'nombre_recurso': self.nombre
        })
        print(f"Se ha registrado el paquete de alimentos {self.nombre} para la persona {persona.nombre}.")


#en refugio tiene que checar la capacidad y que sea mayor a 0,metodo para meter y sacar personas y revisar capacidad esto es para los 3 aseosres,comida y refugio

@dataclass
class Refugio:
    #ATRIBUTOS
    nombre: str  # Nombre del refugio
    capacidad: int
    ocupantes: int = 0

    #CONSTRUCTOR
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.ocupantes = 0

    #MÉTODOS
    # Crear tres refugios con una capacidad de 15 personas cada uno
    refugio1 = Refugio ("Refugio 1", 15)
    refugio2 = Refugio("Refugio 2", 15)
    refugio3 = Refugio("Refugio 3", 15) #pasar al main
    ###Insertar datos de los Refugios en el arreglo de listas (en el indice 1, el del Refugios)
    arreglo_listas[1].insertAtEnd(refugio1)
    arreglo_listas[1].insertAtEnd(refugio2)
    arreglo_listas[1].insertAtEnd(refugio3)

#revisa dany 
    def asignarRefugio(self, persona: Persona, arreglo_listas):
        ###Recorrer la lista para asignar el primer refugio disponible (checando lo de capacidad)
        actual=arreglo_listas[1].cabeza ###Apunta al primer nodo de la lista en la posicion 0
        while actual: ###recorre mientras que el nodo no apunte a null (es decir mientras siga habiendo nodos)
            if actual.dato.capacidad >= actual.dato.ocupantes: ###Si el refugio (nodo) tiene capacidad disponible
                actual.dato.ocupantes += 1 ### le suma otro ocupante al refugio
                print(f"El refugio {actual.dato.nombre} le fue asignado a otra nueva persona.")
                return
            actual=actual.siguiente #si no tiene capacidad disponible, pasa al siguiente
            
        #si no encontró ninguno con capacidad disponible
        print(f"Error: No hay capacidad disponible en ningún refugio")           


def liberarRefugio(self, nombre, persona: Persona):
    b = Refugio(nombre) #variable arbitraria para guardar el nombre
    refug=arreglo_listas[1].search(b)#retorna none si no encuentra nada (no esta disponible)
    
    if refug==None:
        print(f"El refugio {refug.nombre} no se encuentra.")
        return
    elif refug.ocupante <= 0: ###Si el refugio (nodo) ya no tiene ocupantes/personas
        print(f"Error: No hay ocupantes en el refugio {refug.nombre}.")
        return
    else:
        refug.ocupantes=0 ##se libera el refugio (sin tomar en cuenta la persona)
        return
    

@dataclass

class Alimentos:
    #ATRIBUTOS
    #solo 1 atributo que es una lista de alimentos
    lista_alimentos: list
    cantidad : int 

    #CONSTRUCTOR
def __init__(self, lista_alimentos): 
    self.lista_alimentos = lista_alimentos

    paquete1 = Alimentos(["Arroz", "Frijoles", "Aceite"])
    paquete2 = Alimentos(["Pasta", "Salsa de tomate", "Queso"]) #pasar al main
    paquete3 = Alimentos(["Pan", "Mermelada", "Leche"])
        
    ###Insertar datos de los Alimentos en el arreglo de listas (en el indice 2, el del Alimentos)
    arreglo_listas[2].insertAtEnd(paquete1)
    arreglo_listas[2].insertAtEnd(paquete2)
    arreglo_listas[2].insertAtEnd(paquete3)

        #falta lista circular para asesoria legal y refugio hasta que se resuelva el caso, tiene que tener un metodo de seguimiento
        #falta una clase seguimiento para guardar las listas circulares
