import random
import math

cromosoma_1 = [ 12, 5, 23, 8 ]
cromosoma_2 = [ 2, 21, 18, 3 ]
cromosoma_3 = [ 10, 4, 13, 14 ]
cromosoma_4 = [ 20, 1, 10, 6 ]
cromosoma_5 = [ 1, 4, 13, 19 ]
cromosoma_6 = [ 20, 5, 17, 1 ]

def f_deX( cromosoma ):
    a, b, c, d = cromosoma [ 0 ], cromosoma[ 1 ], cromosoma[ 2 ], cromosoma[ 3 ]

    fx = ( ( a + ( 2 * b ) + ( 3 * c ) + ( 4 * d ) ) - 30 )

    return fx

def fitness( fx ):
    return 1 / ( 1 + fx )

def reasignar_cromosomas( grupo_cromosomas ):
    nuevo_lugar = 0
    global cromosoma_1, cromosoma_2, cromosoma_3, cromosoma_4, cromosoma_5, cromosoma_6

    for nc in grupo_cromosomas:
        print(nc)
        if nuevo_lugar == 0:
            cromosoma_1 = nc
        if nuevo_lugar == 1:
            cromosoma_2 = nc
        if nuevo_lugar == 2:
            cromosoma_3 = nc
        if nuevo_lugar == 3:
            cromosoma_4 = nc
        if nuevo_lugar == 4:
            cromosoma_5 = nc
        if nuevo_lugar == 5:
            cromosoma_6 = nc
            
        nuevo_lugar += 1
    
    print("Nuevos cromosomas1:", cromosoma_1, "\n")
    print("Nuevos cromosomas2:", cromosoma_2, "\n")
    print("Nuevos cromosomas3:", cromosoma_3, "\n")
    print("Nuevos cromosomas4:", cromosoma_4, "\n")
    print("Nuevos cromosomas5:", cromosoma_5, "\n")
    print("Nuevos cromosomas6:", cromosoma_6, "\n")

