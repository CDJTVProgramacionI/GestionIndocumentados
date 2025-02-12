from Registro.Personas import Persona
from dataclasses import dataclass
from Registro.Estructuras.listaDobleDinamica import DoubleLinkedList
from Registro.Estructuras.listaSimpleDinamica import LinkedList



#ASESOR LEGAL
@dataclass
class AsesorLegal:
    #ATRIBUTOS
    __nombreasesor: str
    __disponibilidad: bool

    #CONSTRUCTOR
    def __init__(self, nombre, disponibilidad=True):
        self.__nombre = nombre
        self.__disponibilidad = disponibilidad ###inicialmente el asesor está disponible
        
    def set_disponibilidad(self, disponibilidad):
        self.__disponibilidad = disponibilidad
                
    def esta_disponible(self):
        return self.__disponibilidad



@dataclass
class Refugio:
    #ATRIBUTOS
    nombre: str  # Nombre del refugio
    capacidad: int
    ocupantes: list

    #CONSTRUCTOR
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.ocupantes = []

    #MÉTODOS
    def meterPersona(self, persona : Persona):
        if self.capacidad > len(self.ocupantes): ###Si el refugio (nodo) tiene capacidad disponible
                self.ocupantes.append(persona) ### agrega la persona al refugio
        else:
            raise ValueError("No hay capacidad en el refugio")
                
    def sacarPersona(self, id : str):
        i = 0
        for persona in self.ocupantes:
            if persona.id == id:
                self.ocupantes.pop(i)
                return    
            i += 1
            
        raise ValueError("La persona no está en el refugio")
                        

@dataclass
class Alimentos:
    #ATRIBUTOS
    #solo 1 atributo que es una lista de alimentos
    lista_alimentos: list

    #CONSTRUCTOR
    def __init__(self, lista_alimentos): 
        self.lista_alimentos = lista_alimentos


class Recursos:
    # Crear el arreglo de listas ligadas
    arreglo_listas = [LinkedList() for _ in range(3)] ###0=Asesor, 1=Refugio, 2=Alimentos
    lista_recursos_asignados = DoubleLinkedList() ###Lista para guardar los recursos asignados
    
    def __init__(self, nombre):
        self.nombre = nombre # Nombre del recurso
        
    def insertarRecurso(self, tipo_recurso : int, recurso : any):
        match tipo_recurso:
            case 0:
                self.arreglo_listas[0].insertAtEnd(recurso)
            case 1:
                self.arreglo_listas[1].insertAtEnd(recurso)
            case 2:
                self.arreglo_listas[2].insertAtEnd(recurso)
            case _:
                print("Error: Tipo de recurso no válido.")
                
    #agregar un metodo para asignar asesor que cambie la disponibilidad a false
    def asignarAsesor(self, persona : Persona):     
        #Hacer cabeza y siguiente publicos
        actual=self.arreglo_listas[0].cabeza ###Apunta al primer nodo de la lista en la posicion 0
        while actual: ###recorre mientras que el nodo no apunte a null (es decir mientras siga habiendo nodos)
            if actual.esta_disponible(): ###Si el asesor (nodo) está disponible
                actual.set_disponibilidad(False)
                print(f"El asesor {self.nombre} se ha asignado.")
                return #para que se salga de la funcion cuando encuentra algo
            actual=actual.siguiente #si no esta disponible, pasa al siguiente
            
            # Registrar en la lista doble
            self.lista_recursos_asignados.insertAtEnd({
                'persona': persona,
                'recurso': 'Asesoría Legal',
                'nombre_recurso': self.nombre
            })
            print(f"Se ha registrado la asesoría legal {self.nombre} para la persona {persona.nombre}.")
            
        #si no encontró asesores
        raise ValueError(f"Error: No hay asesores disponibles.")
    
    def liberarAsesor(self, nombre : str):
        a = AsesorLegal(nombre) #variable arbitraria para guardar el nombre
        asesor=self.arreglo_listas[0].search(a)#retorna none si no encuentra nada (no esta disponible)
        
        if asesor==None:
            raise ValueError(f"El asesor {asesor.nombre} no se encuentra.")
        else: 
            asesor.set_disponibilidad(True) ### lo libera cambiando la disponibilidad a true
            
    def asignarRefugio(self, persona: Persona):
        ###Recorrer la lista para asignar el primer refugio disponible (checando lo de capacidad)
        actual=self.arreglo_listas[1].cabeza ###Apunta al primer nodo de la lista en la posicion 0
        while actual: ###recorre mientras que el nodo no apunte a null (es decir mientras siga habiendo nodos)
            try:
                actual.meterPersona(persona)
                print(f"El refugio {actual.dato.nombre} le fue asignado a otra nueva persona.")
            except ValueError:
                actual=actual.siguiente
            
        #si no encontró ninguno con capacidad disponible
        raise ValueError(f"Error: No hay capacidad disponible en ningún refugio") 
    
    def liberarRefugio(self, nombre : str, persona: Persona):
        b = Refugio(nombre) #variable arbitraria para guardar el nombre
        refug=self.arreglo_listas[1].search(b)#retorna none si no encuentra nada (no esta disponible)
        
        if refug==None:
            raise ValueError(f"El refugio {refug.nombre} no se encuentra.")
        else:
            refug.sacarPersona()  

    def asignarAlimento(self, persona: Persona, lista_alimentos):
        ###Recorrer la lista para asignar el primer alimento disponible 
        alimentos = lista_alimentos[2].deleteAtBegin()
        if alimentos is None:
            raise ValueError("Error: No hay alimentos disponibles.")

        # Registrar en la lista doble
        self.lista_recursos_asignados.insertAtEnd({
            'persona': persona,
            'recurso': 'Alimentos',
            'nombre_recurso': self.nombre
        })
        print(f"Se ha registrado el paquete de alimentos {self.nombre} para la persona {persona.nombre}.")
