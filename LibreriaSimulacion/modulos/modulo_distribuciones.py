import numpy as np
import math

def generar_random(): #>> retorna valor random entre 0 y 1
    #Generar numero random
    return np.random.rand()


# DISTRIBUCION UNIFORME: distribucion_uniforme(a, b)
def distribucion_uniforme(a, b, cant_num):
    lista_num_uniformes = []
    for i in range(cant_num):
        lista_num_uniformes.append(generar_random() * (b - a) + a)
    return lista_num_uniformes


# DISTRIBUCION NORMAL: distribucion normal(desviacion, media)
def distribucion_normal(desviacion, media, cant_num):

    lista_num_normales = []
    for i in range(0, cant_num, 2):
        r1, r2 = generar_random(), generar_random()
        z1 = (math.sqrt(-2 * math.log(r1, math.e)) * math.cos(2 * math.pi * r2)) * desviacion + media
        z2 = math.sqrt(-2 * math.log(r1, math.e)) * math.sin(2 * math.pi * r2) * desviacion + media
        lista_num_normales += [z1, z2]

    return lista_num_normales


# DISTRIBUCION EXPONENCIAL: distribucion_exponencial(media)
def distribucion_exponencial(media, cant_num):
    lista_num_exponenciales = []
    for i in range(cant_num):
        lista_num_exponenciales.append(math.log(1 - generar_random(), math.e) * (-media))

    return lista_num_exponenciales

# DISTRIBUCION POISSON: distribucion_poisson(media)

def distribucion_poisson(lambd, cant_num):

    lista_num_poisson = []

    for i in range(cant_num):
        p = 1
        x = -1
        a = math.e ** (-lambd)


        while p >= a:
            u = generar_random()
            p *= u
            x += 1
        lista_num_poisson.append(x)
    return lista_num_poisson