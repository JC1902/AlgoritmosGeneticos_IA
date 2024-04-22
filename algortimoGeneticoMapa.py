import random
import numpy as np

# Matriz inicial
initial_matrix = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 2, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 3, 0, 0, 2, 0, 1],
    [1, 0, 3, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 2, 2, 0, 2, 0, 1],
    [1, 0, 3, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 0, 2, 0, 3, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

# Matriz objetivo
target_matrix = np.array([
    [3, 5, 1, 1, 1, 6, 6, 1, 1, 5],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
    [1, 4, 3, 1, 1, 1, 5, 5, 3, 1],
    [1, 4, 5, 1, 6, 6, 3, 5, 4, 1],
    [1, 4, 5, 6, 9, 10, 6, 5, 4, 1],
    [1, 3, 5, 6, 8, 7, 6, 5, 3, 1],
    [1, 4, 5, 6, 3, 5, 1, 5, 4, 1],
    [1, 3, 5, 6, 5, 3, 1, 5, 4, 1],
    [5, 4, 6, 6, 5, 1, 1, 1, 4, 1],
    [4, 4, 1, 1, 1, 1, 1, 1, 4, 4]
])

# Parámetros del algoritmo genético
mutation_rate = 0.05
population_size = 200
max_generations_without_improvement = 200

def fitness(individual):
    return np.sum(individual == target_matrix)

def roulette_selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, ind in enumerate(population):
        current += fitness_values[i]
        if current > pick:
            return ind

def create_individual():
    return initial_matrix.copy()

def mutate(individual):
    mutated_individual = individual.copy()
    for i in range(mutated_individual.shape[0]):
        for j in range(mutated_individual.shape[1]):
            if random.random() < mutation_rate:
                mutated_individual[i][j] = random.randint(1, 10)
    return mutated_individual

# Algoritmo genético
current_matrix = create_individual()

best_fitness = 0
generations_without_improvement = 0

while True:
    current_fitness = fitness(current_matrix)
    if current_fitness == np.prod(current_matrix.shape):
        print("Solución encontrada.")
        break

    if current_fitness > best_fitness:
        best_fitness = current_fitness
        best_solution = current_matrix.copy()
        generations_without_improvement = 0
    else:
        generations_without_improvement += 1

    if generations_without_improvement >= max_generations_without_improvement:
        print("Se alcanzó el límite de generaciones sin mejora.")
        break

    next_population = [best_solution.copy()]  
    while len(next_population) < population_size:
        selected_individual = roulette_selection([current_matrix], [current_fitness])
        new_individual = mutate(selected_individual)
        # Reemplazar los ceros con valores aleatorios
        new_individual[new_individual == 0] = random.randint(1, 10)
        next_population.append(new_individual)

    current_matrix = roulette_selection(next_population, [fitness(ind) for ind in next_population])  # Utilizamos la selección de ruleta para todos los padres

best_solution = current_matrix
print("Mejor solución encontrada:")
print(best_solution)
