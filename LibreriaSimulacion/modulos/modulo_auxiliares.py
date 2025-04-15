
from datetime import datetime
# from modulo_chicuadrado import chi_cuadrado_normal as chi_cuadrado_normal
# from modulo_chicuadrado import chi_cuadrado_uniforme as chi_cuadrado_uniforme
# from modulo_chicuadrado import chi_cuadradro_exponecial as chi_cuadrado_exponencial

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


def agrupar_valores_con_esperadas(frec_obs, bins, frec_esp, threshold=5):
    new_obs = []
    new_esp = []
    new_bins = [bins[0]]  # Inicio de los intervalos

    temp_obs = frec_obs[0]
    temp_esp = frec_esp[0]

    for i in range(1, len(frec_obs)):
        if temp_obs < threshold:
            # Aún no alcanza el umbral, seguir acumulando
            temp_obs += frec_obs[i]
            temp_esp += frec_esp[i]
        else:
            # Ya superó el umbral, guardar lo acumulado y arrancar nuevo grupo
            new_obs.append(temp_obs)
            new_esp.append(temp_esp)
            new_bins.append(bins[i])  # Marcamos el nuevo corte

            temp_obs = frec_obs[i]
            temp_esp = frec_esp[i]

    # Agregar los últimos valores si quedó algo sin cerrar
    if new_obs and temp_obs < threshold:
        # Agrupar al último grupo
        new_obs[-1] += temp_obs
        new_esp[-1] += temp_esp
        new_bins[-1] = bins[-1]
    else:
        # Nuevo grupo final si era suficiente
        new_obs.append(temp_obs)
        new_esp.append(temp_esp)
        new_bins.append(bins[-1])

    return new_obs, new_esp, new_bins


#VALIDAR SI ESTA BIEN HECHO CHI_UNIFORME CON LOS EJEMPLOS DEL PROFE
# def probar_chi_cuadrado_uniforme_profe():
#     datos_uniforme = [0.15, 0.22, 0.41, 0.65, 0.84, 0.81, 0.62, 0.45, 0.32, 0.07,
#     0.11, 0.29, 0.58, 0.73, 0.93, 0.97, 0.79, 0.55, 0.35, 0.09,
#     0.99, 0.51, 0.35, 0.02, 0.19, 0.24, 0.98, 0.10, 0.31, 0.17]
#     frec_obse = [8, 7,5,4,6]
#     chi_uni = chi_cuadrado_uniforme(frec_obse, len(datos_uniforme))
#     print("Valor de chi: ", chi_uni)
#
# #VALIDAR SI ESTA BIEN HECHO CHI_NORMAL CON LOS EJEMPLOS DEL PROFE
# def probar_chi_normal_profe():
#     frec_obs = [0, 1, 3, 4, 8, 7, 5, 2, 0, 0]
#     lim_intervalos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#     chi_calculado, intervalos = chi_cuadrado_normal(frec_obs,lim_intervalos, 30,1.5574,4.8410)
#     print("Valor de chi= " , chi_calculado, "\nIntervalos = ", intervalos)
#
# def probar_chi_exp_profe():
#     frec_obs = [18,10,9,8,3,1,1]
#     media = 2.4984
#     cant_numeros = 50
#     lim_intervalos = [0.10, 1.28, 2.46, 3.64, 4.82, 6.00, 7.18, 8.36]
#     chi_exp, intervalos = chi_cuadrado_exponencial(frec_obs, cant_numeros, media, lim_intervalos)
#     print("Valor de chi exp= ", chi_exp, "\nIntervalos = ", intervalos)
#
#
# # def probar_chi_poisson_profe():
# #     valores = [1, 1, 1, 3, 1, 4, 6, 5, 6, 6, 4, 5, 1, 3, 1, 0, 1, 1]
# #     media = 15.04
# #     n = 50
# #     lim_intervalos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #     chi_calculado, intervalos = chi_cuadrado_poaasson(valores,media, n)
# #     print("Valor de chi= ", chi_calculado, "\nIntervalos = ", intervalos)
#
#
# probar_chi_cuadrado_uniforme_profe()
# probar_chi_normal_profe()
# probar_chi_exp_profe()
#probar_chi_poisson_profe()
