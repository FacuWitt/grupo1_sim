import math
from scipy.stats import chi2

def valor_chi_cuadrado(gl, alfa):
    """
    Retorna el valor crítico del Chi-cuadrado para un nivel de significancia dado.

    Parámetros:
    - gl: grados de libertad (int)
    - alfa: nivel de significancia (float, entre 0 y 1)

    Retorna:
    - valor crítico del chi-cuadrado (float)
    """
    return chi2.ppf(1 - alfa, gl)


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

def dist_densidad_normal(x, media, desviacion):
    # Calcular la densidad de probabilidad de la distribución normal
    return (1 / (desviacion * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - media) / desviacion) ** 2)

def dist_densidad_poisson(lambd, x):
    return ((lambd ** x) * math.exp(-lambd)) / math.factorial(int(x))

def dist_densidad_exponencial(lambd, lim_intervalo, lim_intervalo_sig):
    marca = (lim_intervalo + lim_intervalo_sig) / 2
    return lambd * math.exp(-lambd * marca) * (lim_intervalo_sig -lim_intervalo)

def dist_densidad_exponecial_acum(lamb, lim_intervalo, lim_intervalo_sig):
    return (1 - math.exp(-lamb * lim_intervalo_sig)) - (1 - math.exp(-lamb * lim_intervalo))

def chi_cuadrado_normal(frec, lim_intervalos, cant_numeros, desviacion, media, alfa=0.05):
    cant_intervalos = len(frec)
    marca = []
    frec_esperada = []
    for i in range(cant_intervalos):
        marca = (lim_intervalos[i] + lim_intervalos[i+1]) / 2
        prob_x = dist_densidad_normal(marca, media, desviacion) * (lim_intervalos[i+1] - lim_intervalos[i])
        frec_esperada.append(prob_x * cant_numeros)

    frec, frec_esperada, lim_intervalos = agrupar_bins_con_esperadas(frec, lim_intervalos, frec_esperada)
    chi_cuadrado = 0
    for i in range(len(frec)):
        chi_cuadrado += ((frec[i] - frec_esperada[i]) ** 2) / frec_esperada[i]

    chi_cuadrado_tab = valor_chi_cuadrado(len(frec) - 1, alfa)

    return chi_cuadrado, chi_cuadrado_tab, len(frec) - 1

def chi_cuadrado_uniforme(frec_obs, cant_numeros, alfa=0.05):
    cant_intervalos = len(frec_obs)
    frec_esperada = cant_numeros / cant_intervalos
    chi_cuadrado = 0
    for i in range(len(frec_obs)):
        chi_cuadrado += ((frec_obs[i] - frec_esperada) ** 2) / frec_esperada

    chi_cuadrado_tab = valor_chi_cuadrado(cant_intervalos - 1, alfa)
    return chi_cuadrado, chi_cuadrado_tab, len(frec_obs) - 1

def chi_cuadrado_poisson(frec_observadas, values, media, cant_numeros, alfa=0.05):
    frec_esperada = []
    for x in values:
        prob_x = dist_densidad_poisson(media, x)
        frec_esperada.append(round(prob_x * cant_numeros))


    frec_observadas, frec_esperada, values = agrupar_valores_con_esperadas(frec_observadas, values, frec_esperada)

    chi_cuadrado = 0

    for i in range(len(frec_observadas)):
        chi_cuadrado += ((frec_observadas[i] - frec_esperada[i]) ** 2) / frec_esperada[i]

    chi_cuadrado_tab = valor_chi_cuadrado(len(frec_observadas) - 1, alfa)
    return chi_cuadrado, chi_cuadrado_tab, len(frec_observadas) - 1

def chi_cuadradro_exponecial(frec_obs, cant_numeros, media, lim_intervalos, alfa=0.05):
    cant_intervalos = len(frec_obs)

    frec_esp = []
    lambd = 1/media
    for i in range(cant_intervalos):
        #prob_x = dist_densidad_exponencial(lambd, lim_intervalos[i], lim_intervalos[i + 1])
        prob_x = dist_densidad_exponecial_acum(lambd, lim_intervalos[i], lim_intervalos[i+1])
        frec_esp.append(prob_x * cant_numeros)

    frec_obs, frec_esperada, lim_intervalos = agrupar_bins_con_esperadas(frec_obs, lim_intervalos, frec_esp)
    chi_cuadrado = 0
    for i in range(len(frec_obs)):
        chi_cuadrado += ((frec_obs[i] - frec_esperada[i]) ** 2) / frec_esperada[i]

    chi_cuadrado_tab = valor_chi_cuadrado(len(frec_obs) - 1, alfa)

    return chi_cuadrado, chi_cuadrado_tab, len(frec_obs) - 1





# counts = [0, 1, 3, 4, 8, 7, 5, 2, 0, 0]
# bins =   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# counts_esperada = [0.1550, 0.7567, 2.4464, 5.2369, 7.4226, 6.9660, 4.3286, 1.7809, .4852, 0.0875 ]
#
# print(counts)
# print(bins)
# print(counts_esperada)
#
# # Agrupar bins con frecuencias esperadas
# new_counts, new_bins, new_counts_esp = agrupar_bins_con_esperadas(counts, bins, counts_esperada)
#
# print("=====")
# print("obs:", new_counts)
# print("newbins:", new_bins)
# print("esp:", new_counts_esp)
#
#
