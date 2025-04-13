import math


# def agrupar_bins_frecuencia_baja(frec, lim_intervalos, threshold=5):
#     new_counts = []
#     new_bins = [lim_intervalos[0]]
#
#     temp_count = 0
#     temp_bin_start = lim_intervalos[0]
#
#     for i in range(len(frec)):
#         temp_count += frec[i]
#
#         if temp_count >= threshold:
#             new_counts.append(temp_count)
#             temp_count = 0
#             new_bins.append(lim_intervalos[i + 1])
#
#     # Si quedaron frecuencias acumuladas sin agrupar
#     if temp_count > 0:
#         # Las sumamos al último grupo o las dejamos como grupo final
#         if len(new_counts) > 0:
#             new_counts[-1] += temp_count
#             new_bins[-1] = lim_intervalos[-1]
#         else:
#             new_counts.append(temp_count)
#             new_bins.append(lim_intervalos[-1])
#
#     return new_counts, new_bins

import numpy as np

def agrupar_bins_con_esperadas(frec_obs, bins, frec_esp, threshold=5):
    new_obs = []
    new_esp = []
    new_bins = [bins[0]]

    temp_obs = 0
    temp_esp = 0

    for i in range(len(frec_obs)):
        temp_obs += frec_obs[i]
        temp_esp += frec_esp[i]

        if temp_obs >= threshold:
            new_obs.append(temp_obs)
            new_esp.append(temp_esp)
            new_bins.append(bins[i+1])
            temp_obs = 0
            temp_esp = 0

    # Si quedaron restos sin agrupar
    if temp_obs > 0:
        if len(new_obs) > 0:
            new_obs[-1] += temp_obs
            new_esp[-1] += temp_esp
            new_bins[-1] = bins[-1]
        else:
            new_obs.append(temp_obs)
            new_esp.append(temp_esp)
            new_bins.append(bins[-1])

    return new_obs, new_esp, new_bins

def dist_densidad_normal(x, media, desviacion):

    # Calcular la densidad de probabilidad de la distribución normal
    return (1 / (desviacion * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - media) / desviacion) ** 2)

def chi_cuadrado_normal(frec, lim_intervalos, cant_numeros, desviacion, media):

    cant_intervalos = len(frec)

    marca = []
    # prob_x = []
    frec_esperada = []

    for i in range(cant_intervalos):
        # marca.append((lim_intervalos[i] + lim_intervalos[i+1]) / 2)
        marca = (lim_intervalos[i] + lim_intervalos[i+1]) / 2

        # prob_x.append(dist_densidad_normal(marca, media, desviacion) * (lim_intervalos[i+1] - lim_intervalos[i]))

        prob_x = dist_densidad_normal(marca, media, desviacion) * (lim_intervalos[i+1] - lim_intervalos[i])

        frec_esperada.append(prob_x * cant_numeros)

        # frec, lim_intervalos = agrupar_bins_frecuencia_baja(frec, lim_intervalos)
        # frec_esperada, lim_intervalos = agrupar_bins_frecuencia_baja(frec_esperada, lim_intervalos)


        print(frec)
        print(frec_esperada)
        print(lim_intervalos)

        frec, frec_esperada, lim_intervalos = agrupar_bins_con_esperadas(frec, lim_intervalos, frec_esperada)

        print("\n=====\n")
        print(frec)
        print(frec_esperada)
        print(lim_intervalos)

counts = [0, 1, 3, 4, 8, 7, 5, 2, 0, 0]
bins =   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counts_esperada = [0.1550, 0.7567, 2.4464, 5.2369, 7.4226, 6.9660, 4.3286, 1.7809, .4852, 0.0875 ]

print(counts)
print(bins)
print(counts_esperada)

# Agrupar bins con frecuencias esperadas
new_counts, new_bins, new_counts_esp = agrupar_bins_con_esperadas(counts, bins, counts_esperada)

print("=====")
print("obs:", new_counts)
print("newbins:", new_bins)
print("esp:", new_counts_esp)


