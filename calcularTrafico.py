from datetime import datetime

def calcular_trafico(lineas, fecha_inicio, fecha_fin):
    trafico_por_usuario = {}
    # Define las columnas correspondientes a cada campo
    columna_usuario = 3
    columna_fecha_inicio = 6
    columna_fecha_hora_inicio = 7
    columna_fecha_fin = 8
    columna_fecha_hora_fin = 9
    columna_input_octets = 11
    columna_output_octets = 12
    
    for linea in lineas:
        # Obtén los valores de las columnas para esta línea
        fecha_inicio_str = linea[columna_fecha_inicio]
        fecha_hora_inicio_str = linea[columna_fecha_hora_inicio]
        fecha_fin_str = linea[columna_fecha_fin]
        fecha_hora_fin_str = linea[columna_fecha_hora_fin]
        usuario = linea[columna_usuario]
        input_octets = int(linea[columna_input_octets])
        output_octets = int(linea[columna_output_octets])
        
        # Convierte las fechas y horas en objetos datetime
        fecha_inicio_conexion = datetime.strptime(fecha_inicio_str + ' ' + fecha_hora_inicio_str, '%Y-%m-%d %H:%M:%S')
        fecha_fin_conexion = datetime.strptime(fecha_fin_str + ' ' + fecha_hora_fin_str, '%Y-%m-%d %H:%M:%S')
        
        # Verifica si la conexión está en el rango de fechas especificado
        if fecha_inicio <= fecha_inicio_conexion <= fecha_fin or fecha_inicio <= fecha_fin_conexion <= fecha_fin:
            trafico_total = input_octets + output_octets
            
            # Agrega el tráfico al usuario correspondiente en el diccionario
            if usuario in trafico_por_usuario:
                trafico_por_usuario[usuario] += trafico_total
            else:
                trafico_por_usuario[usuario] = trafico_total
                
    return trafico_por_usuario