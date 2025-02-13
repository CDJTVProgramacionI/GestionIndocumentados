from lib.pro_reader import ProReader
from Registro.Personas import Persona
from Registro.Registro import Registro
from Registro.Seguimiento import *
from Registro.Recurso import *
from Registro.Reporte import Reporte

def crea_reporte(registro : Registro, recursos : Recursos, seguimiento_asesorias : SeguimientoAsesoria):
    personas_atendidos = registro.get_casostotales()
    recursos_utilizados = recursos.recursos_usados()
    recursos_disponibles = recursos.recursos_disponibles()
    casos_resueltos = seguimiento_asesorias.get_casos_resueltos()
    casos_pendientes = seguimiento_asesorias.get_casos_pendientes()
    reporte = Reporte(personas_atendidos, recursos_utilizados, recursos_disponibles, casos_resueltos, casos_pendientes)
    reporte.generar_reporte("reporte.txt")

def crea_recursos(recursos : Recursos):
        #Crea los asesores legales
        AsesorLegal1 = AsesorLegal("Asesor 1")
        AsesorLegal2 = AsesorLegal("Asesor 2")
        AsesorLegal3 = AsesorLegal("Asesor 3")
        
        recursos.insertarRecurso(0, AsesorLegal1)
        recursos.insertarRecurso(0, AsesorLegal2)
        recursos.insertarRecurso(0, AsesorLegal3)
        
        # Crear tres refugios con una capacidad de 15 personas cada uno
        refugio1 = Refugio ("Refugio 1", 15)
        refugio2 = Refugio("Refugio 2", 15)
        refugio3 = Refugio("Refugio 3", 15)
        
        recursos.insertarRecurso(1, refugio1)
        recursos.insertarRecurso(1, refugio2)
        recursos.insertarRecurso(1, refugio3)
        
        #Crea los alimentos
        paquete1 = Alimentos(["Arroz", "Frijoles", "Aceite"])
        paquete2 = Alimentos(["Pasta", "Salsa de tomate", "Queso"]) #pasar al main
        paquete3 = Alimentos(["Pan", "Mermelada", "Leche"])
        
        recursos.insertarRecurso(2, paquete1)
        recursos.insertarRecurso(2, paquete2)
        recursos.insertarRecurso(2, paquete3)

def pidedatos(lee : ProReader):
    nombre=lee.read_string("Ingrese el nombre de la persona: ")
    id=lee.read_string("Ingrese el id de la persona: ")
    nacionalidad=lee.read_string("Ingrese la nacionalidad de la persona: ")
    edad=lee.read_int("Ingrese la edad de la persona: ")
    motivo=lee.read_string("Ingrese el motivo de repatriacion la persona: ")
    asesoria=lee.read_bool("La persona requiere asesoria? (true/false): ")
    alimento=lee.read_bool("La persona requiere alimento? (true/false): ")
    refugio=lee.read_bool("La persona requiere refugio? (true/false): ")
    prioridad=lee.read_bool("La persona es prioritaria: (true/false): ")
    
    if prioridad:
        prioridad=1
    else:
        prioridad=2
        
    return Persona(nombre, id, nacionalidad, edad, motivo, prioridad, asesoria, alimento, refugio)
    

def print_menu():
    print("Bienvenido al sistema de gestion de migrantes")
    print("1. Ingresar datos")
    print("2. Atender siguiente")
    print("3. Segumiento de asesoria")
    print("4. Seguimiento de refugios")
    print("5. Imprimir reporte semanal")
    print("6. Imprimir historial de recursos")
    print("7. Salir")

def main():
    lee = ProReader("lib/pro_reader.dll")
    registros = Registro()
    recursos = Recursos()
    seg_asesorias = SeguimientoAsesoria()
    seg_refugios = SeguimientoRefugios()
    
    crea_recursos(recursos)
    op = 0
    while op != 7:
        print_menu()
        op = lee.read_int("Ingrese una opcion: ")
        
        match op:
            case 1:
                #persona = pidedatos(lee)
                persona = Persona("Juan", "123", "Mexicana", 20, "Repatriacion", 1, True, True, True)
                registros.registrar(persona)
            case 2:
                sig_persona = registros.atendsig()
                
                if sig_persona is None:
                    continue
                
                if sig_persona.necesita_asesoria():
                    try:
                        recursos.asignarAsesor(sig_persona)
                        print(sig_persona.asesor)
                        seg_asesorias.registrar(sig_persona)
                    except ValueError as e:
                        print(e)
                    
                if sig_persona.necesita_alimento():
                    recursos.asignarAlimento(sig_persona)
                    
                if sig_persona.necesita_refugio():
                    try:
                        recursos.asignarRefugio(sig_persona)
                        seg_refugios.registrar(sig_persona)
                    except ValueError as e:
                        print(e)             
            case 3:
                id = lee.read_string("Ingrese el id de la persona:")
                seg_asesorias.darSeguimiento(id, recursos)
            case 4:
                id = lee.read_string("Ingrese el id de la persona:")
                seg_refugios.darSeguimiento(id, recursos)
            case 5:
                crea_reporte(registros, recursos, seg_asesorias)
                print("Reporte generado")
            case 6:
                print("Historial de recursos")
                recursos.imprimir_historial()
            case 7:
                print("Saliendo")
            case _:
                print("Opcion invalida")

if __name__ == "__main__":
    main()