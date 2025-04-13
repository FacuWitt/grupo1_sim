import matplotlib.pyplot as plt

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