def main():
    generacion = 1
    global cromosoma_1, cromosoma_2, cromosoma_3, cromosoma_4, cromosoma_5, cromosoma_6
    ratio_mutacion = 0.1
    total_genes = 4*6

    mutaciones_totales = math.floor( ratio_mutacion * total_genes )

    while ( generacion <= 51 ):
        print( f"1.- {cromosoma_1}", f"2.- {cromosoma_2}", f"3.- {cromosoma_3}", f"4.- {cromosoma_4}", f"5.- {cromosoma_5}", f"6.- {cromosoma_6}" )

        totalFitnesses, acum_suma = 0, 0 
        probabilities, acumulaciones, nuevas_pos, nuevos_cromosomas = [], [], [], []
        num_rand1, num_rand2 = [ random.random() for _ in range( 6 ) ], [ random.random() for _ in range( 6 ) ]
        para_crossover = [ 0, 0, 0, 0, 0, 0 ]
        cp = [ 0, 0, 0, 0, 0, 0 ]
        pos_mutaciones, genes_mutados = 0, 0

        fxs = [ f_deX( cromosoma_1 ), f_deX( cromosoma_2 ), f_deX( cromosoma_3 ), f_deX( cromosoma_4 ), f_deX( cromosoma_5 ), f_deX( cromosoma_6 ) ]

        print( f"Generacion: {generacion}" )
        print( "F(x) = [ ", end=" " )
        print( " ".join( f"{ valor }" for valor in fxs ), end=" " )
        print( " ]\n" )

        fitnesses = [ fitness( fx ) for fx in fxs ]

        print( "Fitness = [ ", end=" " )
        print( " ".join( f"{valor:.9f} " for valor in fitnesses ), end=" " )
        print( " ]\n" )

        for aptitud in fitnesses:
            totalFitnesses += aptitud

        print( f"Total de fitness de la generación { generacion }: ", totalFitnesses, "\n" )

        for fitness_i in fitnesses:
            probabilities.append( fitness_i / totalFitnesses )

        print( "Probabilidades = [ ", end=" " )
        print( " ".join( f"{valor:.9f} " for valor in probabilities ), end=" " )
        print( " ]\n" )

        for probabilidad in probabilities:
            acum_suma += probabilidad
            acumulaciones.append( acum_suma )

        print( "Probabilidad acumulada = [ ", end=" " )
        print( " ".join( f"{valor:.9f} " for valor in acumulaciones ), end=" " )
        print( " ]\n" )

        print( "Numeros random = [ ", end=" " )
        print( " ".join( f"{valor:.3f} " for valor in num_rand1 ), end=" " )
        print( " ]\n" )

        i = 0

        while i <= 5:
            if num_rand1[i] < acumulaciones[0]: 
                nuevas_pos.append(1)
            
            if num_rand1[i] >= acumulaciones[0] and num_rand1[i] <= acumulaciones[1]:
                nuevas_pos.append(2)

            if num_rand1[i] >= acumulaciones[1] and num_rand1[i] <= acumulaciones[2]:
                nuevas_pos.append(3)
            
            if num_rand1[i] >= acumulaciones[2] and num_rand1[i] <= acumulaciones[3]:
                nuevas_pos.append(4)

            if num_rand1[i] >= acumulaciones[3] and num_rand1[i] <= acumulaciones[4]:
                nuevas_pos.append(5)

            if num_rand1[i] >= acumulaciones[4] and num_rand1[i] <= acumulaciones[5]:
                nuevas_pos.append(6)
            
            i += 1

        print( "Nuevas posiciones = [ ", end=" " )
        print( " ".join( f"{valor}" for valor in nuevas_pos ), end=" " )
        print( " ]\n" )

        for lugar in nuevas_pos:
            if lugar == 1:
                nuevos_cromosomas.append(cromosoma_1[:])

            if lugar == 2:
                nuevos_cromosomas.append(cromosoma_2[:])

            if lugar == 3:
                nuevos_cromosomas.append(cromosoma_3[:])

            if lugar == 4:
                nuevos_cromosomas.append(cromosoma_4[:])

            if lugar == 5:
                nuevos_cromosomas.append(cromosoma_5[:])

            if lugar == 6:
                nuevos_cromosomas.append(cromosoma_6[:])

        print("Nuevos cromosomas:", nuevos_cromosomas, "\n")

        reasignar_cromosomas( nuevos_cromosomas )

        print( "Segundo grupo de numeros random = [ ", end=" " )
        print( " ".join( f"{valor:.3f} " for valor in num_rand2 ), end=" " )
        print( " ]\n" )

        index = 0
        for num in num_rand2:
            if num < 0.25:
                para_crossover[ index ] = index + 1
            
            index += 1

        # Crear una lista temporal para almacenar los valores no cero
        temp = [valor for valor in para_crossover if valor != 0]

        # Reemplazar los valores en la lista original
        for i in range(len(para_crossover)):
            if para_crossover[i] != 0:
                para_crossover[i] = temp.pop()

        print( "Crossover = [ ", end=" " )
        print( " ".join( f"{valor} " for valor in para_crossover ), end=" " )
        print( " ]\n" )

        for i in range(len(cp)):
            if para_crossover[i] != 0:
                cp[i] = random.randint(1, len(cromosoma_1) - 1)

        print( "Puntos de corte = [ ", end=" " )
        print( " ".join( f"{valor} " for valor in cp ), end=" " )
        print( " ]\n" )

        for index, ncp in enumerate( cp ):
            if ncp != 0:
                print(ncp, index)

        # nuevos_cromosomas_temp = nuevos_cromosomas[:]

        # for index, valor in enumerate(para_crossover):
        #     if valor != 0:
        #         cromosoma_1_index = index
        #         cromosoma_2_index = valor - 1  # Restamos 1 para ajustar al índice de Python

        #         # Cromosomas involucrados en el cruce
        #         cromosoma_1 = nuevos_cromosomas[cromosoma_1_index]
        #         cromosoma_2 = nuevos_cromosomas[cromosoma_2_index]

        #         # Puntos de corte
        #         puntos_de_corte = cp[index]

        #         # Realizar el cruce
        #         hijo_1 = cromosoma_1[:puntos_de_corte] + cromosoma_2[puntos_de_corte:]

        #         nuevos_cromosomas_temp[cromosoma_1_index + 1] = hijo_1

        #         print("Cruce entre cromosoma", cromosoma_1_index + 1, "y cromosoma", cromosoma_2_index + 1)
        #         print("Puntos de corte:", puntos_de_corte)
        #         print("Hijo 1:", hijo_1)
        #         print()

        # nuevos_cromosomas = nuevos_cromosomas_temp

        # Crear una lista temporal para almacenar los nuevos cromosomas generados durante el cruce
        nuevos_cromosomas_temp = nuevos_cromosomas[:]

        for index, valor in enumerate(para_crossover):
            if valor != 0:
                cromosoma_1_index = index
                cromosoma_2_index = valor - 1  # Restamos 1 para ajustar al índice de Python

                # Cromosomas involucrados en el cruce
                cromosoma_1 = nuevos_cromosomas[cromosoma_1_index]
                cromosoma_2 = nuevos_cromosomas[cromosoma_2_index]

                # Puntos de corte
                puntos_de_corte = cp[index]

                # Realizar el cruce
                hijo_1 = cromosoma_1[:puntos_de_corte] + cromosoma_2[puntos_de_corte:]

                # Reemplazar el cromosoma existente con el nuevo cromosoma generado
                nuevos_cromosomas_temp[cromosoma_1_index] = hijo_1

                print("Cruce entre cromosoma", cromosoma_1_index + 1, "y cromosoma", cromosoma_2_index + 1)
                print("Puntos de corte:", puntos_de_corte)
                print("Hijo 1:", hijo_1)
                print()

        # Asignar la lista temporal actualizada a nuevos_cromosomas
        nuevos_cromosomas = nuevos_cromosomas_temp

        print( f"Nuevos cromosomas: {nuevos_cromosomas}" )

        reasignar_cromosomas( nuevos_cromosomas )
        
        pos_mutaciones = [ random.randint( 1, 24 ) for _ in range( mutaciones_totales ) ]

        if pos_mutaciones[ 0 ] == pos_mutaciones[ 1 ]:
            while pos_mutaciones[ 0 ] == pos_mutaciones[ 1 ]:
                pos_mutaciones[ 1 ] = random.randint( 1, 24 )

        genes_mutados = [ random.randint( 1, 30 ) for _ in range( mutaciones_totales ) ]

        print("Posicion de las mutaciones: ", pos_mutaciones )
        print( "Nuevos genes despues de la mutacion: ", genes_mutados )

        # Actualizar los nuevos cromosomas con los genes mutados en las posiciones especificadas
        for i in range(mutaciones_totales):
            fila = (pos_mutaciones[i] - 1) // 4  # Calcula la fila correspondiente
            columna = (pos_mutaciones[i] - 1) % 4  # Calcula la columna correspondiente
            nuevos_cromosomas[fila][columna] = genes_mutados[i]

        # Mostrar los nuevos cromosomas después de la mutación
        print("\nNuevos cromosomas después de la mutación:")
        for fila in nuevos_cromosomas:
            print(fila)

        print("\n")

        reasignar_cromosomas( nuevos_cromosomas )


        generacion += 1 
        
if __name__ == "__main__":
    main()