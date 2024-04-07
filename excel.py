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

def main():
    generacion = 0

    while ( generacion <= 50 ):    
        totalFitnesses, acum_suma = 0, 0 
        probabilities, acumulaciones = [], []

        fxs = [ f_deX( cromosoma_1 ), f_deX( cromosoma_2 ), f_deX( cromosoma_3 ), f_deX( cromosoma_4 ), f_deX( cromosoma_5 ), f_deX( cromosoma_6 ) ]

        print( "F(x) = [ ", end="" )
        print( " ".join( f"{ valor }" for valor in fxs ), end="" )
        print( " ]" )

        fitnesses = [ fitness( fxs[ 0 ] ), fitness( fxs[ 1 ] ), fitness( fxs[ 2 ] ), fitness( fxs[ 3 ] ), fitness( fxs[ 4 ] ), fitness( fxs[ 5 ] ) ]

        print( "Fitness = [ ", end="" )
        print( " ".join( f"{valor:.9f} " for valor in fitnesses ), end="" )
        print( " ]" )

        for aptitud in fitnesses:
            totalFitnesses += aptitud

        print( f"Total de fitness de la generación { generacion }" )
        print( totalFitnesses )

        for fitness_i in fitnesses:
            probabilities.append( fitness_i / totalFitnesses )

        print( "Probabilidades = [ ", end="" )
        print( " ".join( f"{valor:.9f} " for valor in probabilities ), end="" )
        print( " ]" )

        for probabilidad in probabilities:
            acum_suma += probabilidad
            acumulaciones.append( acum_suma )

        print( "Probabilidad acumulada = [ ", end="" )
        print( " ".join( f"{valor:.9f} " for valor in acumulaciones ), end="" )
        print( " ]" )

        generacion += 1 
        
if __name__ == "__main__":
    main()