from dataclasses import dataclass

@dataclass
class Reporte:
    __atenciones : int
    __recursos_utilizados : list
    __recursos_disponibles : list
    __casos_resueltos : int
    __casos_pendientes : int
    
    def __init__(self, casos_atendidos : int, recursos_utilizados : list, recursos_disponibles : list, casos_resueltos : int, casos_pendientes : int):
        self.__atenciones = casos_atendidos
        self.__recursos_utilizados = recursos_utilizados
        self.__recursos_disponibles = recursos_disponibles
        self.__casos_resueltos = casos_resueltos
        self.__casos_pendientes = casos_pendientes
    
    @staticmethod
    def generar_reporte(self, archivo):
        with open(archivo, 'w') as file:
            file.write(f"Casos atendidos: {self.__atenciones}\n")
            file.write(f"Recursos Utilizados: {self.__recursos_utilizados}\n")
            file.write(f"Recursos Disponibles: {self.__recursos_disponibles}\n")
            file.write(f"Casos Resueltos: {self.__casos_resueltos}\n")
            file.write(f"Casos Pendientes: {self.__casos_pendientes}\n")

