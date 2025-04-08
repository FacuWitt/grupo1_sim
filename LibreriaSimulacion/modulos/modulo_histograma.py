import matplotlib.pyplot as plt

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

def mostrar_histograma(num_datos, cant_col=None, min_max=None, title="Histograma", name='name'):
    if min_max:
        # Quiero ver los intervalos

        plt.hist(num_datos, bins=cant_col, range=min_max, density=True, alpha=0.5, color='g')



    else:
        plt.hist(num_datos, bins=cant_col, color='#2F4937')
    plt.xlabel('Intervalues')
    plt.ylabel('Frequency')

    plt.show()