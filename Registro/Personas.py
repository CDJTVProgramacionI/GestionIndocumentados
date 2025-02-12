from dataclasses import dataclass

@dataclass
class Persona: 
    __nombre: str
    __id: str
    __nacionalidad: str
    __edad: int
    __motivo: str
    __priority: int
    __nec_asesor: bool
    __nec_alimento : bool
    __nec_refugio : bool
    __asesor : str
    __refugio : str
    
    @property
    def id(self):
        return self.__id
    
    @property
    def priority(self):
        return self.__priority
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def asesor(self):
        return self.__asesor
    
    @property
    def refugio(self):
        return self.__refugio
    
    
    #Urgente sera 1 y regular sera 2 
    
    def __init__(self, nombre, id, nacionalidad, edad, motivo, priority, asesoria, alimento, refugio):
        self.__nombre = nombre
        self.__id = id
        self.__nacionalidad = nacionalidad
        self.__edad = edad
        self.__motivo = motivo
        self.__priority = priority
        self.__nec_asesor = asesoria
        self.__nec_alimento = alimento
        self.__nec_refugio = refugio
        self.__asesor = None
        self.__refugio = ""
        
    def necesita_asesoria(self):
        return self.__nec_asesor
    
    def necesita_alimento(self):
        return self.__nec_alimento
    
    def necesita_refugio(self):
        return self.__nec_refugio
    
    def asignar_asesor(self, nombre_asesor : str):
        self.__asesor = nombre_asesor
        
    def asignar_refugio(self, nombre_refugio):
        self.__refugio = nombre_refugio
    
    def get_id(self):
        return self.__id

    def __str__(self):
        return f'{self.nombre}'
    #Eq compara igual, lt menor que, le menor o igual, gt mayor que, ge mayor o igual, ne diferente 
    def __eq__(self, other):
        return self.__id == other.__id

    def __lt__(self, other):
        return self.__priority < other.__priority

    def __le__(self, other):
        return self.__priority <= other.__priority

    def __gt__(self, other):
        return self.__priority > other.__priority

    def __ge__(self, other):
        return self.__priority >= other.__priority

    def __ne__(self, other):
        return self.id != other.id