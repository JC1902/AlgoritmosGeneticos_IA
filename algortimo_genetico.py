import random
import math

NUM_CROMOSOMAS = 5.0
GENES_POR_CROMOSOMA = 15.0
GENES_TOTALES = NUM_CROMOSOMAS * GENES_POR_CROMOSOMA

def generar_poblacion_inicial():
    return [
        [ 4, 11, 4, 3, 0, 0, 9, 2, 3, 2 ],
        [ 0, 13, 1, 11, 7, 12, 10, 4, 12, 5 ],
        [ 11, 8, 11, 14, 13, 14, 6, 3, 8, 1 ],
        [ 4, 9, 13, 11, 1, 1, 4, 6, 3, 5 ],
        [ 10, 5, 3, 6, 1, 14, 10, 13, 12, 8 ],
        [ 12, 2, 8, 6, 1, 13, 5, 12, 11, 10 ],
        [ 13, 9, 14, 3, 3, 0, 6, 12, 2, 5 ],
        [ 1, 3, 3, 4, 6, 10, 0, 2, 1, 0 ],
        [ 11, 8, 11, 14, 14, 10, 1, 7, 0, 10 ],
        [ 9, 1, 8, 9, 10, 14, 11, 13, 12, 2 ]
    ]