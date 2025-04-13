import time
from datetime import datetime


import pandas as pd


def validar_int(valor, minimo=None, maximo=None):
    try:
        valor = int(valor)
        if valor <= 0 or (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
            raise ValueError("El numero debe ser positivo")
        return valor
    except ValueError:
        return None

def validar_float(valor, minimo=None, maximo=None):
    try:
        valor = float(valor)
        if valor <= 0 or (minimo is not None and valor < minimo) or (maximo is not None and valor > maximo):
            raise ValueError("El numero debe ser positivo")
        return valor
    except ValueError:
        return None

def input_numero(msg, tipo, min=None, max=None):

    valor = validar_int(input(msg), minimo=min, maximo=max) if tipo == "int" else validar_float(input(msg), minimo=min, maximo=max)

    while valor is None:
        print("Valor no valido, ingrese un numero valido")
        valor = validar_int(input(msg), minimo=min, maximo=max) if tipo == "int" else validar_float(input(msg), minimo=min, maximo=max)

    return valor

# def mostrar_numeros(numeros):
#     print("\n==================================================\n")
#     print("Numeros generados:")
#     for i in numeros:
#         print(i)
#     print("\n==================================================\n")

# def mostrar_numeros(numeros):
#     # mostrar todos los numeros
#     df = pd.DataFrame(numeros, columns=["Numeros Generados"])
#
#     print("\n==================================================\n")
#     print(df)
#     print("\n==================================================\n")


def mostrar_numeros(numeros, distribucion):
    # Asegurar que se muestren todos los elementos del DataFrame
    pd.set_option('display.max_rows', None)      # Mostrar todas las filas
    pd.set_option('display.max_columns', None)   # Mostrar todas las columnas
    pd.set_option('display.width', None)         # Ajustar al ancho total disponible
    pd.set_option('display.max_colwidth', None)  # Mostrar el contenido completo de cada celda

    ids = list(range(1, len(numeros) + 1))

    # df = pd.DataFrame(numeros, columns=["Numeros Generados"])
    df = pd.DataFrame({
        "Index": ids,
        "Numero generado": numeros
    })

    print("\n==================================================\n")
    print(df.to_string(index=False))
    print("\n==================================================\n")

    # Generar timestamp: mes, día, hora, minuto, segundo
    timestamp = datetime.now().strftime("%d-%m-%H%M%S")
    filename = f"recursos/numeros_generados_{distribucion}_{timestamp}.csv"

    df.to_csv(filename, index=False)
    print(f'Archivo "{filename}" guardado correctamente.')


# def fun(frec):
#     i_frec = 0
#     while i_frec <= len(frec) - 1:
#
#         print("==============")
#         print (frec[i_frec])
#
#         n = frec[i_frec] # Frecuencia observada
#
#         while n < 5:
#             print("i_frec:", i_frec)
#             print("n_anterior:", n)
#             n += frec[i_frec + 1]
#             i_frec += 1
#             print("n:", n)
#             print("i_final:", i_frec)
#         i_frec +=1



def fun(frec_obs):
    frec_ant = 0
    pos_inicial = 0
    pos_final = 0
    primer_entrada = True
    for i in range(len(frec_obs)):
        if (frec_obs[i] + frec_ant) < 5:
            if primer_entrada:
                pos_inicial = i
            primer_entrada = False
            frec_ant += frec_obs[i] # anterior mas actual
        else:
            pos_final = i
            primer_entrada = True


def agrupar_bins_frecuencia_baja(counts, bins, threshold=5):
    new_counts = []
    new_bins = [bins[0]]

    temp_count = 0
    temp_bin_start = bins[0]

    for i in range(len(counts)):
        temp_count += counts[i]

        if temp_count >= threshold:
            new_counts.append(temp_count)
            temp_count = 0
            new_bins.append(bins[i + 1])

    # Si quedaron frecuencias acumuladas sin agrupar
    if temp_count > 0:
        # Las sumamos al último grupo o las dejamos como grupo final
        if len(new_counts) > 0:
            new_counts[-1] += temp_count
            new_bins[-1] = bins[-1]
        else:
            new_counts.append(temp_count)
            new_bins.append(bins[-1])

    return new_counts, new_bins











