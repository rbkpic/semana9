from app_consola import cola_pendientes, pila_historial

def buscar_solicitud(id_solicitud):
    for solicitud in cola_pendientes:
        if solicitud["id"]==id_solicitud:
            return solicitud, "Pendientes"

    for solicitud in pila_historial:
            if solicitud["id"]==id_solicitud:
                return solicitud, "Historial"

    return None, None

if __name__=="__main__":
    id_buscar=1

    resultado, ubicacion = buscar_solicitud(id_buscar)

    if resultado:
        print("ID encontrado")

    else:
        print("NO ENCONTRADO0")