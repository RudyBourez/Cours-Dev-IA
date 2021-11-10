# Exercice 1:

""" Create a dictionary from the list with same key:value pairs, such as: {"key": "key"}.
 """

lst=["NY", "FL", "CA", "VT"]

dict={k:k for k in lst}
print(dict)

# Exercice 2:

""" First, create a range from 100 to 160 with steps of 10. Second, using dict comprehension, create a dictionary where each number in the range is the key and each item divided by 100 is the value. """

my_dict = {k:k/100 for k in range(100, 160, 10)}
print(my_dict)

# Exercice 3:

""" Using dict comprehension and a conditional argument create a dictionary from the current dictionary where only the key:value pairs with value above 2000 are taken to the new dictionary.
 """

dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}

my_dict_1 = {k:v for k,v in dict1.items() if v > 2000}
print(my_dict_1)

# Exercice 4: 

""" En utilisant la fonction zip() et la comprehension de dictionnaire, créer un dictionnaire qui prend comme clef les valeurs de la première liste et en valeur les valeurs de la seconde
 """

lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]

my_dict_2 = {k:v for k,v in zip(lst1, lst2)}
print(my_dict_2)