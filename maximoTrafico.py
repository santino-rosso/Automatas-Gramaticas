# Encuentra el usuario con más tráfico
def encontrar_usuario_max_trafico(trafico_por_usuario):
    lista_valores = trafico_por_usuario.values()
    trafico_maximo = max(lista_valores)
    usuario_max_trafico = None
    for usuario, trafico in trafico_por_usuario.items():
        if trafico == trafico_maximo:
            usuario_max_trafico = usuario
    return usuario_max_trafico, trafico_maximo