import random
import numpy


# Inverse et return la valeur a et b
def swap(a, b):
    return b, a


# Trie tout les éléments de la list en deux sous tableaux
# L'absolute_value est une valeur aléatoire qui nous sert de valeur de référence pour trié les valeurs du tableau
# Toutes les valeurs inférieure à l'absolute value sont stocker dans under_absolute
# Toutes les valeurs supérieure à l'absolute value sont stocker dans over_absolute
# Return deux list : under_absolute, over_absolute
def sort_under_over_value(list, begin, end):
    under_absolute = begin
    index = begin
    over_absolute = end
    absolute_value = list[begin]

    while index <= over_absolute:
        if list[index] < absolute_value:
            list[under_absolute], list[index] = swap(list[under_absolute], list[index])
            under_absolute += 1
            index += 1
        elif list[index] > absolute_value:
            list[over_absolute], list[index] = swap(list[over_absolute], list[index])
            over_absolute -= 1
        else:
            index += 1
    return under_absolute, over_absolute


# Fonction récursive qui définie l'absolute_value, puis qui l'insére dans la fonction sort_under_over_value
# Premiere récursive pour trié les valeurs dans le tableau under_absolute
# Premiere récursive pour trié les valeurs dans le tableau over_absolute
def recursive_sort(list, begin, end):
    if begin >= end:
        return
    absolute_value = random.randint(begin, end)
    list[absolute_value], list[begin] = swap(list[absolute_value], list[begin])

    under_absolute, over_absolute = sort_under_over_value(list, begin, end)

    recursive_sort(list, begin, under_absolute - 1)
    recursive_sort(list, over_absolute + 1, end)
    return list


def parcours(list):
    sort = recursive_sort(list, 0, len(list) - 1)
    return sort


size = 1000
llist = numpy.random.normal(0, size, size).tolist()
print(parcours(llist))