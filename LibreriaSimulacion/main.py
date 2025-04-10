import math

import grupo1_sim.LibreriaSimulacion.modulos.modulo_histograma as histograma
import grupo1_sim.LibreriaSimulacion.modulos.modulo_distribuciones as distribuciones
import grupo1_sim.LibreriaSimulacion.modulos.modulo_auxiliares as aux


def main():

    # todo Generar lista de numeros aleatorios
    numeros = []

    input_distribucion = int(input("Ingrese la distribucion a usar: "
                               "    1 uniforme"
                               "    2 normal "
                               "    3 exponencial "
                               "    4 poisson "))

    # cant_numeros = int(input("Ingrese la cantidad de numeros a generar: "))

    # TODO> PROBANDO VALIDACIONES (A MEJORAR)
    cant_numeros = aux.input_numero("Ingrese la cantidad de numeros a generar: ", "int")



    # cant_intervalos = int(input(f"Ingrese la cantidad de intervalos a utilizar (recomendado: {round(cant_numeros ** (1/2))}): "))
    # cant_intervalos = int(input(f"Ingrese la cantidad de intervalos a utilizar (recomendado: {round(3*math.log(cant_numeros) + 10)}): "))
    cant_intervalos = None


    # match input_distribucion:

    bins=None

    match input_distribucion:
        case 1:
            # Generar numeros uniformes
            a = float(input("Ingrese el limite inferior: "))
            b = float(input("Ingrese el limite superior: "))

            numeros = distribuciones.distribucion_uniforme(a, b, cant_numeros)

            cant_intervalos = int(input(f"Ingrese la cantidad de intervalos a utilizar: "))
        case 2:
            # Generar numeros normales
            media = float(input("Ingrese la media: "))
            desviacion = float(input("Ingrese la desviacion estandar: "))
            numeros = distribuciones.distribucion_normal(desviacion, media, cant_numeros)

            cant_intervalos = int(input(f"Ingrese la cantidad de intervalos a utilizar (recomendado: {round(3*math.log(cant_numeros) + 10)}): "))
        case 3:
            # Generar numeros exponenciales
            media = float(input("Ingrese la media: "))
            numeros = distribuciones.distribucion_exponencial(media, cant_numeros)

            cant_intervalos = int(input(f"Ingrese la cantidad de intervalos a utilizar (recomendado: {round(3*math.log(cant_numeros) + 10)}): "))
        case 4:
            # Generar numeros poisson
            media = float(input("Ingrese la media: "))
            numeros = distribuciones.distribucion_poisson(media, cant_numeros)
            maximo_numero = max(numeros)

            input_cant_intervalos = int(input(f"Ingrese la cantidad de intervalos a utilizar (Para una mejor representacion ingresar: {maximo_numero}): "))
            # cant_intervalos=[i for i in range(0, max(numeros) + 1)]

            #operador ternario

            cant_intervalos = [i for i in range(min(numeros), input_cant_intervalos + 1)] if input_cant_intervalos == maximo_numero else input_cant_intervalos

        case _:
            print("Distribucion no valida")
            return

    # Generar histograma

    histograma.mostrar_histograma(numeros, cant_col=cant_intervalos, title="Histograma de Ejemplo")

if __name__ == '__main__':
    main()