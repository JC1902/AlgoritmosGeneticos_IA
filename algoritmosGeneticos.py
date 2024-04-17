import random

class Agente:
    def __init__(self, fuerza, vida, ataque, defensa, resistencia, agilidad):
        self.fuerza = fuerza
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.resistencia = resistencia
        self.agilidad = agilidad
        self.fitness = 0  # Inicializar el fitness en 0
#-----------------------------------------------------------------------------------
    def atacar(self):
        # Convertir la agilidad a un entero
        agilidad_entero = int(self.agilidad)
        # Calcular el daño total de un ataque
        ataques_realizados = random.randint(1, agilidad_entero)
        daño_total = self.ataque * self.fuerza * ataques_realizados
        return daño_total
#-----------------------------------------------------------------------------------
    def recibir_ataque(self, ataque_enemigo):
        # Calcular el daño recibido
        porcentaje_defensa = random.randint(1, 100)
        daño_recibido = ataque_enemigo * (100 - self.defensa) / 100
        self.vida -= daño_recibido
#-----------------------------------------------------------------------------------
    def crossover(self, partner):
        # Realizar el crossover para generar un nuevo agente hijo
        child_genes = {
            'fuerza': (self.fuerza + partner.fuerza) / 2,
            'vida': (self.vida + partner.vida) / 2,
            'ataque': (self.ataque + partner.ataque) / 2,
            'defensa': (self.defensa + partner.defensa) / 2,
            'resistencia': (self.resistencia + partner.resistencia) / 2,
            'agilidad': (self.agilidad + partner.agilidad) / 2
        }
        return Agente(**child_genes)  # Crear un nuevo agente con los genes del hijo
#-----------------------------------------------------------------------------------
class AlgoritmoGenetico:
    def __init__(self, poblacion_size):
        self.poblacion = []
        self.poblacion_size = poblacion_size
#-----------------------------------------------------------------------------------
    def generar_poblacion_inicial(self):
        for _ in range(self.poblacion_size):
            # Generar características aleatorias para los agentes
            fuerza = random.randint(1, 10)
            vida = 100
            ataque = random.randint(1, 10)
            defensa = random.randint(1, 100)
            resistencia = random.randint(1, 100)
            agilidad = random.randint(1, 10)
            agente = Agente(fuerza, vida, ataque, defensa, resistencia, agilidad)
            self.poblacion.append(agente)
#-----------------------------------------------------------------------------------
    def simular_combate(self, agente1, agente2):
        while agente1.vida > 0 and agente2.vida > 0:
            # Turno del agente 1
            daño_agente1 = agente1.atacar()
            agente2.recibir_ataque(daño_agente1)
            
            # Turno del agente 2
            daño_agente2 = agente2.atacar()
            agente1.recibir_ataque(daño_agente2)

        if agente1.vida <= 0:
            return agente2
        else:
            return agente1
#-----------------------------------------------------------------------------------
    def calcular_fitness(self):
        # Simular combate entre cada par de agentes en la población
        for i in range(len(self.poblacion)):
            for j in range(i + 1, len(self.poblacion)):
                resultado = self.simular_combate(self.poblacion[i], self.poblacion[j])

                # Calcular el fitness basado en el resultado del combate
                if resultado == self.poblacion[i]:
                    self.poblacion[i].fitness += 1
                else:
                    self.poblacion[j].fitness += 1
#-----------------------------------------------------------------------------------
    def seleccionar_padres(self):
        # Seleccionar dos padres aleatorios basados en el fitness
        padres = random.choices(self.poblacion, weights=[agente.fitness for agente in self.poblacion], k=2)
        return padres
#-----------------------------------------------------------------------------------
    def algoritmo_genetico(self, max_generaciones):
        self.generar_poblacion_inicial()
        num_generaciones = 0

        while num_generaciones < max_generaciones:
            # Calcular el fitness de la población actual
            self.calcular_fitness()

            # Seleccionar dos padres y realizar crossover para crear nuevos hijos
            for _ in range(self.poblacion_size // 2):
                padre1, padre2 = self.seleccionar_padres()
                hijo1 = padre1.crossover(padre2)
                hijo2 = padre2.crossover(padre1)
                self.poblacion.extend([hijo1, hijo2])

            # Incrementar el número de generaciones
            num_generaciones += 1

        return num_generaciones
#-----------------------------------------------------------------------------------
# Uso del algoritmo genético para simular combates entre dos agentes
algoritmo = AlgoritmoGenetico(poblacion_size=10)
num_generaciones = algoritmo.algoritmo_genetico(10)
print("Número total de generaciones:", num_generaciones)

# Seleccionar dos agentes para el combate
agente1 = algoritmo.poblacion[0]
agente2 = algoritmo.poblacion[1]

# Simular combate entre los dos agentes
ganador = algoritmo.simular_combate(agente1, agente2)
print("El ganador es el agente con {} de vida restante.".format(ganador.vida))
