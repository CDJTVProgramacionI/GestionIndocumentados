from Estructuras.listaCircularDinamica import CircularLinkedList
from dataclasses import dataclass

@dataclass
class SeguimientoAsesoria:
    __lista_seguimiento_de_asesoria: CircularLinkedList
    
    def __init__(self):
        self.__lista_seguimiento_de_asesoria = CircularLinkedList()
    
    def registrar(self, persona):
        self.__lista_seguimiento_de_asesoria.insertAtEnd(persona)
        
    def darSeguimiento(self, id : str):
        indice = self.__lista_seguimiento_de_asesoria.search(id)
        print(f"Dando seguimiento a la persona con id {id}")
        caso_cerrado = input("¿Se cerró el caso?").lower()
        
        if caso_cerrado == "si":
            self.__lista_seguimiento_de_asesoria.deleteAt(indice)
            print("Caso cerrado")
        else:
            print("Se dará seguimiento al caso")
        
        
@dataclass
class SeguimientoRefugios:
    __lista_seguimiento_de_refugios: CircularLinkedList
    
    def __init__(self):
        self.__lista_seguimiento_de_refugios = CircularLinkedList()
        
    def registrar(self, persona):
        self.__lista_seguimiento_de_refugios.insertAtEnd(persona)
        
    def darSeguimiento(self, id : str):
        indice = self.__lista_seguimiento_de_refugios.search(id)
        print(f"Dando seguimiento a la persona con id {id}")
        caso_cerrado = input("Hola deportado, ¿aún necesitas el refugio?").lower()
        
        if caso_cerrado == "si":
            print("Se dará seguimiento más adelante")
        else:
            self.__lista_seguimiento_de_refugios.deleteAt(indice)
            print("Refugio liberado")