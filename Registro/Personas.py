from dataclasses import dataclass

@dataclass
class Persona: 
    __nombre: str
    __id: str
    __nacionalidad: str
    __edad: int
    __motivo: str
    __priority: int
    
    #Urgente sera 1 y regular sera 2 
    
    def __init__(self, nombre, id, nacionalidad, edad, motivo, priority):
        self.__nombre = nombre
        self.__id = id
        self.__nacionalidad = nacionalidad
        self.__edad = edad
        self.__motivo = motivo
        self.__priority = priority

    def __str__(self):
        return f'{self.nombre}'
    #Eq compara igual, lt menor que, le menor o igual, gt mayor que, ge mayor o igual, ne diferente 
    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __le__(self, other):
        return self.__priority <= other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority

    def __ge__(self, other):
        return self.__priority >= other.__priority

    def __ne__(self, other):
        return self.id != other.__id