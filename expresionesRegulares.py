import re

def Validar_ID(string):
    reg = re.compile(r"^\d{6,7}$")
    return bool(reg.match(string))

def Validar_ID_Sesion(string):
    reg = re.compile(r"^(([0-9]|[A-F]){8}-?([0-9]|[A-F]){8})$")
    return bool(reg.match(string))

def Validar_ID_Conexion_Unico(string):
    reg = re.compile(r"^([0-9]|[a-f]){16}$")
    return bool(reg.match(string))

def Validar_Usuario(string):
    reg = re.compile(r"^.*\D+.*$")
    return bool(reg.match(string))

def Validar_Inicio_Conexion_Dia(string):
    reg = re.compile(r"^(2019|202[0-3])-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$")
    return bool(reg.match(string))

def Validar_Inicio_Conexion_Hora(string):
    reg = re.compile(r"^([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])$")
    return bool(reg.match(string))

def Validar_Fin_Conexion_Dia(string):
    reg = re.compile(r"^(2019|202[0-3])-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$")
    return bool(reg.match(string))

def Validar_Fin_Conexion_Hora(string):
    reg = re.compile(r"^([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])$")
    return bool(reg.match(string))

def Validar_Session_Time(string):
    reg = re.compile(r"^\d+$")
    return bool(reg.match(string))

def Validar_Input_Octects(string):
    reg = re.compile(r"^\d+$")
    return bool(reg.match(string))

def Validar_Output_Octects(string):
    reg = re.compile(r"^\d+$")
    return bool(reg.match(string))

def Validar_MAC_AP(string):
    reg = re.compile(r"^(([A-F]|[0-9]){2}-){5}([A-F]|[0-9]){2}:[A-Z]{4}$")
    return bool(reg.match(string))

def Validar_MAC_Cliente(string):
    reg = re.compile(r"^(([A-F]|[0-9]){2}-){5}([A-F]|[0-9]){2}$")
    return bool(reg.match(string))