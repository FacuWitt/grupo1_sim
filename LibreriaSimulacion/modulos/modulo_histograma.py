import matplotlib.pyplot as plt
from collections import Counter

def mostrar_histograma(num_datos, cant_col=None, title="Histograma"):

    # count, bins, patches = plt.hist(num_datos, bins=cant_col, color='#2F4937', edgecolor='grey', alpha=0.7)
    count, bins, patches = plt.hist(num_datos, bins=cant_col, color='#a73a3a', edgecolor='#ffc8c8')

    plt.xticks(bins, [f"{b:.2f}" for b in bins], rotation=70, fontsize=8)
    plt.tight_layout()

    plt.xlabel('Intervalos')
    plt.ylabel('Frecuencia')
    plt.title(title)

    plt.show()
    return count, bins

def mostrar_barras(valores, title="Histograma Discreto"):
    conteo = Counter(valores)

    # Asegurarse de incluir todos los valores intermedios con frecuencia 0
    minimo = min(valores)
    maximo = max(valores)
    claves_ordenadas = list(range(minimo, maximo + 1))
    frecuencias = [conteo.get(k, 0) for k in claves_ordenadas]

    # Graficar
    plt.bar(claves_ordenadas, frecuencias, color='#a73a3a', edgecolor='#ffc8c8')
    plt.xticks(claves_ordenadas, rotation=45)
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.title(title)
    plt.tight_layout()
    plt.show()

    return frecuencias, claves_ordenadas
