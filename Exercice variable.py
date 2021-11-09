#Exercice 1

name = "DRUESNES"
first_name = "Steven"
second_first_name = "Oliver"
full_name = f'{name} {first_name}, {second_first_name}'

print(full_name)

actual_year = 2021
birth_date = 1992
age = actual_year - birth_date

print(f'{age} ans')

name = full_name
del full_name

print(name, str(age) + " ans")
print("------------------------------------------------")

# Exercice 2

# print(5 - 3 // 2) : Ajouter parenthèse pour que ce soit égal à 1
print((5 - 3) // 2)
print("------------------------------------------------")

#Exercice 3

# print(8 - 3 * 2 - 1 + 1) : Ajouter parenthèse pour que ce soit égal à 0
print(8 - (3 * 2) - (1 + 1))
print("------------------------------------------------")

#Exercice 4

""" Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. For the sake of their friendship, any candies left over will be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
Write an arithmetic expression below to calculate how many candies they must smash for a given haul. """

alice_candies = 121
bob_candies = 77
carol_candies = 109

smashed_candies = (alice_candies + bob_candies + carol_candies) % 3
print(smashed_candies)
print("------------------------------------------------")

#Exercice 5 

""" Travaillez sur la définition de python:

Remplacez python par lovely python partout dans la chaine de caractère suivante
Affichez la chaine suivante en une seule chaine de caractères en sautant une ligne entre chaque phrase et en faisant commencer chaque phrase par une majuscule (

Indice:

On calcule le nombre d'élément d'une liste de la meme manière qu'on calcule la longueur d'une chaine de caratère
On accède au nème éléments d'une liste de la même manière qu'on accède nème caractère d'une chaine de caractères. """

python_definition = "python is an interpreted high-level general-purpose programming language. its design philosophy emphasizes code readability with its use of significant indentation. its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
new_python_definition = python_definition.replace("python", "lovely python")
splitted_python_definition = new_python_definition.split(". ")

first_line = splitted_python_definition[0].capitalize() + "." + "\n"
second_line = splitted_python_definition[1].capitalize() + "." + "\n"
last_line = splitted_python_definition[2].capitalize()

last_python_definition = first_line + second_line + last_line

print(last_python_definition)

test = ""
for element in range(len(splitted_python_definition)):
    if element == len(splitted_python_definition) - 1:
        element = splitted_python_definition[element].capitalize()
        test += element
    else:
        element = splitted_python_definition[element].capitalize() + "." + "\n"
        test += element

print(test)