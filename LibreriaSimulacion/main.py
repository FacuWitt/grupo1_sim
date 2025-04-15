import math

import modulos.modulo_histograma as histograma
import modulos.modulo_distribuciones as distribuciones
import modulos.modulo_chicuadrado as chi
import modulos.modulo_auxiliares as aux


def main():
    numeros = []
    cant_intervalos = None
    bins=None
    input_distribucion = 0


    while input_distribucion != 5:

        input_distribucion = aux.input_numero("\nIngrese la distribucion a usar: \n\t1 uniforme \n\t2 normal\n\t3 exponencial \n\t4 poisson \n\t5 SALIR\n\n =>", "int", min=1, max=5)
        if input_distribucion == 5:
            print("Fin del programa")
            break
        cant_numeros = aux.input_numero("Ingrese la cantidad de numeros a generar: ", "int")

        match input_distribucion:
            case 1:
                a = aux.input_numero("Ingrese el limite inferior: ", "float")
                b = aux.input_numero("Ingrese el limite superior: ", "float", min=a + 1)

                # TODO-> Generacion de numeros aleatorios con una distribucion UNIFORME
                numeros = distribuciones.distribucion_uniforme(a, b, cant_numeros)

                cant_intervalos = aux.input_numero(f"Ingrese la cantidad de intervalos a utilizar: ", "int")

                aux.mostrar_numeros(numeros, "d_uniforme")

                frec, lim_intervalos = histograma.mostrar_histograma(numeros, cant_col=cant_intervalos, title="Histograma Uniforme")

                # TODO  Calcular Chi_cuadrado=======================================

                alfa = aux.input_numero("Ingrese el alfa (valor flotante entre 0 y 1): ", "float", min=0, max=1)
                chi_cuadrado, chi_cuadrado_tab, grados_de_libertad = chi.chi_cuadrado_uniforme(frec, cant_numeros, alfa)

                print('\n---------------------------------------------')
                print(f"Grados de libertad: {grados_de_libertad}\n  Chi cuadrado calculado: {chi_cuadrado} \n  Chi cuadrado Tabla: {chi_cuadrado_tab}\n")
                print(f'{"No se rechaza" if chi_cuadrado_tab > chi_cuadrado else "Rechazada"}')
                print('---------------------------------------------')


            case 2:
                media = aux.input_numero("Ingrese la media: ", "float")
                desviacion = aux.input_numero("Ingrese la desviacion estandar: ", "float", min=0)

                # TODO-> Generacion de numeros aleatorios con una distribucion NORMAL
                numeros = distribuciones.distribucion_normal(desviacion, media, cant_numeros)


                cant_intervalos = aux.input_numero(f"Ingrese la cantidad de intervalos a utilizar para la grafica (recomendado: {round(3*math.log(cant_numeros) + 10)}): ", "int")

                aux.mostrar_numeros(numeros, "d_normal")

                # Generar histograma
                frec, lim_intervalos = histograma.mostrar_histograma(numeros, cant_col=cant_intervalos, title="Histograma Normal")


                # TODO  Calcular Chi_cuadrado=======================================
                alfa = aux.input_numero("Ingrese el alfa (valor flotante entre 0 y 1): ", "float", min=0, max=1)
                chi_cuadrado, chi_cuadrado_tab, grados_de_libertad = chi.chi_cuadrado_normal(frec, lim_intervalos, cant_numeros, desviacion, media, alfa)


                print('\n---------------------------------------------')
                print(f"Grados de libertad: {grados_de_libertad}\n  Chi cuadrado calculado: {chi_cuadrado} \n  Chi cuadrado Tabla: {chi_cuadrado_tab}\n")
                print(f'{"No se rechaza" if chi_cuadrado_tab > chi_cuadrado else "Rechazada"   }')
                print('---------------------------------------------')


            case 3:
                media = aux.input_numero("Ingrese la media: ", "float", min=0)

                # TODO-> Generacion de numeros aleatorios con una distribucion EXPONENCIAL
                numeros = distribuciones.distribucion_exponencial(media, cant_numeros)

                cant_intervalos = aux.input_numero(f"Ingrese la cantidad de intervalos a utilizar (recomendado: {round(3*math.log(cant_numeros) + 10)}): ", "int")

                aux.mostrar_numeros(numeros, "d_exponencial")

                frec, lim_intervalos = histograma.mostrar_histograma(numeros, cant_col=cant_intervalos, title="Histograma Exponencial")

                # TODO  Calcular Chi_cuadrado=======================================
                alfa = aux.input_numero("Ingrese el alfa (valor flotante entre 0 y 1): ", "float", min=0, max=1)
                chi_cuadrado, chi_cuadrado_tab, grados_de_libertad = chi.chi_cuadradro_exponecial(frec, cant_numeros, media, lim_intervalos, alfa)

                print('\n---------------------------------------------')
                print(f"Grados de libertad: {grados_de_libertad}\n  Chi cuadrado calculado: {chi_cuadrado}\n  Chi cuadrado Tabla: {chi_cuadrado_tab}\n")
                print(f'{"No se rechaza" if chi_cuadrado_tab > chi_cuadrado else "Rechazada"}')
                print('---------------------------------------------')

            case 4:
                media = aux.input_numero("Ingrese la media: ", "float", min=0)

                # TODO-> Generacion de numeros aleatorios con una distribucion POISSON
                numeros = distribuciones.distribucion_poisson(media, cant_numeros)

                # numeros = [14, 7, 13, 16, 16, 13, 14, 17, 15, 16, 13, 15, 10, 15, 16, 14, 12, 17, 14, 12, 13, 20, 8, 17, 19, 11, 12, 17, 9, 18, 20, 10, 18, 15, 13, 16, 24, 18, 16, 18, 12, 14, 20, 15, 10, 13, 21, 23, 18, 15]

                aux.mostrar_numeros(numeros, "d_poisson")

                frec, values = histograma.mostrar_barras(numeros, title="Histograma poisson") # devuelve los valores y frecuencias

                alfa = aux.input_numero("Ingrese el alfa (valor flotante entre 0 y 1): ", "float", min=0, max=1)

                # TODO  Calcular Chi_cuadrado=======================================
                chi_cuadrado, chi_cuadrado_tab, grados_de_libertad = chi.chi_cuadrado_poisson(frec, values, media, cant_numeros, alfa)

                print('\n---------------------------------------------')
                print(f"Grados de libertad: {grados_de_libertad}\n  Chi cuadrado calculado: {chi_cuadrado} \n  Chi cuadrado Tabla: {chi_cuadrado_tab}\n")
                print(f'{"No se rechaza" if chi_cuadrado_tab > chi_cuadrado else "Rechazada"}')
                print('---------------------------------------------')


            case _:
                print("Distribucion no valida")
                return





if __name__ == '__main__':
    main()

