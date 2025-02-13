from Registro.Personas import Persona
from dataclasses import dataclass
from Registro.Estructuras.listaDobleDinamica import DoubleLinkedList
from Registro.Estructuras.listaSimpleDinamica import LinkedList



#ASESOR LEGAL
@dataclass
class AsesorLegal:
    #ATRIBUTOS
    __nombre: str
    __disponibilidad: bool
    
    @property 
    def nombre(self):
        return self.__nombre

    #CONSTRUCTOR
    def __init__(self, nombre, disponibilidad=True):
        self.__nombre = nombre
        self.__disponibilidad = disponibilidad ###inicialmente el asesor está disponible
        
    def set_disponibilidad(self, disponibilidad):
        self.__disponibilidad = disponibilidad
                
    def esta_disponible(self):
        return self.__disponibilidad
    
    def __eq__(self, value):
        return self.nombre == value.nombre
    
    def __neq__(self, value):
        return self.nombre != value.nombre



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
        if self.tiene_espacio(): ###Si el refugio (nodo) tiene capacidad disponible
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
    
    def tiene_espacio(self):
        return self.capacidad > len(self.ocupantes)
    
    def __eq__(self, value):
        return self.nombre == value.nombre
    
    def __neq__(self, value):
        return self.nombre != value.nombre
                        

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
    alims_asignados = 0
        
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
        actual=self.arreglo_listas[0].head ###Apunta al primer nodo de la lista en la posicion 0
        while actual: ###recorre mientras que el nodo no apunte a null (es decir mientras siga habiendo nodos)
            if actual.data.esta_disponible(): ###Si el asesor (nodo) está disponible
                actual.data.set_disponibilidad(False)
                persona.asignar_asesor(actual.data.nombre) ###asigna el asesor a la persona
                print(f"El asesor {actual.data.nombre} se ha asignado a {persona.nombre}.")
                # Registrar en la lista doble
                self.lista_recursos_asignados.insertAtEnd(f"Se asignó el asesor {actual.data.nombre} a {persona.nombre}")
                return #para que se salga de la funcion cuando encuentra algo
            actual=actual.next #si no esta disponible, pasa al siguiente
            
        #si no encontró asesores
        raise ValueError(f"Error: No hay asesores disponibles.")
    
    def liberarAsesor(self, persona: Persona):
        a = AsesorLegal(persona.asesor) #variable arbitraria para guardar el nombre
        asesor=self.arreglo_listas[0].search(a)#retorna none si no encuentra nada (no esta disponible)
        
        if asesor is None:
            raise ValueError(f"El asesor {persona.asesor} no se encuentra.")
        else: 
            asesor.set_disponibilidad(True) ### lo libera cambiando la disponibilidad a true
            print(f"El asesor {asesor.nombre} ha sido liberado.")
            self.lista_recursos_asignados.insertAtEnd(f"Se liberó el asesor {asesor.nombre}")
            
    def asignarRefugio(self, persona: Persona):
        ###Recorrer la lista para asignar el primer refugio disponible (checando lo de capacidad)
        actual=self.arreglo_listas[1].head ###Apunta al primer nodo de la lista en la posicion 0
        while actual: ###recorre mientras que el nodo no apunte a null (es decir mientras siga habiendo nodos)
            try:
                actual.data.meterPersona(persona)
                persona.asignar_refugio(actual.data.nombre)
                print(f"El refugio {actual.data.nombre} le fue asignado a {persona.nombre}.")
                self.lista_recursos_asignados.insertAtEnd(f"Se asignó el refugio {actual.data.nombre} a {persona.nombre}")
                return
            except ValueError:
                actual=actual.next
            
        #si no encontró ninguno con capacidad disponible
        raise ValueError(f"Error: No hay capacidad disponible en ningún refugio") 
    
    def liberarRefugio(self, persona: Persona):
        b = Refugio(persona.refugio, 0) #variable arbitraria para guardar el nombre
        refug=self.arreglo_listas[1].search(b)#retorna none si no encuentra nada (no esta disponible)
        
        if refug is None:
            raise ValueError(f"El refugio {refug.nombre} no se encuentra.")
        else:
            try:
                refug.sacarPersona(persona.get_id())
                print(f"La persona {persona.nombre} fue sacada del refugio {refug.nombre}.")
                self.lista_recursos_asignados.insertAtEnd(f"Se liberó un espacio del refugio {refug.nombre}")
            except ValueError:
                print(f"La persona {persona.nombre} no está en el refugio {refug.nombre}.")
             

    def asignarAlimento(self, persona: Persona):
        ###Recorrer la lista para asignar el primer alimento disponible 
        alimentos = self.arreglo_listas[2].deleteAtBegin()
        if alimentos is None:
            raise ValueError("Error: No hay alimentos disponibles.")

        # Registrar en la lista doble
        self.lista_recursos_asignados.insertAtEnd(f"Se asignó {alimentos.lista_alimentos} a {persona.nombre}")
        
        self.alims_asignados += 1
        print(f"Se ha registrado el paquete de alimentos {alimentos.lista_alimentos} para la persona {persona.nombre}.")


    def __recursos_disp_asesores(self): 
        cant_de_asesores = 0
        actual=self.arreglo_listas[0].head
        while actual: 
            if actual.data.esta_disponible(): 
                cant_de_asesores+=1

            actual=actual.next
        
        return cant_de_asesores

    def __recursos_disp_alimentos(self):
        numpaquetes= self.arreglo_listas[2].len
        return numpaquetes

    def __recursos_disp_refugios(self): 
        cant_de_refugios=0
        actual=self.arreglo_listas[1].head
        while actual: 
            if actual.data.tiene_espacio():
                cant_de_refugios+=1
                
            actual=actual.next
        return cant_de_refugios
    
    def recursos_disponibles(self):
        arraydisp=[0]*3
        arraydisp[0]=self.__recursos_disp_asesores()
        arraydisp[1]=self.__recursos_disp_refugios()
        arraydisp[2]=self.__recursos_disp_alimentos()
        return arraydisp
    
    def __asesores_usados(self): 
        cant_de_asesores = 0
        actual=self.arreglo_listas[0].head 
        while actual: 
            if not actual.data.esta_disponible(): 
                cant_de_asesores+=1
            actual=actual.next
        return cant_de_asesores
    
    def __refugios_usados(self): 
        cant_de_refugios=0
        actual=self.arreglo_listas[1].head
        while actual: 
            if not actual.data.tiene_espacio():
                cant_de_refugios+=1
            actual=actual.next
        return cant_de_refugios
    
    def recursos_usados(self): 
        arrayusados=[0]*3

        arrayusados[0]= self.__asesores_usados()
        arrayusados[1]= self.alims_asignados
        arrayusados[2]= self.__refugios_usados()

        return arrayusados
    
    def imprimir_historial(self):
        self.lista_recursos_asignados.print()