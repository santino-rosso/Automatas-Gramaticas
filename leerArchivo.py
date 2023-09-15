from expresionesRegulares import *

# Lee el archivo de entrada y filtra las líneas válidas
def leer_archivo(nombre_archivo):
    lineas_validas = []
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        for linea in lineas[1:]:  # Ignorar la primera línea de encabezado
            campos = linea.strip().split(",")
            campos.pop()
            campos.pop()
            if (
                len(campos) == 16 and
                Validar_ID(campos[0]) and
                Validar_ID_Sesion(campos[1]) and
                Validar_ID_Conexion_Unico(campos[2]) and
                Validar_Usuario(campos[3]) and 
                Validar_Inicio_Conexion_Dia(campos[6]) and 
                Validar_Inicio_Conexion_Hora(campos[7]) and
                Validar_Fin_Conexion_Dia(campos[8]) and 
                Validar_Fin_Conexion_Hora(campos[9]) and
                Validar_Session_Time(campos[10]) and
                Validar_Input_Octects(campos[11]) and
                Validar_Output_Octects(campos[12]) and
                Validar_MAC_AP(campos[13]) and
                Validar_MAC_Cliente(campos[14])
            ):
                lineas_validas.append(campos)
    return lineas_validas