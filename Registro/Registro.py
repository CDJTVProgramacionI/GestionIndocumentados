from dataclasses import dataclass
from Estructuras.Piladinamica import pila
from Estructuras.colalineal import ColaLineal
from Personas import Persona

@dataclass
class Registro:
    #ATRIBUTOS
    __urgente: pila
    __regular: ColaLineal
    __totalcase: int
    #CONSTRUCTOR
    def __init__(self): 
        self.__urgente=pila()
        self.__regular=ColaLineal()
        self.__totalcase=0
        
    def registrar(self, persona : Persona):
        if persona.__priority == 1: #Urgente
            self.__urgente.push(persona)
        elif persona.__priority == 2: #Regular
            self.__regular.encolar(persona)  #mandamos a la cola a la persona 
            
        self.__totalcase += 1
    
    def atendsig(self) -> Persona: 
        if self.__urgente.estavacio():
            return self.__regular.desencolar()
        else: 
            return self.__urgente.pop()
        
    
    