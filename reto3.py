"""
Crea cancelar_pendiente(id_solicitud). Solo puede cancelar elementos que sigan en la cola. 
Devuelve el elemento eliminado o None.

Prueba: cancela una solicitud intermedia y comprueba que las demás mantienen su orden relativo. 
Una solicitud atendida no puede cancelarse como pendiente.
"""
from app_consola import cola_pendientes
from collections import deque

def cancelar_pendiente(id_solicitud):
    for i in range(len(cola_pendientes)):
        if cola_pendientes[i]["id"]==id_solicitud:
            solicitud_eliminada=cola_pendientes.pop(i)
            return solicitud_eliminada

        else:
            return None
