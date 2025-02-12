from Registro.Estructuras.listaCircularDinamica import CircularLinkedList
from Registro.Personas import Persona
from Registro.Recurso import Recursos
from dataclasses import dataclass

@dataclass
class SeguimientoAsesoria:
    __lista_seguimiento_de_asesoria: CircularLinkedList
    __casos_resueltos: int
    
    def __init__(self):
        self.__lista_seguimiento_de_asesoria = CircularLinkedList()
        self.__casos_resueltos = 0
    
    def registrar(self, persona):
        self.__lista_seguimiento_de_asesoria.insertAtEnd(persona)
        
    def darSeguimiento(self, id : str, recursos : Recursos):
        persona = Persona("", id, "", 0, "", 0, False, False, False)
        indice = self.__lista_seguimiento_de_asesoria.search(persona)
        
        if indice == -1:
            print("No se encontró a la persona")
            return
        
        print(f"Dando seguimiento a la persona con id {id}")
        caso_cerrado = input("¿Se cerró el caso?").lower()
        
        if caso_cerrado == "si":
            self.__lista_seguimiento_de_asesoria.deleteAt(indice)
            self.__casos_resueltos += 1
            recursos.liberarAsesor(persona)
            print("Caso cerrado")
        else:
            print("Se dará seguimiento al caso")
            
    def get_casos_resueltos(self) -> int:
        return self.__casos_resueltos
    
    def get_casos_pendientes(self) -> int:
        return self.__lista_seguimiento_de_asesoria.size()
        
        
@dataclass
class SeguimientoRefugios:
    __lista_seguimiento_de_refugios: CircularLinkedList
    
    def __init__(self):
        self.__lista_seguimiento_de_refugios = CircularLinkedList()
        
    def registrar(self, persona):
        self.__lista_seguimiento_de_refugios.insertAtEnd(persona)
        
    def darSeguimiento(self, id : str, recursos : Recursos):
        persona = Persona("", id, "", 0, "", 0, False, False, False)
        indice = self.__lista_seguimiento_de_refugios.search(persona)
        
        if indice == -1:
            print("No se encontró a la persona")
            return
        
        print(f"Dando seguimiento a la persona con id {id}")
        caso_cerrado = input("Aún se necesita el refugio?").lower()
        
        if caso_cerrado == "si":
            print("Se dará seguimiento más adelante")
        else:
            self.__lista_seguimiento_de_refugios.deleteAt(indice)
            recursos.liberarRefugio(persona)
            print("Refugio liberado")