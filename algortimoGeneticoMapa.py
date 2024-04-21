import numpy as np 
import math
import random
from main import mapaJuego
#-------------------------------------------------------------------------


NUM_CROMOSOMAS = 10
GENES_POR_CROMOSOMA = 10
TOTAL_GENES = NUM_CROMOSOMAS * GENES_POR_CROMOSOMA
RATIO_MUTACION = 0.1

def f_deX(cromosoma):
    return sum((i + 1) * valor for i, valor in enumerate(cromosoma)) + 50

def fitness(fx):
    return 1 / (1 + fx)

def generar_cromosomas_iniciales():
    return mapaJuego

def calcular_fitnesses(cromosomas):
    fxs = [f_deX(cromosoma) for cromosoma in cromosomas]
    total_fitness = sum(fitness(fx) for fx in fxs)
    return [fitness(fx) / total_fitness for fx in fxs]

def seleccionar_nuevas_posiciones(probabilidades):
    acumulaciones = [sum(probabilidades[:i+1]) for i in range(NUM_CROMOSOMAS)]
    return [next(i+1 for i, acum in enumerate(acumulaciones) if rand < acum) for rand in [random.random() for _ in range(NUM_CROMOSOMAS)]]

def cruzar_cromosomas(cromosomas, nuevas_posiciones, puntos_de_corte):
    nuevos_cromosomas = cromosomas[:]
    for i, pos in enumerate(nuevas_posiciones):
        if pos != i + 1 and puntos_de_corte[i] != 0:
            punto_corte = puntos_de_corte[i]
            cromosoma_1 = nuevos_cromosomas[i]
            cromosoma_2 = nuevos_cromosomas[pos - 1]
            nuevos_cromosomas[i] = cromosoma_1[:punto_corte] + cromosoma_2[punto_corte:]
    return nuevos_cromosomas

def mutar_cromosomas(cromosomas, pos_mutaciones, genes_mutados):
    for i, pos in enumerate(pos_mutaciones):
        fila = (pos - 1) // GENES_POR_CROMOSOMA
        columna = (pos - 1) % GENES_POR_CROMOSOMA
        cromosomas[fila][columna] = genes_mutados[i]
    return cromosomas

def reasignar_cromosomas(cromosomas):
    for i, cromosoma in enumerate(cromosomas):
        globals()[f"cromosoma_{i+1}"] = cromosoma

def seleccionar_mejores_cromosomas(cromosomas):
    mejores_cromosomas = []

    for cromosoma in cromosomas:
        valor = abs(f_deX(cromosoma))
        if len(mejores_cromosomas) < 10:
            # Si aún no tenemos 10 cromosomas en la lista, simplemente agregamos este
            mejores_cromosomas.append((cromosoma, valor))
            # Ordenamos la lista de mejores cromosomas basados en el valor absoluto
            mejores_cromosomas.sort(key=lambda x: x[1])
        else:
            # Si ya tenemos 10 cromosomas en la lista, comprobamos si este cromosoma es mejor que alguno de los existentes
            peor_valor = max(mejores_cromosomas, key=lambda x: x[1])[1]
            if valor < peor_valor:
                # Si el nuevo cromosoma es mejor que el peor de los 10, lo reemplazamos
                peor_index = mejores_cromosomas.index((max(mejores_cromosomas, key=lambda x: x[1])))
                mejores_cromosomas[peor_index] = (cromosoma, valor)
                # Ordenamos la lista de mejores cromosomas basados en el valor absoluto
                mejores_cromosomas.sort(key=lambda x: x[1])

    return [cromosoma for cromosoma, _ in mejores_cromosomas]

print("Mejor cromosoma:", seleccionar_mejores_cromosomas( generar_cromosomas_iniciales() ) )

mapaJuego = seleccionar_mejores_cromosomas( generar_cromosomas_iniciales() )

def algoritmo_genetico():
    cromosomas = generar_cromosomas_iniciales()
    fitnesses = calcular_fitnesses(cromosomas)
    seleccionados = seleccionar_nuevas_posiciones(fitnesses)
    puntos_de_corte = [random.randint(0, GENES_POR_CROMOSOMA) for _ in range(NUM_CROMOSOMAS)]
    cromosomas = cruzar_cromosomas(cromosomas, seleccionados, puntos_de_corte)
    pos_mutaciones = [random.randint(1, TOTAL_GENES) for _ in range(int(TOTAL_GENES * RATIO_MUTACION))]
    genes_mutados = [random.randint(0, 3) for _ in range(int(TOTAL_GENES * RATIO_MUTACION))]
    cromosomas = mutar_cromosomas(cromosomas, pos_mutaciones, genes_mutados)
    reasignar_cromosomas(cromosomas)
    mejores_cromosomas = seleccionar_mejores_cromosomas(cromosomas)
    return mejores_cromosomas

# Ejemplo de uso del algoritmo genético
mapaJuego = mejores_cromosomas = algoritmo_genetico()
for cromosoma in mejores_cromosomas:
    print(f_deX(cromosoma))

#-------------------------------------------------------------------------