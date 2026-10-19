from app_consola import cola_pendientes 

def consultar_siguiente():
    if len(cola_pendientes)==0:
        return None

    else:
        return cola_pendientes[0]

print("--- PRUEBA 1: Primera consulta ---")
print("Siguiente:", consultar_siguiente())
print("Cantidad de elementos en cola:", len(cola_pendientes))

print("\n--- PRUEBA 2: Segunda consulta (debe ser el mismo ID y la misma longitud) ---")
print("Siguiente:", consultar_siguiente())
print("Cantidad de elementos en cola:", len(cola_pendientes))