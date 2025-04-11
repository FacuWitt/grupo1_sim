import matplotlib.pyplot as plt
from matplotlib.pyplot import autoscale, yticks, ylabel


# def histograma(num_matrix, cant_col=30, min_max=None, title="Histograma", name='name'):
#
#     for num_list in num_matrix:
#         if min or max:
#             plt.hist(num_list, bins=cant_col, range=min_max, alpha=1, label=name)
#
#         else:
#             plt.hist(num_list, bins=cant_col, density=True)
#         plt.xlabel('Intervalues')
#         plt.ylabel('Frequency')
#
#     plt.show()

def mostrar_histograma(num_datos, cant_col=None, title="Histograma"):

    count, bins, patches = plt.hist(num_datos, bins=cant_col, color='#2F4937', edgecolor='white', alpha=0.7)
    # count, bins, patches = plt.hist(num_datos, bins=binss, color='#2F4937', edgecolor='white', alpha=0.7)

    plt.xticks(bins, [f"{b:.2f}" for b in bins], rotation=70, fontsize=8)
    plt.tight_layout()

    # print (f'bins: {bins}')



    # for intervalo in range(len(bins) - 1):
    #     print(f'({bins[intervalo]} ; {bins[intervalo + 1]}) => {count[intervalo]}')

    plt.xlabel('Intervalos')
    plt.ylabel('Frecuencia')
    plt.title(title)

    plt.show()
    return count, bins