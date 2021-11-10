# Exercice 1:

""" Utilisez la compréhension de liste pour à partir de la liste ma_liste, renvoyer une nouvelle liste ne comprennant seulement les nombres impair se situant juste après les nombres paires positif de cette liste.
 """
ma_liste = [3, -4, 8, 7, 20, 32, -9, 21]
list_1 = [ma_liste[i] for i in range(1, len(ma_liste)) if ma_liste[i]%2 != 0 and ma_liste[i-1] > 0 and ma_liste[i-1] %2 == 0]
print(list_1)

#Exercice 2:

""" Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
 """

lst1=[2, 4, 6, 8, 10, 12, 14]
list_2 = [i ** 2 for i in lst1 if i ** 2 > 50]
print(list_2)

# Exercice 3:

""" Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
 """
list_3 = [i for i in range(1200, 2000, 130)]
print(list_3)

# Exercice 4:

""" Given dictionary is consisted of vehicles and their weights in kilograms. Contruct a list of the names of vehicles with weight below 5000 kilograms. In the same list comprehension make the key names all upper case. """

dict = {"mazda" : 1000, "peugeot": 5100, "citroen": 1300, "mini-cooper": 900, "ford": 800, "renaut": 5900}
list_4 = [k.upper() for k,v in dict.items() if v<5000]
print(list_4)