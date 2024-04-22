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
                 'vida': 100,
               'ataque': (self.ataque + partner.ataque) / 2,
              'defensa': (self.defensa + partner.defensa) / 2,
          'resistencia': (self.resistencia + partner.resistencia) / 2,
             'agilidad': (self.agilidad + partner.agilidad) / 2,
        }
            return Agente(**child_genes)  # Crear un nuevo agente con los genes del hijo
#-----------------------------------------------------------------------------------
    def mutar(self, probabilidad_mutacion):
            if random.random() < probabilidad_mutacion:
                # Si la probabilidad de mutación se cumple, muta un gen aleatorio
                genes = ['fuerza', 'vida', 'ataque', 'defensa', 'resistencia', 'agilidad']
                gen_a_mutar = random.choice(genes)
                nuevo_valor = random.randint(1, 10)  # Nuevo valor aleatorio para el gen mutado
                print( "Si muto" )
                setattr(self, gen_a_mutar, nuevo_valor)
#-----------------------------------------------------------------------------------
    def status( self, nombre ) :
        print( "{} su vida es de: {}".format( nombre, self.vida ) )
        print( "{} su fuerza es: {}".format( nombre, self.fuerza ) )
        print( "{} su ataque es: {}".format( nombre, self.ataque ) )
        print( "{} su defensa es: {}".format( nombre, self.defensa ) )
        print( "{} su agilidad es: {}".format( nombre, self.agilidad ) )
        print( "{} su resistencia es: {}".format( nombre, self.resistencia ) )
        print( "{} su fitness es: {}".format( nombre, self.fitness ) )
        print( "============================================")
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
    def simular_combate(self, a1, a2):
        #agente1.status( "Agente 1" )
        #agente2.status( "Agente 2" )
        while a1.vida > 0 and a2.vida > 0:
            # Turno del agente 1
            if a2.vida >= 0 :
                daño_agente1 = a1.atacar()
                a2.recibir_ataque(daño_agente1)
                print( "Agente 2 recibio {} de daño".format( daño_agente1 ) )
                print ( "La vida del agente 2 es de: {}".format( a2.vida ))
            else:
                break
            
            # Turno del agente 2
            if a1.vida >= 0:
                daño_agente2 = a2.atacar()
                a1.recibir_ataque(daño_agente2)
                print( "Agente 1 recibio {} de daño".format( daño_agente2 ) )
                print ( "La vida del agente 2 es de: {}".format( a1.vida ))
            else:
                break

        if a1.vida <= 0:
            #print( "Agente 1 a muerto" )
            return a2
        else:
            #print( "Agente 2 a muerto" )
            return a1
#-----------------------------------------------------------------------------------
    def calcular_fitness(self):
        # Simular combate entre cada par de agentes en la población
        for i in range(len(self.poblacion)):
            for j in range(i + 1, len(self.poblacion)):
                resultado = self.simular_combate(self.poblacion[i], self.poblacion[j])

                # Calcular el fitness basado en el resultado del combate
                if resultado == self.poblacion[i] :
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
                print( "Generacion {}".format( num_generaciones ) )
                padre1, padre2 = self.seleccionar_padres()

                hijo1 = padre1.crossover(padre2)
                
                padre1.status( "padre 2")
                hijo1.status("Hijo 1")

                hijo1.mutar(random.random())

                self.poblacion.extend([hijo1])

            # Incrementar el número de generaciones
            num_generaciones += 1
            print ( "La pobalcion actiual es de: {}".format(len(self.poblacion) ))
                    
        return num_generaciones
#-----------------------------------------------------------------------------------
    def masApto( self ):
        self.poblacion = [agente for agente in self.poblacion if agente.vida > 0]

        if len( self.poblacion ) <= 2 :
            self.algoritmoGenetico(10)
        else:
            print("No hay algun individuo más apto")
#-----------------------------------------------------------------------------------
# Uso del algoritmo genético para simular combates entre dos agentes
algoritmo = AlgoritmoGenetico(poblacion_size=10)
num_generaciones = algoritmo.algoritmo_genetico(10)
print("Número total de generaciones:", num_generaciones)

algoritmo.masApto()
print ( "La pobalcion actiual es de: {}".format(len(algoritmo.poblacion) ))
# Seleccionar dos agentes para el combate
agente1 = algoritmo.poblacion[ random.randint( 0, len( algoritmo.poblacion ) - 1 ) ]
agente2 = algoritmo.poblacion[ random.randint( 0, len( algoritmo.poblacion ) - 1 ) ]



# Simular combate entre los dos agentes
ganador = algoritmo.simular_combate(agente1, agente2)
print("El ganador es el agente con {} de vida restante.".format(ganador.vida))

agente1.status( "Agente1" )
agente2.status( "Agente2" )
