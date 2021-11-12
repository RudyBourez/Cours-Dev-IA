#Exercice 1

""" Ecrire une fonction qui permet de calculer le produit des éléments d'une liste contenant des entiers"""

liste_1 = [1, 20, 90, 5, 13, 25]
liste_2 = [1, 2, 5]


def produit(liste):
    resultat = 1
    for element in range(len(liste)):
        resultat *= liste[element]
    print(resultat)

produit(liste_1)
produit(liste_2)    