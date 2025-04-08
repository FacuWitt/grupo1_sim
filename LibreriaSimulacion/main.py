import grupo1_sim.LibreriaSimulacion.modulos.modulo_histograma as histograma
import grupo1_sim.LibreriaSimulacion.modulos.modulo_distribuciones as distribuciones

def main():

    # Generar lista de numeros aleatorios
    numeros = []

    input_distribucion = int(input("Ingrese la distribucion a usar: "
                               "    1 uniforme"
                               "    2 normal "
                               "    3 exponencial "
                               "    4 poisson "))
    cant_numeros = int(input("Ingrese la cantidad de numeros a generar: "))


    # match input_distribucion:

    match input_distribucion:
        case 1:
            # Generar numeros uniformes
            a = float(input("Ingrese el limite inferior: "))
            b = float(input("Ingrese el limite superior: "))
            numeros = distribuciones.distribucion_uniforme(a, b, cant_numeros)
        case 2:
            # Generar numeros normales
            media = float(input("Ingrese la media: "))
            desviacion = float(input("Ingrese la desviacion estandar: "))
            numeros = distribuciones.distribucion_normal(desviacion, media, cant_numeros)
        case 3:
            # Generar numeros exponenciales
            media = float(input("Ingrese la media: "))
            numeros = distribuciones.distribucion_exponencial(media, cant_numeros)
        case 4:
            # Generar numeros poisson
            media = float(input("Ingrese la media: "))
            numeros = distribuciones.distribucion_poisson(media, cant_numeros)
        case _:
            print("Distribucion no valida")
            return





    # Generar histograma
    histograma.mostrar_histograma(numeros, title="Histograma de Ejemplo", name="Ejemplo")

if __name__ == '__main__':
    main()