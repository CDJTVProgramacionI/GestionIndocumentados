from lib.pro_reader import ProReader
from Registro.Personas import Persona
from Registro.Registro import Registro
from Registro.Seguimiento import *
from Registro.Recurso import *

def crea_recursos():
        #Crea los asesores legales
        AsesorLegal1 = AsesorLegal("Asesor 1")
        AsesorLegal2 = AsesorLegal("Asesor 2")
        AsesorLegal3 = AsesorLegal("Asesor 3")
        
        # Crear tres refugios con una capacidad de 15 personas cada uno
        refugio1 = Refugio ("Refugio 1", 15)
        refugio2 = Refugio("Refugio 2", 15)
        refugio3 = Refugio("Refugio 3", 15)
        
        #Crea los alimentos
        paquete1 = Alimentos(["Arroz", "Frijoles", "Aceite"])
        paquete2 = Alimentos(["Pasta", "Salsa de tomate", "Queso"]) #pasar al main
        paquete3 = Alimentos(["Pan", "Mermelada", "Leche"])

def pidedatos(lee : ProReader):
    nombre=lee.read_string("Ingrese el nombre e la persona: ")
    id=lee.read_string("Ingrese el id de la persona: ")
    nacionalidad=lee.read_string("Ingrese la nacionalidad de la persona: ")
    edad=lee.read_int("Ingrese la edad de la persona: ")
    motivo=lee.read_string("Ingrese el motivo de repatriacion la persona: ")
    asesoria=lee.read_bool("La persona requiere asesoria? (Si/No): ")
    alimento=lee.read_bool("La persona requiere alimento? (Si/No): ")
    refugio=lee.read_bool("La persona requiere refugio? (Si/No): ")
    prioridad=lee.read_bool("La persona es prioritaria: (Si/No): ")
    
    if prioridad:
        prioridad=1
    else:
        prioridad=2
        
    return Persona(nombre, id, nacionalidad, edad, motivo, prioridad, asesoria, alimento, refugio)
    

def print_menu():
    print("Bienvenido al sistema de gestion de migrantes")
    print("1. Ingrar datos")
    print("2. Segumiento de asesoria")
    print("3. Seguimiento de refugios")
    print("4. Imprimir reporte semanal")
    print("5. Salir")

def main():
    lee = ProReader("lib/pro_reader.dll")
    registros = Registro()
    seg_asesorias = SeguimientoAsesoria()
    seg_refugios = SeguimientoRefugios()
    op = 0
    while op != 5:
        print_menu()
        op = lee.read_int("Ingrese una opcion: ")
        
        match op:
            case 1:
                persona = pidedatos(lee)
                registros.registrar(persona)
            case 2:
                id = lee.read_string("Ingrese el id de la persona:")
                seg_asesorias.darSeguimiento(id)
            case 3:
                id = lee.read_string("Ingrese el id de la persona:")
                seg_refugios.darSeguimiento(id)
            case 4:
                print("You selected Option 4")
            case 5:
                print("Ayos suerte con la deportacion")
            case _:
                print("Opcion invalida")

if __name__ == "__main__":
    main()