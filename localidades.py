from localidad import Localidad
from coleccion import Coleccion

VESTIBULO = 0
MITAD_PASILLO = 1
COCINA = 2
BIBLIOTECA = 3

_localidades = Coleccion()

datos_localidad = {
    VESTIBULO: Localidad.localidad(
        'VESTÍBULO',
        'Estás en el vestíbulo del castillo.'
    ),
    MITAD_PASILLO: Localidad.localidad(
        'Estás en mitad del pasillo.',
        'MITAD PASILLO'
    ),
    COCINA: Localidad.localidad(
        'Estás en la cocina.',
        'COCINA'
    ),
    BIBLIOTECA: Localidad.localidad(
        'Estás en la biblioteca.',
        'BIBLIOTECA'
    )
}

for clave, loc in datos_localidad.items():
    Coleccion.insertar(_localidades, clave, loc)

"""
Cocina --- Mitad pasillo --- Biblioteca
                |
            Vestíbulo
"""

_conexiones = {
    VESTIBULO: {
        'N': MITAD_PASILLO
    },
    MITAD_PASILLO: {
        'S': VESTIBULO,
        'E': BIBLIOTECA,
        'O': COCINA,
    },
    BIBLIOTECA: {
        'O': MITAD_PASILLO,
    },
    COCINA: {
        'E': MITAD_PASILLO,
    },
}

def salida_hacia(localidad_actual, verbo):
    salidas = _conexiones[localidad_actual]
    return salidas.get(verbo)

def localidad(k):
    """
    Devuelve la localidad cuya clave es k en la colección de localidades.

    Lanza una excepción KeyError si la localidad con clave k no existe.
    """
    return Coleccion.elemento(_localidades, k)
