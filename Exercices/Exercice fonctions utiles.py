#-----------------------------------------------Enumerate--------------------------------------------------------

# Exercice 1:

"""A l'aide de enumerate et d'une dictionnary comprehension, créer un dictionnaire avec pour clef la valeur de la liste et
comme valeur, cette valeur de la liste exprimée en integer"""

keys_list = ["one", "two", "three", "for", "five"]

dict_1 = {k:v for v,k in enumerate(keys_list,1)}
print(dict_1)

# Exercice 2:

"""En utilisant la fonction enumerate, renvoyer une liste qui rassemble les deux autres"""

liste_1 = ["a", "b", "c", "d"]
liste_2 = ["e", "f", "g", "h"]

liste = [liste_1[i]+j for i,j in enumerate(liste_2)]
print(liste)

#----------------------------------------------------Lambda--------------------------------------------------------

# Exercice 1

""" Write a lambda function that takes x as parameter and returns x+2. Then assign it to a variable named L.
 """
i=6

L= lambda x: x + 2
print(L(i))

# Exercice 2

""" Write a function which takes two arguments: a and b and returns the multiplication of them: a*b. Assign it to a variable named: f.
 """

i,j=5,10
f = lambda i,j : i * j

print(f(i, j))

# Exercice 3`

""" Use the sorted() function to sort the list in ascending order with lambda.
 """

lst1=[100, 10, 10000, 1, 9, 999, 99]
lst1_sorted = lambda x: sorted(x)

print(lst1_sorted(lst1))

# Exercice 4

""" Using sorted() function and lambda sort the words in the list based on their second letter from a to z.
 """

lst2=["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]
lst2_sorted = sorted(lst2, key=lambda item: item[1:])

print(lst2_sorted)

# Exercice 5

"""Using sorted() function and lambda, sort the tuples based on the last character of the second items"""

lst3=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
lst3_sorted = sorted(lst3, key=lambda item: item[1][::-1])

print(lst3_sorted)

#-----------------------------------------------------Map----------------------------------------------------------

# Exercice 1:
""" A l'aide de Map et lambda, ajoutez une majuscule aux éléments de cette liste"""

liste_3 = ["alpha", "beta", "gamma"]
list_capitalized = list(map(lambda x: x.capitalize(), liste_3))

print(list_capitalized)

# Exercice 2:
""" A l'aide de Map et lambda, renvoyez une liste des arrondis"""

liste_4 = [3.8 , 8.5 , 5.0 , 9.3]
list_round = list(map(lambda x: round(x),liste_4))

print(list_round)

#-----------------------------------------------------Filter----------------------------------------------------------

# Exercice 1:

""" En une ligne revoyer uniquement les prénoms de 4 lettres ou moins"""

liste_5 = ["Bernard", "Fred", "Alain", "Zoé", "Cléroncle", "Denis", "Paul"]
list_filtered = list(filter(lambda x: len(x) <= 4, liste_5))

print(list_filtered)

# Exercice 2: 

""" En une ligne revoyer (en utilisant filter et enumerate) uniquement les chiffre dont la première valeurs 
 la virgule est supérieur ou égale à 7"""

liste_6 = [3.789, 34.34, 28.965, 0.22, 4.674, 1098.99]
liste_filter_enumerate = list(filter(lambda x: 0.7 <= x - int(x), liste_6))

print(liste_filter_enumerate)