#Exercice 1 

liste_nombres = [1, 6, 98, 52, 1045, 3]

# 1) classez la liste
liste_nombres.sort()
print(liste_nombres)
# 2) supprimez le premier élément de la liste
liste_nombres.pop(0)
print(liste_nombres)
# 3) ajoutez le nombre "1097" à la fin de la liste
liste_nombres.append(1097)
print(liste_nombres)
# 4) récupérez le deuxième élément dans une variable "deuxieme_element"
deuxieme_element = liste_nombres[1]
print(deuxieme_element) # la console devrait afficher "6" !

# 5) affichez la longueur de la liste
print(len(liste_nombres))


liste_1 = [1, 2, 3, 4]
liste_2 = [5, 6, 7]

liste_2.extend(liste_1)
liste_1.append(liste_2)
print(liste_1)
print(liste_2)