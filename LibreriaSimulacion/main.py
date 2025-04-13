import math

import grupo1_sim.LibreriaSimulacion.modulos.modulo_histograma as histograma
import grupo1_sim.LibreriaSimulacion.modulos.modulo_distribuciones as distribuciones
import grupo1_sim.LibreriaSimulacion.modulos.modulo_auxiliares as aux


from grupo1_sim.LibreriaSimulacion.modulos.modulo_auxiliares import input_numero
from grupo1_sim.LibreriaSimulacion.modulos.modulo_auxiliares import mostrar_numeros



def main():
    numeros = []
    cant_intervalos = None
    bins=None


    input_distribucion = 0

    while input_distribucion != 5:

        input_distribucion = aux.input_numero("Ingrese la distribucion a usar: \n\t1 uniforme \n\t2 normal\n\t3 exponencial \n\t4 poisson \n\t5 SALIR\n\n =>", "int", min=1, max=5)
        if input_distribucion == 5:
            print("Fin del programa")
            break
        cant_numeros = aux.input_numero("Ingrese la cantidad de numeros a generar: ", "int")

        match input_distribucion:
            case 1:
                a = input_numero("Ingrese el limite inferior: ", "float")
                b = input_numero("Ingrese el limite superior: ", "float", min=a + 1)

                # TODO-> Generacion de numeros aleatorios con una distribucion UNIFORME
                numeros = distribuciones.distribucion_uniforme(a, b, cant_numeros)

                cant_intervalos = input_numero(f"Ingrese la cantidad de intervalos a utilizar: ", "int")

            case 2:
                media = input_numero("Ingrese la media: ", "float")
                desviacion = input_numero("Ingrese la desviacion estandar: ", "float", min=0)

                # TODO-> Generacion de numeros aleatorios con una distribucion NORMAL
                numeros = distribuciones.distribucion_normal(desviacion, media, cant_numeros)


                cant_intervalos = input_numero(f"Ingrese la cantidad de intervalos a utilizar para la grafica (recomendado: {round(3*math.log(cant_numeros) + 10)}): ", "int")

                aux.mostrar_numeros(numeros, "d_normal")
            case 3:
                media = input_numero("Ingrese la media: ", "float", min=0)

                # TODO-> Generacion de numeros aleatorios con una distribucion EXPONENCIAL
                numeros = distribuciones.distribucion_exponencial(media, cant_numeros)

                cant_intervalos = input_numero(f"Ingrese la cantidad de intervalos a utilizar (recomendado: {round(3*math.log(cant_numeros) + 10)}): ", "int")

            case 4:
                media = input_numero("Ingrese la media: ", "float", min=0)

                # TODO-> Generacion de numeros aleatorios con una distribucion POISSON
                numeros = distribuciones.distribucion_poisson(media, cant_numeros)
                cant_intervalos = aux.input_numero(f"Ingrese la cantidad de intervalos a utilizar (Para una mejor representacion ingresar: {max(numeros) - min(numeros)}): ", "int")

            case _:
                print("Distribucion no valida")
                return

        # Generar histograma
        count, bins = histograma.mostrar_histograma(numeros, cant_col=cant_intervalos, title="Histograma de Ejemplo")

        # count y bins son arrays utiles para calcular la frecuencia relativa
        # TODO -> prueba de chi-cuadrado



if __name__ == '__main__':
    main()