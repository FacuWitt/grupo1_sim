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




