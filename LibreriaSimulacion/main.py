import math

import modulos.modulo_histograma as histograma
import modulos.modulo_distribuciones as distribuciones
import modulos.modulo_auxiliares as aux
import modulos.modulo_chicuadrado as chi
from modulos.modulo_auxiliares import input_numero
from modulos.modulo_auxiliares import mostrar_numeros

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

                #aux.mostrar_numeros(numeros, "d_uniforme")

                frec, lim_intervalos = histograma.mostrar_histograma(numeros, cant_col=cant_intervalos, title="Histograma Uniforme")
                print(frec, "\n", lim_intervalos)
                #  Calcular Chi_cuadrado
                chi_cuadrado = chi.chi_cuadrado_uniforme(frec, cant_numeros)
                print(f"Chi cuadrado: {chi_cuadrado} \nCantidad de intervalos: {len(frec)} \n")
            case 2:
                media = input_numero("Ingrese la media: ", "float")
                desviacion = input_numero("Ingrese la desviacion estandar: ", "float", min=0)

                # TODO-> Generacion de numeros aleatorios con una distribucion NORMAL
                numeros = distribuciones.distribucion_normal(desviacion, media, cant_numeros)


                cant_intervalos = input_numero(f"Ingrese la cantidad de intervalos a utilizar para la grafica (recomendado: {round(3*math.log(cant_numeros) + 10)}): ", "int")

                #aux.mostrar_numeros(numeros, "d_normal")

                # Generar histograma
                frec, lim_intervalos = histograma.mostrar_histograma(numeros, cant_col=cant_intervalos, title="Histograma Normal")
                # Calcular chi cuadrado
                chi_cuadrado, cantidad_int = chi.chi_cuadrado_normal(frec, lim_intervalos, cant_numeros, desviacion, media)
                print(f"Chi cuadrado: {chi_cuadrado} \nCantidad de intervalos: {cantidad_int} \n")


            case 3:
                media = input_numero("Ingrese la media: ", "float", min=0)

                # TODO-> Generacion de numeros aleatorios con una distribucion EXPONENCIAL
                numeros = distribuciones.distribucion_exponencial(media, cant_numeros)

                cant_intervalos = input_numero(f"Ingrese la cantidad de intervalos a utilizar (recomendado: {round(3*math.log(cant_numeros) + 10)}): ", "int")

                #aux.mostrar_numeros(numeros, "d_exponencial")

                frec, lim_intervalos = histograma.mostrar_histograma(numeros, cant_col=cant_intervalos, title="Histograma Exponencial")
            case 4:
                media = input_numero("Ingrese la media: ", "float", min=0)

                # TODO-> Generacion de numeros aleatorios con una distribucion POISSON
                numeros = distribuciones.distribucion_poisson(media, cant_numeros)
                cant_intervalos = aux.input_numero(f"Ingrese la cantidad de intervalos a utilizar (Para una mejor representacion ingresar: {max(numeros) - min(numeros)}): ", "int")

                #aux.mostrar_numeros(numeros, "d_poisson")

                frec, lim_intervalos = histograma.mostrar_histograma(numeros, cant_col=cant_intervalos, title="Histograma Poisson")

                #Calculo chi cuadrado
                chi_cuadrado, cantidad_int = chi.chi_cuadrado_poaasson(frec, lim_intervalos, media, cant_numeros)
                print(f"Chi cuadrado: {chi_cuadrado} \nCantidad de intervalos: {cantidad_int} \n")
            case _:
                print("Distribucion no valida")
                return





if __name__ == '__main__':
    main()