import random
import math

NUM_CROMOSOMAS = 6
GENES_POR_CROMOSOMA = 4
TOTAL_GENES = NUM_CROMOSOMAS * GENES_POR_CROMOSOMA
RATIO_MUTACION = 0.1

def f_deX(cromosoma):
    return sum((i + 1) * valor for i, valor in enumerate(cromosoma)) - 30

def evaluar(cromosoma):
    return sum((i + 1) * valor for i, valor in enumerate(cromosoma))

def fitness(fx):
    return 1 / (1 + fx)

def generar_cromosomas_iniciales():
    return [
        [12, 5, 23, 8],
        [2, 21, 18, 3],
        [10, 4, 13, 14],
        [20, 1, 10, 6],
        [1, 4, 13, 19],
        [20, 5, 17, 1]
    ]

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

def seleccionar_mejor_cromosoma(cromosomas):
    mejor_cromosoma = None
    mejor_valor = float('inf')  # Inicializar con infinito para encontrar el más cercano a 0

    for cromosoma in cromosomas:
        valor = abs(evaluar(cromosoma))
        if valor < mejor_valor:
            mejor_valor = valor
            mejor_cromosoma = cromosoma

    return mejor_cromosoma

def main():
    generacion = 1
    cromosomas = generar_cromosomas_iniciales()
    
    while True:
        print(f"Generación: {generacion}")
        print("Cromosomas:", cromosomas)
        print("\n")

        fitnesses = calcular_fitnesses(cromosomas)
        print("Fitness:", fitnesses)
        print("\n")

        nuevas_posiciones = seleccionar_nuevas_posiciones(fitnesses)
        print("Nuevas posiciones:", nuevas_posiciones)
        print("\n")

        puntos_de_corte = [random.randint(0, GENES_POR_CROMOSOMA - 1) if random.random() < 0.25 else 0 for _ in range(NUM_CROMOSOMAS)]
        print("Puntos de corte:", puntos_de_corte)
        print("\n")

        cromosomas = cruzar_cromosomas(cromosomas, nuevas_posiciones, puntos_de_corte)
        print("Cromosomas después de cruce:", cromosomas)
        print("\n")

        pos_mutaciones = [random.randint(1, TOTAL_GENES) for _ in range(math.floor(RATIO_MUTACION * TOTAL_GENES))]
        print(pos_mutaciones)
        genes_mutados = [random.randint(1, 30) for _ in range(len(pos_mutaciones))]
        cromosomas = mutar_cromosomas(cromosomas, pos_mutaciones, genes_mutados)
        print("Cromosomas después de mutación:", cromosomas)
        print("\n")

        reasignar_cromosomas(cromosomas)
        print("\n")

        generacion += 1
        
        mejor_cromosoma = seleccionar_mejor_cromosoma(cromosomas)
        valor_objetivo = evaluar(mejor_cromosoma)
        if valor_objetivo == 30:
            print("¡Se encontró un cromosoma con un valor de función objetivo de 30!")
            print("Mejor cromosoma:", mejor_cromosoma)
            print("Valor de la función objetivo:", valor_objetivo)
            break

if __name__ == "__main__":
    main()