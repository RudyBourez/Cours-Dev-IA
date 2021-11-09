from typing import Type


def my_sort(liste):

    for index in range(len(liste)-1):
        if type(liste[index]) != type(liste[index+1]):
            raise(TypeError("Only integers are allowed"))

    while liste != sorted(liste):
        for index in range(len(liste)-1):
            if liste[index] > liste[index+1]:
                liste.append(liste.pop(index))
    return liste


